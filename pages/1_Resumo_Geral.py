import streamlit as st
import pandas as pd
import plotly.express as px
import calendar
from data.carregar_dados import carregar_dados

st.set_page_config(page_title="Resumo Geral dos Acidentes", layout="wide")


df = carregar_dados()

st.title("Painel - Resumo Geral dos Acidentes")

st.markdown("Este painel apresenta um resumo dos acidentes ocorridos na BR-163, com base em dados entre 2022 e 2025. Explore a distribuição geográfica, por sentido da via e variação mensal.")

col1, col2 = st.columns(2)

with col1:
    fig_km = px.histogram(
        df, 
        x="km", 
        nbins=30, 
        title="Distribuição de Acidentes por Quilômetro",
        labels={"km": "Quilômetro"},
        color_discrete_sequence=["steelblue"]
    )
    fig_km.update_layout(margin=dict(t=40, b=20))
    st.plotly_chart(fig_km, use_container_width=True)

with col2:
    sentido_fig = px.pie(df, names='sentido', title="Distribuição por Sentido")
    st.plotly_chart(sentido_fig, use_container_width=True)

inicio = pd.Timestamp('2023-01-01')
fim = pd.Timestamp('2024-12-31')
df_filtrado_periodo = df[(df['data'] >= inicio) & (df['data'] <= fim)].copy()
acidentes_por_mes = df_filtrado_periodo.groupby(df_filtrado_periodo['data'].dt.month).size().reset_index(name='quantidade')
acidentes_por_mes['mes_nome'] = acidentes_por_mes['data'].apply(lambda x: calendar.month_abbr[x].capitalize())
acidentes_por_mes = acidentes_por_mes.sort_values('data')
fig_mes = px.bar(
    acidentes_por_mes,
    x='mes_nome',
    y='quantidade',
    labels={'mes_nome': 'Mês', 'quantidade': 'Quantidade de Acidentes'},
    title='Total de Acidentes por Mês (2023-2024)',
    color_discrete_sequence=['skyblue']
)

fig_mes.update_layout(
    xaxis_title='Mês',
    yaxis_title='Quantidade de Acidentes',
    margin=dict(t=50, b=40)
)

st.plotly_chart(fig_mes, use_container_width=True)

col3, col4 = st.columns(2)

with col3:
    col_veiculos = ['automovel', 'bicicleta', 'caminhao', 'moto', 'onibus', 'outros']
    totais_veiculos = df[col_veiculos].sum().sort_values(ascending=False)
    fig_veiculos = px.bar(
        x=totais_veiculos.index,
        y=totais_veiculos.values,
        title="Tipos de Veículos Envolvidos nos Acidentes",
        labels={"x": "Tipo de Veículo", "y": "Quantidade"},
        color_discrete_sequence=["darkorange"]
    )
    fig_veiculos.update_layout(xaxis_title="Veículo", yaxis_title="Total Envolvido")
    st.plotly_chart(fig_veiculos, use_container_width=True)

with col4:
    dados_feridos = df['teve_feridos'].value_counts().rename({True: 'Com Feridos', False: 'Sem Feridos'})
    fig_feridos = px.bar(
        x=dados_feridos.index,
        y=dados_feridos.values,
        title="Acidentes com e sem Feridos",
        labels={"x": "Tipo de Acidente", "y": "Quantidade"},
        color_discrete_sequence=["crimson"]
    )
    fig_feridos.update_layout(xaxis_title="", yaxis_title="Número de Acidentes")
    st.plotly_chart(fig_feridos, use_container_width=True)
