# API REST

Base local: `http://localhost:8000`. JSON e erros `{ "detail": "mensagem" }`.

- `GET /`, `GET /health`
- Dashboard: `GET /api/dashboard/summary`, `/code-health`, `/activities`
- Projetos: `GET|POST /api/projects`, `GET|PUT|DELETE /api/projects/{id}`; listagem aceita `search` e `status`.
- Análises: `POST /api/analysis/chat/{projectId}`, `/game-design/{projectId}`, `/narrative/{projectId}`, `/level-design/{projectId}`, `/code`, `/project-structure`.
- Tarefas: `GET /api/tasks/project/{projectId}`, `POST /api/tasks`, `POST /api/tasks/generate/{projectId}`, `PUT /api/tasks/{id}`, `PATCH /api/tasks/{id}/status`, `DELETE /api/tasks/{id}`.
- QA: `GET /api/qa/project/{projectId}`, `POST /api/qa/generate/{projectId}`, `PATCH /api/qa/{id}`, `POST /api/qa/{id}/convert-to-task`.
- Relatórios: `GET /api/reports/project/{projectId}`, `POST /api/reports/generate/{projectId}`, `GET|DELETE /api/reports/{id}`.
- Atividades: `GET /api/activities`, `GET /api/activities/project/{projectId}`.

A especificação interativa e modelos completos ficam em `/docs` (Swagger) e `/redoc` com o backend ativo.
