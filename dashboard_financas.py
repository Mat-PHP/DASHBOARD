import random
import pandas as pd
import matplotlib.pyplot as plt

# Gerar dados financeiros aleatórios
categorias = ["Aluguel", "Transporte", "Alimentação", "Lazer", "Compras", "Saúde", "Investimentos"]
gastos = [random.randint(200, 3000) for _ in categorias]

# Criar tabela (DataFrame)
df = pd.DataFrame({
    "Categoria": categorias,
    "Gasto (R$)": gastos
})

print("\n===== DASHBOARD FINANCEIRO =====\n")
print(df)
print("\nTotal gasto no mês: R$", df["Gasto (R$)"].sum())

# Criar gráfico
plt.figure(figsize=(8, 5))
plt.bar(df["Categoria"], df["Gasto (R$)"])
plt.title("Gastos Mensais por Categoria")
plt.xlabel("Categoria")
plt.ylabel("Valor (R$)")
plt.tight_layout()

plt.show()
