# 💸 Finanças em Foco

Um dashboard financeiro pessoal, interativo e local-first. Importe suas transações em CSV, filtre por período e categoria e acompanhe receitas, despesas, saldo e tendências mensais.

## Destaques

- Interface web responsiva com Streamlit
- Upload e validação de CSV
- Indicadores de receitas, despesas, saldo e gasto médio
- Gráficos interativos por categoria e por mês
- Dados de demonstração determinísticos
- Testes automatizados, lint e integração contínua
- Processamento local: o aplicativo não envia seus dados a serviços externos

## Executar localmente

Requer Python 3.10 ou superior.

```bash
python -m venv .venv
```

Ative o ambiente virtual:

```bash
# Windows (PowerShell)
.venv\\Scripts\\Activate.ps1

# macOS/Linux
source .venv/bin/activate
```

Instale e execute:

```bash
pip install -e .
streamlit run app.py
```

O navegador abrirá em `http://localhost:8501`.

## Formato do CSV

O arquivo deve conter estas colunas:

| Coluna | Descrição | Exemplo |
|---|---|---|
| `data` | Data no formato AAAA-MM-DD | `2026-03-15` |
| `descricao` | Nome da movimentação | `Supermercado` |
| `categoria` | Categoria livre | `Alimentação` |
| `tipo` | `Receita` ou `Despesa` | `Despesa` |
| `valor` | Número positivo, sem símbolo monetário | `755.20` |

Você também pode baixar um modelo diretamente pela barra lateral do aplicativo.

## Qualidade

```bash
pip install -e ".[dev]"
ruff check .
pytest
```

O GitHub Actions executa essas verificações em cada push e pull request.

## Estrutura

```text
.
├── app.py                         # Interface Streamlit
├── finance_dashboard/
│   ├── analytics.py               # Métricas e agregações
│   └── data.py                    # Leitura, validação e dados de exemplo
├── tests/                         # Testes unitários
└── .github/workflows/ci.yml       # Integração contínua
```

## Privacidade

As transações ficam na memória do processo local durante o uso. Não inclua arquivos financeiros pessoais no repositório e confira sempre o conteúdo antes de compartilhar capturas de tela.

## Próximos passos

- Orçamentos mensais por categoria
- Persistência local opcional
- Importadores específicos para extratos bancários
- Comparação entre períodos

