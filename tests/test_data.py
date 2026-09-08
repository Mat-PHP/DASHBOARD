from io import BytesIO

import pytest

from finance_dashboard.data import load_transactions, sample_transactions


def test_sample_data_is_valid() -> None:
    result = sample_transactions()

    assert not result.empty
    assert set(result["tipo"]) == {"Receita", "Despesa"}


def test_rejects_missing_columns() -> None:
    source = BytesIO(b"data,valor\n2026-01-01,10")

    with pytest.raises(ValueError, match="colunas obrigatórias"):
        load_transactions(source)


def test_rejects_negative_values() -> None:
    source = BytesIO(
        b"data,descricao,categoria,tipo,valor\n2026-01-01,Teste,Geral,Despesa,-10"
    )

    with pytest.raises(ValueError, match="valores devem ser números positivos"):
        load_transactions(source)

