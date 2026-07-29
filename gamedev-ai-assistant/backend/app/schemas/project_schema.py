from datetime import datetime, timezone
from pydantic import BaseModel, Field, field_validator
from typing import Optional
ENGINES={"Godot","Unity","Unreal Engine","GameMaker","Construct","Custom Engine","Outra"}
STATUSES={"planejamento","protótipo","em desenvolvimento","testes","pausado","concluído"}
class ProjectCreate(BaseModel):
    name:str=Field(min_length=2,max_length=100); description:str=Field(min_length=10,max_length=2000); genre:str=Field(min_length=2); engine:str; platform:str=Field(min_length=2); targetAudience:str="Geral"; visualStyle:str=""; references:list[str]=[]; status:str="planejamento"; overallScore:int=Field(70,ge=0,le=100); progress:int=Field(0,ge=0,le=100); taskCount:int=Field(0,ge=0); bugCount:int=Field(0,ge=0); assetCount:int=Field(0,ge=0); teamSize:int=Field(1,ge=1); multiplayer:bool=False; imageUrl:str=""
    @field_validator("engine")
    @classmethod
    def engine_ok(cls,v):
        if v not in ENGINES: raise ValueError("Engine inválida")
        return v
    @field_validator("status")
    @classmethod
    def status_ok(cls,v):
        if v not in STATUSES: raise ValueError("Status inválido")
        return v
class ProjectUpdate(ProjectCreate): pass
