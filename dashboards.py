import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

df = pd.read_csv("vendas_mercadinho.csv", sep=";", decimal=",")
df["Data"] = pd.to_datetime(df["Data"])
df = df.sort_values("Data")

df["Month"] = df["Data"].apply(lambda x: str(x.year) + "-" + str(x.month))
month = st.sidebar.selectbox("Mês", df["Month"].unique())

df_filtered = df[df["Month"] == month]

cidade_total = df_filtered.groupby("Cidade")["Total"].sum().reset_index()


col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

fig_data = px.bar(df_filtered, x="Data", y="Total", color="Cidade", title="Quantia de Faturamento por Dia")
col1.plotly_chart(fig_data, use_container_width=True)

fig_prod = px.bar(df_filtered, x="Data", y="Categoria de Produto", color="Categoria de Produto", title="Quantia de Faturamento por Produto", orientation="h")
col2.plotly_chart(fig_prod, use_container_width=True)

fig_cidade = px.bar(cidade_total, x="Cidade", y="Total", title="Quantia de Faturamento por Cidade")
col3.plotly_chart(fig_cidade, use_container_width=True)

fig_pagamento = px.bar(df_filtered, x="Data", y="Método de Pagamento", color="Método de Pagamento", title="Quantia de Faturamento por Forma de Pagamento")
col4.plotly_chart(fig_pagamento, use_container_width=True)

fig_sexo = px.bar(df_filtered, x="Data", y="Sexo", color="Sexo", title="Quantia de Compras por Sexo")
col5.plotly_chart(fig_sexo, use_container_width=True)

