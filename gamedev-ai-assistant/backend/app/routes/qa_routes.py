from fastapi import APIRouter
from pydantic import BaseModel
from ..services import qa_service as s
class Patch(BaseModel): status:str|None=None; notes:str|None=None
router=APIRouter(prefix="/qa",tags=["QA"])
@router.get("/project/{project_id}")
async def listing(project_id:str): return await s.list_tests(project_id)
@router.post("/generate/{project_id}")
async def generate(project_id:str): return await s.generate(project_id)
@router.patch("/{test_id}")
async def patch(test_id:str,b:Patch): return await s.patch(test_id,b.model_dump(exclude_none=True))
@router.post("/{test_id}/convert-to-task")
async def convert(test_id:str): return await s.convert(test_id)
