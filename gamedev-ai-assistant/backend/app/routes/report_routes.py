from fastapi import APIRouter
from ..services import report_service as s
from ..database import db
from ..utils.object_id import oid
router=APIRouter(prefix="/reports",tags=["Relatórios"])
@router.get("/project/{project_id}")
async def listing(project_id:str): return await s.list_reports(project_id)
@router.post("/generate/{project_id}")
async def generate(project_id:str): return await s.generate(project_id)
@router.get("/{report_id}")
async def get(report_id:str): return await s.get(report_id)
@router.delete("/{report_id}")
async def delete(report_id:str): await db.reports.delete_one({"_id":oid(report_id)}); return {"deleted":True}
