from fastapi import APIRouter,Query
from ..schemas.project_schema import ProjectCreate,ProjectUpdate
from ..services import project_service as s
router=APIRouter(prefix="/projects",tags=["Projetos"])
@router.get("")
async def listing(search:str="",status:str|None=None): return await s.list_projects(search,status)
@router.post("",status_code=201)
async def create(body:ProjectCreate): return await s.create_project(body.model_dump())
@router.get("/{project_id}")
async def get(project_id:str): return await s.get_project(project_id)
@router.put("/{project_id}")
async def update(project_id:str,body:ProjectUpdate): return await s.update_project(project_id,body.model_dump())
@router.delete("/{project_id}")
async def delete(project_id:str): return await s.delete_project(project_id)
