from __future__ import annotations

from datetime import date

import plotly.express as px
import streamlit as st

from finance_dashboard.analytics import calculate_summary, monthly_totals
from finance_dashboard.data import load_transactions, sample_transactions

st.set_page_config(page_title="Finanças em Foco", page_icon="💸", layout="wide")

st.title("💸 Finanças em Foco")
st.caption("Entenda para onde seu dinheiro vai — sem enviar seus dados para nenhum servidor.")

with st.sidebar:
    st.header("Seus dados")
    uploaded_file = st.file_uploader("Importe um CSV", type="csv")
    st.download_button(
        "Baixar modelo CSV",
        sample_transactions().to_csv(index=False).encode("utf-8"),
        file_name="transacoes_exemplo.csv",
        mime="text/csv",
    )

try:
    transactions = load_transactions(uploaded_file) if uploaded_file else sample_transactions()
except ValueError as exc:
    st.error(str(exc))
    st.stop()

min_date = transactions["data"].min().date()
max_date = transactions["data"].max().date()

with st.sidebar:
    selected_period = st.date_input(
        "Período",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date,
    )
    categories = sorted(transactions["categoria"].unique())
    selected_categories = st.multiselect("Categorias", categories, default=categories)

if isinstance(selected_period, tuple) and len(selected_period) == 2:
    start_date, end_date = selected_period
else:
    start_date = end_date = selected_period if isinstance(selected_period, date) else min_date

filtered = transactions[
    transactions["data"].dt.date.between(start_date, end_date)
    & transactions["categoria"].isin(selected_categories)
]

if filtered.empty:
    st.info("Nenhuma transação encontrada para os filtros selecionados.")
    st.stop()

summary = calculate_summary(filtered)
income_col, expense_col, balance_col, average_col = st.columns(4)
income_col.metric("Receitas", f"R$ {summary.income:,.2f}")
expense_col.metric("Despesas", f"R$ {summary.expenses:,.2f}")
balance_col.metric("Saldo", f"R$ {summary.balance:,.2f}")
average_col.metric("Gasto médio", f"R$ {summary.average_expense:,.2f}")

chart_col, trend_col = st.columns(2)
expenses = filtered[filtered["tipo"] == "Despesa"]

with chart_col:
    st.subheader("Despesas por categoria")
    by_category = expenses.groupby("categoria", as_index=False)["valor"].sum()
    st.plotly_chart(
        px.pie(by_category, names="categoria", values="valor", hole=0.55),
        use_container_width=True,
    )

with trend_col:
    st.subheader("Evolução mensal")
    trend = monthly_totals(filtered)
    st.plotly_chart(
        px.bar(trend, x="mes", y="valor", color="tipo", barmode="group"),
        use_container_width=True,
    )

st.subheader("Transações")
st.dataframe(
    filtered.sort_values("data", ascending=False),
    use_container_width=True,
    hide_index=True,
    column_config={
        "data": st.column_config.DateColumn("Data", format="DD/MM/YYYY"),
        "valor": st.column_config.NumberColumn("Valor", format="R$ %.2f"),
    },
)

