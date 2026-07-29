from datetime import datetime,timezone
from fastapi import HTTPException
from ..database import db
from ..utils.object_id import oid,serialize
from .project_service import log
now=lambda:datetime.now(timezone.utc)
async def list_tasks(pid): return serialize(await db.tasks.find({"projectId":oid(pid)}).sort("createdAt",-1).to_list(500))
async def create(data):
 doc={**data,"projectId":oid(data["projectId"]),"createdAt":now(),"updatedAt":now(),"completedAt":None}; r=await db.tasks.insert_one(doc); await log(doc["projectId"],"task_created",f"Tarefa {doc['title']} criada"); return serialize(await db.tasks.find_one({"_id":r.inserted_id}))
async def update(tid,data):
 data["projectId"]=oid(data["projectId"]); data["updatedAt"]=now(); await db.tasks.update_one({"_id":oid(tid)},{"$set":data}); return serialize(await db.tasks.find_one({"_id":oid(tid)}))
async def status(tid,value):
 doc=await db.tasks.find_one({"_id":oid(tid)});
 if not doc: raise HTTPException(404,"Tarefa não encontrada")
 fields={"status":value,"updatedAt":now(),"completedAt":now() if value=="concluída" else None}; await db.tasks.update_one({"_id":doc["_id"]},{"$set":fields});
 if value=="concluída": await log(doc["projectId"],"task_completed",f"Tarefa {doc['title']} concluída")
 return serialize({**doc,**fields})
async def generate(pid):
 templates=[("Definir vertical slice","feature","alta"),("Revisar performance da cena principal","performance","alta"),("Criar testes de regressão","QA","média")]; return [await create({"projectId":pid,"title":t,"description":"Gerada pelo assistente local","category":c,"priority":p,"status":"backlog","assignedTo":"","estimatedHours":4}) for t,c,p in templates]
