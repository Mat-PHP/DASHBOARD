from pydantic import BaseModel,Field
class ChatRequest(BaseModel): module:str=Field(min_length=2); message:str=Field(min_length=2,max_length=5000)
class CodeRequest(BaseModel): projectId:str|None=None; engine:str=""; language:str; filename:str="codigo"; code:str=Field(min_length=1)
class StructureRequest(BaseModel): projectId:str|None=None; engine:str; structure:str=Field(min_length=3)
class LevelRequest(BaseModel): objective:str; type:str="dungeon"; difficulty:str="média"; duration:int=20; environment:str=""; enemies:int=5; puzzles:int=2
