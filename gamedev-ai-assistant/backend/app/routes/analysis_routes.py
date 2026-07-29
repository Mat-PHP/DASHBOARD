from fastapi import APIRouter
from ..schemas.analysis_schema import ChatRequest,CodeRequest,StructureRequest,LevelRequest
from ..services import analysis_service as s
router=APIRouter(prefix="/analysis",tags=["Análises"])
@router.post("/chat/{project_id}")
async def chat(project_id:str,b:ChatRequest): return await s.chat(project_id,b)
@router.post("/game-design/{project_id}")
async def game(project_id:str,b:ChatRequest): b.module="Game Design"; return await s.chat(project_id,b)
@router.post("/narrative/{project_id}")
async def narrative(project_id:str,b:ChatRequest): b.module="Narrative Design"; return await s.chat(project_id,b)
@router.post("/level-design/{project_id}")
async def level(project_id:str,b:LevelRequest): return await s.chat(project_id,ChatRequest(module="Level Design",message=f"{b.type}: {b.objective}; dificuldade {b.difficulty}; ambiente {b.environment}; {b.enemies} inimigos e {b.puzzles} puzzles"))
@router.post("/code")
async def code(b:CodeRequest): return await s.code(b)
@router.post("/project-structure")
async def structure(b:StructureRequest): return await s.structure(b)
