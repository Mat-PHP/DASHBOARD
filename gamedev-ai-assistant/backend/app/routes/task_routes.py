from fastapi import APIRouter
from ..schemas.task_schema import TaskCreate,TaskUpdate,StatusUpdate
from ..services import task_service as s
from ..database import db
from ..utils.object_id import oid
router=APIRouter(prefix="/tasks",tags=["Tarefas"])
@router.get("/project/{project_id}")
async def listing(project_id:str): return await s.list_tasks(project_id)
@router.post("",status_code=201)
async def create(b:TaskCreate): return await s.create(b.model_dump())
@router.post("/generate/{project_id}")
async def generate(project_id:str): return await s.generate(project_id)
@router.put("/{task_id}")
async def update(task_id:str,b:TaskUpdate): return await s.update(task_id,b.model_dump())
@router.patch("/{task_id}/status")
async def status(task_id:str,b:StatusUpdate): return await s.status(task_id,b.status)
@router.delete("/{task_id}")
async def delete(task_id:str): await db.tasks.delete_one({"_id":oid(task_id)}); return {"deleted":True}
