from pydantic import BaseModel,Field,field_validator
CATEGORIES={"bug","feature","melhoria","QA","performance","arte","narrativa","áudio","level design","documentação"}; PRIORITIES={"baixa","média","alta","crítica"}; STATUSES={"backlog","pendente","em andamento","revisão","concluída"}
class TaskCreate(BaseModel):
 projectId:str; title:str=Field(min_length=2,max_length=150); description:str=""; category:str="feature"; priority:str="média"; status:str="backlog"; assignedTo:str=""; estimatedHours:float=Field(1,ge=0)
 @field_validator("category")
 @classmethod
 def cat(cls,v):
  if v not in CATEGORIES: raise ValueError("Categoria inválida")
  return v
 @field_validator("priority")
 @classmethod
 def pri(cls,v):
  if v not in PRIORITIES: raise ValueError("Prioridade inválida")
  return v
 @field_validator("status")
 @classmethod
 def sta(cls,v):
  if v not in STATUSES: raise ValueError("Status inválido")
  return v
class TaskUpdate(TaskCreate): pass
class StatusUpdate(BaseModel): status:str
