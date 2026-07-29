# Arquitetura

O navegador renderiza uma SPA React. Contextos mantêm projeto ativo e notificações; services Axios isolam HTTP. Páginas combinam componentes reutilizáveis e todas as operações persistentes usam a API.

A API FastAPI segue o fluxo **route → schema Pydantic → service → Motor → MongoDB**. Routes cuidam de HTTP, services aplicam regras e atividades automáticas, schemas validam entrada e `utils/object_id.py` converte BSON com segurança. O serviço mock gera respostas determinísticas-varáveis a partir do projeto e da pergunta; sua fronteira é o ponto de extensão para provedores reais.

No Compose, os três serviços compartilham rede interna; apenas MongoDB possui volume persistente. CORS aceita a origem configurada por ambiente.
