from datetime import datetime,timezone
from fastapi import HTTPException
from ..database import db
from ..utils.object_id import oid,serialize
from .project_service import get_project,log
async def generate(pid):
 p=await get_project(pid); base=p.get("overallScore",70); scores={"gameplay":min(100,base+3),"code":base-2,"performance":base-5,"narrative":base+1,"art":base+5,"audio":base-1,"levelDesign":base,"technicalQuality":base-3}; doc={"projectId":oid(pid),"overallScore":round(sum(scores.values())/len(scores)),"scores":scores,"strengths":["Identidade visual consistente","Escopo mensurável"],"weaknesses":["Cobertura de testes limitada"],"risks":["Crescimento de escopo"],"recommendations":["Validar vertical slice","Automatizar testes"],"nextSteps":["Priorizar bugs críticos","Realizar playtest"],"createdAt":datetime.now(timezone.utc)}; r=await db.reports.insert_one(doc); await log(oid(pid),"report_generated","Relatório gerado"); return serialize({**doc,"_id":r.inserted_id})
async def list_reports(pid): return serialize(await db.reports.find({"projectId":oid(pid)}).sort("createdAt",-1).to_list(100))
async def get(rid):
 d=await db.reports.find_one({"_id":oid(rid)});
 if not d: raise HTTPException(404,"Relatório não encontrado")
 return serialize(d)
