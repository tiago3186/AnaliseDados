import pandas as pd
import matplotlib.pyplot as plt

# Lendo a planilha de dados
caminho_planilha = "caminho/para/a/sua_planilha.xlsx"  # Coloque o caminho correto do arquivo
df = pd.read_excel(caminho_planilha)

# Tratamento de dados
df = df.dropna()  # Remover linhas com valores ausentes

# Análise dos dados
df["Total Vendas"] = df["Preço"] * df["Quantidade Vendida"]
media_preco_por_produto = df.groupby("Produto")["Preço"].mean()
produtos_mais_vendidos = df.nlargest(5, "Quantidade Vendida")

# Visualização dos dados
plt.figure(figsize=(12, 6))

# Gráfico de barras para total de vendas por produto
plt.subplot(1, 2, 1)
plt.bar(df["Produto"], df["Total Vendas"])
plt.xlabel("Produto")
plt.ylabel("Total de Vendas")
plt.title("Total de Vendas por Produto")
plt.xticks(rotation=45)

# Gráfico de pizza para proporção de vendas por produto
plt.subplot(1, 2, 2)
plt.pie(df["Total Vendas"], labels=df["Produto"], autopct="%1.1f%%")
plt.title("Proporção de Vendas por Produto")

plt.tight_layout()
plt.show()

# Exibindo resumo estatístico
print("Resumo Estatístico:\n")
print("Média de preço por produto:")
print(media_preco_por_produto)
print("\nProdutos mais vendidos:")
print(produtos_mais_vendidos[["Produto", "Quantidade Vendida"]])
