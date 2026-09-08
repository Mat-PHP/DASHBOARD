from __future__ import annotations

from io import BytesIO
from typing import BinaryIO

import pandas as pd

REQUIRED_COLUMNS = {"data", "descricao", "categoria", "tipo", "valor"}
ALLOWED_TYPES = {"Receita", "Despesa"}


def load_transactions(source: BinaryIO | BytesIO) -> pd.DataFrame:
    """Load and validate a transaction CSV."""
    frame = pd.read_csv(source)
    frame.columns = [str(column).strip().lower() for column in frame.columns]

    missing = REQUIRED_COLUMNS - set(frame.columns)
    if missing:
        raise ValueError(f"O CSV não possui as colunas obrigatórias: {', '.join(sorted(missing))}.")

    result = frame[["data", "descricao", "categoria", "tipo", "valor"]].copy()
    result["data"] = pd.to_datetime(result["data"], errors="coerce")
    result["valor"] = pd.to_numeric(result["valor"], errors="coerce")
    result["tipo"] = result["tipo"].astype(str).str.strip().str.title()
    result["categoria"] = result["categoria"].astype(str).str.strip()
    result["descricao"] = result["descricao"].astype(str).str.strip()

    if result["data"].isna().any():
        raise ValueError("Há datas inválidas no CSV. Use o formato AAAA-MM-DD.")
    if result["valor"].isna().any() or (result["valor"] < 0).any():
        raise ValueError("Os valores devem ser números positivos.")
    invalid_types = set(result["tipo"]) - ALLOWED_TYPES
    if invalid_types:
        raise ValueError("A coluna tipo aceita somente Receita ou Despesa.")

    return result.sort_values("data").reset_index(drop=True)


def sample_transactions() -> pd.DataFrame:
    """Return deterministic sample data so the dashboard works on first run."""
    rows = [
        ("2026-01-05", "Salário", "Renda", "Receita", 6500.00),
        ("2026-01-08", "Aluguel", "Moradia", "Despesa", 1800.00),
        ("2026-01-12", "Supermercado", "Alimentação", "Despesa", 720.40),
        ("2026-01-18", "Transporte", "Mobilidade", "Despesa", 310.00),
        ("2026-02-05", "Salário", "Renda", "Receita", 6500.00),
        ("2026-02-08", "Aluguel", "Moradia", "Despesa", 1800.00),
        ("2026-02-13", "Supermercado", "Alimentação", "Despesa", 684.90),
        ("2026-02-20", "Cinema", "Lazer", "Despesa", 96.00),
        ("2026-03-05", "Salário", "Renda", "Receita", 6800.00),
        ("2026-03-08", "Aluguel", "Moradia", "Despesa", 1800.00),
        ("2026-03-15", "Supermercado", "Alimentação", "Despesa", 755.20),
        ("2026-03-22", "Academia", "Saúde", "Despesa", 129.90),
    ]
    frame = pd.DataFrame(rows, columns=["data", "descricao", "categoria", "tipo", "valor"])
    frame["data"] = pd.to_datetime(frame["data"])
    return frame

