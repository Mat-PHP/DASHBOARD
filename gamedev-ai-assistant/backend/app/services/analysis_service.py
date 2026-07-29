import re
from datetime import datetime,timezone
from ..database import db
from ..utils.object_id import oid,serialize
from .project_service import get_project,log
from .mock_ai_service import answer
async def chat(pid,payload):
 p=await get_project(pid); content=answer(p,payload.module,payload.message); doc={"projectId":oid(pid),"type":"chat","module":payload.module,"input":payload.message,"result":content,"createdAt":datetime.now(timezone.utc)}; r=await db.analyses.insert_one(doc); await log(oid(pid),"analysis_completed",f"Análise {payload.module} realizada"); return {"_id":str(r.inserted_id),"response":content}
async def code(payload):
 c=payload.code; issues=[]
 checks=[(r"TODO","Comentário TODO pendente"),(r"print\(|console\.log","Saída de depuração encontrada"),(r"\b(if|elif|else if)\b","Condicionais elevam a complexidade"),(r"\b(for|while)\b","Revise loops em caminhos por frame"),(r"\b(x|tmp|data)\s*=","Nome de variável genérico"),(r"\b(null|None)\b","Proteja acessos contra valor nulo")]
 for pat,msg in checks:
  n=len(re.findall(pat,c,re.I));
  if n: issues.append({"type":msg,"occurrences":n,"severity":"alta" if n>4 else "média"})
 lines=c.splitlines(); score=max(20,100-len(issues)*8-max(0,len(lines)-80)//5); result={"score":score,"complexity":"alta" if score<60 else "moderada" if score<80 else "baixa","issues":issues,"suggestions":["Extraia funções pequenas e nomeadas","Valide referências antes do uso","Remova logs da versão de produção"],"refactoredCode":c.replace("console.log", "// log removido: console.log").replace("print(","# log removido: print(")}
 await db.analyses.insert_one({"projectId":oid(payload.projectId) if payload.projectId else None,"type":"code","result":result,"createdAt":datetime.now(timezone.utc)}); return result
async def structure(payload):
 s=payload.structure.lower(); missing=[x for x in ("scripts","assets","audio","scenes","data","tests") if x not in s]; risks=[]
 if any(x in s for x in (".tmp","temp/","backup")): risks.append("Arquivos temporários ou backups no projeto")
 return {"score":max(35,95-len(missing)*8-len(risks)*10),"missingFolders":missing,"risks":risks,"suggestedStructure":["assets/art","assets/audio","src/core","src/gameplay","scenes","data","tests"],"engine":payload.engine}
