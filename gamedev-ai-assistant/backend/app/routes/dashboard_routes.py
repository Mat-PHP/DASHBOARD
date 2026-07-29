from fastapi import APIRouter
from ..database import db
from ..utils.object_id import serialize
router=APIRouter(prefix="/dashboard",tags=["Dashboard"])
@router.get("/summary")
async def summary():
 projects=await db.projects.find().sort("updatedAt",-1).to_list(20); tasks=await db.tasks.count_documents({}); bugs=await db.tasks.count_documents({"category":"bug"}); scores=[p.get("overallScore",0) for p in projects]
 return serialize({"totalProjects":len(projects),"activeProjects":sum(p.get("status") not in ("pausado","concluído") for p in projects),"averageScore":round(sum(scores)/len(scores)) if scores else 0,"taskCount":tasks,"bugCount":bugs,"recentProjects":projects[:5],"performance":[{"name":p["name"],"score":p.get("overallScore",0),"progress":p.get("progress",0)} for p in projects],"taskCategories":[{"name":x,"value":await db.tasks.count_documents({"category":x})} for x in ("bug","feature","QA","arte","performance")]})
@router.get("/code-health")
async def health(): return {"score":82,"complexity":74,"performance":85,"maintainability":88,"security":79}
@router.get("/activities")
async def activities(): return serialize(await db.activities.find().sort("createdAt",-1).limit(8).to_list(8))
