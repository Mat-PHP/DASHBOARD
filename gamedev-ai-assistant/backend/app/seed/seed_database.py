import asyncio
from datetime import datetime,timezone,timedelta
from app.database import db,create_indexes
PROJECTS=[
{"name":"Eldoria Chronicles","description":"RPG medieval de mundo aberto onde alianças alteram reinos e missões.","genre":"RPG medieval","engine":"Godot","platform":"PC","targetAudience":"Fãs de RPG","visualStyle":"Fantasia pintada à mão","references":["RPGs clássicos"],"status":"em desenvolvimento","overallScore":82,"progress":68,"taskCount":34,"bugCount":6,"assetCount":824,"teamSize":5,"multiplayer":False,"imageUrl":""},
{"name":"Cyber Quest","description":"RPG de ação sci-fi sobre memória, tecnologia e facções rivais.","genre":"RPG de ação e ficção científica","engine":"Unity","platform":"PC e console","targetAudience":"Jogadores de ação","visualStyle":"Neon retrofuturista","references":["Cyberpunk"],"status":"testes","overallScore":86,"progress":75,"taskCount":48,"bugCount":7,"assetCount":1248,"teamSize":5,"multiplayer":True,"imageUrl":""},
{"name":"Echoes of the Manor","description":"Mistério point and click em uma mansão que reage às escolhas do jogador.","genre":"point and click investigativo","engine":"Godot","platform":"PC e web","targetAudience":"Fãs de mistério","visualStyle":"Gótico estilizado","references":["Noir"],"status":"protótipo","overallScore":76,"progress":44,"taskCount":21,"bugCount":3,"assetCount":412,"teamSize":3,"multiplayer":False,"imageUrl":""}]
async def seed():
 await create_indexes(); now=datetime.now(timezone.utc)
 for i,p in enumerate(PROJECTS):
  p={**p,"createdAt":now-timedelta(days=30-i*4),"updatedAt":now-timedelta(days=i)}; await db.projects.update_one({"name":p["name"]},{"$set":p},upsert=True); project=await db.projects.find_one({"name":p["name"]}); pid=project["_id"]
  samples=[("Corrigir colisão do jogador","bug","crítica"),("Implementar missão introdutória","feature","alta"),("Otimizar partículas","performance","média"),("Validar HUD","QA","média")]
  for j,(title,cat,pri) in enumerate(samples): await db.tasks.update_one({"projectId":pid,"seedKey":f"task-{j}"},{"$set":{"projectId":pid,"seedKey":f"task-{j}","title":title,"description":"Item inicial para planejamento","category":cat,"priority":pri,"status":["backlog","em andamento","revisão","concluída"][j],"assignedTo":"PixelNinja","estimatedHours":j+2,"createdAt":now-timedelta(days=j),"updatedAt":now}},upsert=True)
  await db.activities.update_one({"projectId":pid,"seedKey":"initial"},{"$set":{"projectId":pid,"seedKey":"initial","type":"project_created","description":f"Projeto {p['name']} adicionado ao portfólio","createdAt":now-timedelta(hours=i+1)}},upsert=True)
  await db.analyses.update_one({"projectId":pid,"seedKey":"review"},{"$set":{"projectId":pid,"seedKey":"review","type":"game-design","result":{"score":p["overallScore"]},"createdAt":now}},upsert=True)
  await db.reports.update_one({"projectId":pid,"seedKey":"report"},{"$set":{"projectId":pid,"seedKey":"report","overallScore":p["overallScore"],"scores":{"gameplay":84,"code":78,"performance":75,"narrative":86,"art":88,"audio":76,"levelDesign":81,"technicalQuality":79},"strengths":["Direção clara"],"weaknesses":["Testes limitados"],"risks":["Escopo"],"recommendations":["Playtests semanais"],"nextSteps":["Concluir vertical slice"],"createdAt":now}},upsert=True)
  qa={"projectId":pid,"seedKey":"movement","title":"Movimentação","description":"Validar controles e resposta","category":"movimentação","priority":"alta","status":"pendente","expectedResult":"Movimento responsivo","notes":"","createdAt":now}; await db.qa_tests.update_one({"projectId":pid,"seedKey":"movement"},{"$set":qa},upsert=True)
 print("Seed concluído de forma idempotente: 3 projetos e dados relacionados.")
if __name__=="__main__": asyncio.run(seed())
