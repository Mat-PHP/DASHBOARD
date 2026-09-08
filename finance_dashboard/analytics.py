from __future__ import annotations

from dataclasses import dataclass

import pandas as pd


@dataclass(frozen=True)
class FinancialSummary:
    income: float
    expenses: float
    balance: float
    average_expense: float


def calculate_summary(transactions: pd.DataFrame) -> FinancialSummary:
    income = float(transactions.loc[transactions["tipo"] == "Receita", "valor"].sum())
    expense_values = transactions.loc[transactions["tipo"] == "Despesa", "valor"]
    expenses = float(expense_values.sum())
    return FinancialSummary(
        income=income,
        expenses=expenses,
        balance=income - expenses,
        average_expense=float(expense_values.mean()) if not expense_values.empty else 0.0,
    )


def monthly_totals(transactions: pd.DataFrame) -> pd.DataFrame:
    result = transactions.copy()
    result["mes"] = result["data"].dt.to_period("M").astype(str)
    return result.groupby(["mes", "tipo"], as_index=False)["valor"].sum()

