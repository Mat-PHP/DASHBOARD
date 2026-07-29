# GDA — GameDev AI Assistant

Plataforma full stack para planejar, analisar e acompanhar jogos. A interface gamer responsiva concentra projetos, tarefas Kanban, QA, relatórios, análise de código/estrutura, level design e um assistente local contextual — sem depender de APIs externas.

## Funcionalidades
- Dashboard com métricas MongoDB, gráficos, progresso, atividades e saúde de código.
- CRUD validado de projetos; seleção persistente do projeto ativo.
- Assistente com 10 especialidades, histórico, copiar/salvar/avaliar e ações rápidas.
- Analisadores heurísticos de código e estrutura; gerador de level design.
- Kanban com drag-and-drop, geração de tarefas e atualização persistente.
- Checklist QA que converte falhas em tarefas e relatórios históricos.
- Estados de carregamento/erro/vazio, confirmação, toasts e layout mobile.

## Tecnologias e arquitetura
React + Vite, React Router, Axios, Lucide e Recharts compõem o frontend. FastAPI, Pydantic e Motor formam uma API assíncrona organizada em schemas, models, services e routes. MongoDB armazena os documentos. Consulte [arquitetura](docs/architecture.md), [API](docs/api.md) e [banco](docs/database.md).

## Requisitos
Python 3.11+, Node.js 20+, npm e MongoDB 7+ (local/Atlas), ou Docker Compose.

## Execução com Docker
```bash
cd gamedev-ai-assistant
docker compose up
```
O seed roda automaticamente. Abra `http://localhost:5173`; API em `http://localhost:8000`; Swagger em `http://localhost:8000/docs`.

## Execução sem Docker
### MongoDB
Instale o MongoDB Community, inicie o serviço na porta 27017 e confirme com `mongosh --eval "db.runCommand({ping:1})"`. Para Atlas, use a connection string em `MONGODB_URL`.

### Backend
```bash
cd gamedev-ai-assistant/backend
python -m venv venv
# Windows: venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python -m app.seed.seed_database
uvicorn app.main:app --reload
```

### Frontend
```bash
cd gamedev-ai-assistant/frontend
cp .env.example .env
npm install
npm run dev
```

## Variáveis
Backend: `MONGODB_URL`, `MONGODB_DATABASE` (padrão `gamedev_ai`), `FRONTEND_URL`, `AI_PROVIDER`, `OLLAMA_URL`, `OLLAMA_MODEL`. Frontend: `VITE_API_URL`. O MVP suporta `AI_PROVIDER=mock`; a abstração do serviço permite incluir Ollama/OpenAI depois.

## Seed
`python -m app.seed.seed_database` faz upsert por chaves estáveis: pode ser repetido sem duplicar projetos e conteúdo inicial.

## Requisições
```bash
curl http://localhost:8000/health
curl http://localhost:8000/api/projects
curl -X POST http://localhost:8000/api/analysis/chat/ID -H 'Content-Type: application/json' -d '{"module":"Game Design","message":"Como melhorar a progressão?"}'
```

## Solução de problemas
- **503 no health:** confirme serviço/URL do MongoDB e allowlist do Atlas.
- **API indisponível no frontend:** confira `VITE_API_URL`, backend na porta 8000 e CORS `FRONTEND_URL`.
- **Dashboard vazio:** execute o seed no diretório `backend`.
- **Porta ocupada:** encerre o processo ou altere o mapeamento do Compose/Vite.

## Melhorias futuras
Autenticação, colaboração em tempo real, upload de builds/assets, execução segura de linters, provedores Ollama/OpenAI, testes E2E e telemetria de playtests.
