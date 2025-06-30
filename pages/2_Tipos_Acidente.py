import streamlit as st
import plotly.express as px
from data.carregar_dados import carregar_dados

st.set_page_config(page_title="Tipos de Acidentes", layout="wide")


df = carregar_dados()

st.markdown("## Tipos de Acidentes na BR-163")
st.markdown("Explore abaixo os acidentes mais frequentes e suas características por quilômetro, vítimas envolvidas e tipos de veículos.")
top_10 = df['tipo_de_acidente'].value_counts().head(10).index
filtro = st.selectbox("Selecione um tipo de acidente:", top_10)
filtrado = df[df['tipo_de_acidente'] == filtro]

st.divider()

st.markdown(f"### Distribuição por Quilômetro - **{filtro.title()}**")
fig_km = px.histogram(
    filtrado, x='km', nbins=30,
    title=None,
    labels={'km': 'Quilômetro'},
    color_discrete_sequence=['steelblue'],
    hover_data=['data', 'horario']
)
fig_km.update_layout(margin=dict(t=10, b=30), height=350)
st.plotly_chart(fig_km, use_container_width=True)
st.markdown(f"**Total de ocorrências:** {len(filtrado)}")

st.divider()

st.markdown(f"### Distribuição de Vítimas - **{filtro.title()}**")
colunas_vitimas = ['ilesos', 'levemente_feridos', 'moderadamente_feridos', 'gravemente_feridos', 'mortos']
totais_vitimas = filtrado[colunas_vitimas].sum().sort_values(ascending=False)
fig_vitimas = px.bar(
    x=totais_vitimas.index,
    y=totais_vitimas.values,
    labels={'x': 'Condição da vítima', 'y': 'Quantidade'},
    color=totais_vitimas.values,
    color_continuous_scale='Reds'
)
fig_vitimas.update_layout(showlegend=False, height=350)
st.plotly_chart(fig_vitimas, use_container_width=True)

st.divider()

st.markdown(f"### Tipos de Veículos Envolvidos - **{filtro.title()}**")
colunas_veiculos = ['automovel', 'bicicleta', 'caminhao', 'moto', 'onibus', 'outros']
totais_veiculos = filtrado[colunas_veiculos].sum().sort_values(ascending=False)
fig_veiculos = px.bar(
    x=totais_veiculos.index,
    y=totais_veiculos.values,
    labels={'x': 'Tipo de veículo', 'y': 'Quantidade envolvida'},
    color=totais_veiculos.values,
    color_continuous_scale='Blues'
)
fig_veiculos.update_layout(showlegend=False, height=350)
st.plotly_chart(fig_veiculos, use_container_width=True)