from fastapi import APIRouter
from ..database import db
from ..utils.object_id import oid,serialize
router=APIRouter(prefix="/activities",tags=["Atividades"])
@router.get("")
async def listing(limit:int=30): return serialize(await db.activities.find().sort("createdAt",-1).limit(min(limit,100)).to_list(100))
@router.get("/project/{project_id}")
async def project(project_id:str): return serialize(await db.activities.find({"projectId":oid(project_id)}).sort("createdAt",-1).to_list(100))
