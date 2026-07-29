# Banco de dados

Banco padrão: `gamedev_ai`. Coleções: `projects`, `tasks`, `reports`, `analyses`, `qa_tests`, `activities`, `saved_responses`.

Relacionamentos usam `projectId` como `ObjectId`. Respostas convertem todo ObjectId em string. Índices são criados na inicialização para `projectId`, `createdAt`, `status`, `category` e `priority`; `projects.name` é único. Datas são UTC. O seed utiliza `name` e `seedKey` em operações de upsert, garantindo idempotência.

Backup local: `mongodump --db gamedev_ai --out backup`. Restauração: `mongorestore --db gamedev_ai backup/gamedev_ai`.
