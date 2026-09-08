import pandas as pd

from finance_dashboard.analytics import calculate_summary, monthly_totals


def test_calculate_summary() -> None:
    transactions = pd.DataFrame(
        {
            "data": pd.to_datetime(["2026-01-01", "2026-01-02", "2026-01-03"]),
            "tipo": ["Receita", "Despesa", "Despesa"],
            "valor": [1000.0, 200.0, 300.0],
        }
    )

    summary = calculate_summary(transactions)

    assert summary.income == 1000.0
    assert summary.expenses == 500.0
    assert summary.balance == 500.0
    assert summary.average_expense == 250.0


def test_monthly_totals_groups_by_type() -> None:
    transactions = pd.DataFrame(
        {
            "data": pd.to_datetime(["2026-01-01", "2026-01-02", "2026-02-01"]),
            "tipo": ["Receita", "Despesa", "Receita"],
            "valor": [1000.0, 400.0, 1200.0],
        }
    )

    result = monthly_totals(transactions)

    assert len(result) == 3
    assert result["valor"].sum() == 2600.0

