from datetime import datetime,timezone
from ..database import db
from ..utils.object_id import oid,serialize
from .project_service import log
from .task_service import create
ITEMS=["Colisões","Movimentação","Câmera","Save game","Carregamento","FPS","Inimigos","Bosses","Missões","Inventário","Menus","HUD","Áudio","Controles","Resolução","Multiplayer","Acessibilidade"]
async def list_tests(pid): return serialize(await db.qa_tests.find({"projectId":oid(pid)}).to_list(200))
async def generate(pid):
 if await db.qa_tests.count_documents({"projectId":oid(pid)}): return await list_tests(pid)
 now=datetime.now(timezone.utc); docs=[{"projectId":oid(pid),"title":x,"description":f"Validar {x.lower()} em condições normais e limites","category":x,"priority":"alta" if x in ("Save game","FPS","Colisões") else "média","status":"pendente","expectedResult":"Funciona sem erros e com feedback claro","notes":"","createdAt":now} for x in ITEMS]; await db.qa_tests.insert_many(docs); await log(oid(pid),"checklist_created","Checklist QA criado"); return await list_tests(pid)
async def patch(qid,data): await db.qa_tests.update_one({"_id":oid(qid)},{"$set":data}); return serialize(await db.qa_tests.find_one({"_id":oid(qid)}))
async def convert(qid):
 q=await db.qa_tests.find_one({"_id":oid(qid)}); return await create({"projectId":str(q["projectId"]),"title":f"Corrigir falha: {q['title']}","description":q.get("notes") or q["description"],"category":"bug","priority":q["priority"],"status":"backlog","assignedTo":"","estimatedHours":2})
