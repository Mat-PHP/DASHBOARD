from datetime import datetime,timezone
from fastapi import HTTPException
from ..database import db
from ..utils.object_id import oid,serialize
now=lambda:datetime.now(timezone.utc)
async def list_projects(search="",status=None):
 q={};
 if search:q["$or"]=[{"name":{"$regex":search,"$options":"i"}},{"genre":{"$regex":search,"$options":"i"}}]
 if status:q["status"]=status
 return serialize(await db.projects.find(q).sort("updatedAt",-1).to_list(200))
async def get_project(pid):
 doc=await db.projects.find_one({"_id":oid(pid)})
 if not doc: raise HTTPException(404,"Projeto não encontrado")
 return serialize(doc)
async def create_project(data):
 stamp=now(); doc={**data,"createdAt":stamp,"updatedAt":stamp}; result=await db.projects.insert_one(doc); await log(result.inserted_id,"project_created",f"Projeto {doc['name']} criado"); return await get_project(str(result.inserted_id))
async def update_project(pid,data):
 data["updatedAt"]=now(); result=await db.projects.update_one({"_id":oid(pid)},{"$set":data})
 if not result.matched_count: raise HTTPException(404,"Projeto não encontrado")
 await log(oid(pid),"project_updated","Projeto atualizado"); return await get_project(pid)
async def delete_project(pid):
 project=await get_project(pid); await db.projects.delete_one({"_id":oid(pid)}); await log(None,"project_deleted",f"Projeto {project['name']} excluído"); return {"deleted":True}
async def log(project_id,kind,description): await db.activities.insert_one({"projectId":project_id,"type":kind,"description":description,"createdAt":now()})
