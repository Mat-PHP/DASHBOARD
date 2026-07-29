import hashlib,random
MODULES={
"Game Design":["crie um loop de risco e recompensa","teste progressão em três camadas","use recompensas que alterem decisões"],
"Narrative Design":["conecte o conflito central às missões","dê objetivos contraditórios aos NPCs","revele o lore pelo ambiente"],
"Level Design":["altere espaços de tensão e descanso","posicione segredos em linhas visuais","valide rotas alternativas"],
"Code Analysis":["separe responsabilidades","meça gargalos antes de otimizar","automatize testes críticos"],
"Art Direction":["defina silhuetas reconhecíveis","limite a paleta por bioma","documente uma linguagem visual"],
"Audio Design":["use camadas dinâmicas","reserve frequências para feedback","varie sons repetitivos"],
"Marketing Advisor":["comunique um diferencial claro","registre material desde o protótipo","teste a página com jogadores"],
"QA Tester":["priorize caminhos críticos","registre passos reproduzíveis","teste limites e estados inválidos"],
"Performance Advisor":["estabeleça orçamento por frame","use pooling nos objetos recorrentes","meça em hardware alvo"],
"Task Generator":["quebre entregas em até oito horas","inclua critério de aceite","explicite dependências"]}
def answer(project,module,message):
 options=MODULES.get(module,MODULES["Game Design"]); rng=random.Random(hashlib.sha256((message+project['name']).encode()).hexdigest()); picks=rng.sample(options,len(options));
 return f"### Direção para {project['name']}\nConsiderando **{project['genre']}**, {project['engine']} em {project['platform']} e o estilo {project.get('visualStyle') or 'definido pelo projeto'}, recomendo:\n\n"+"\n".join(f"{i+1}. {x.capitalize()}." for i,x in enumerate(picks))+f"\n\n**Próximo experimento:** crie um protótipo focado em “{message[:120]}” e valide com 5 jogadores. Registre tempo, abandono e clareza."
