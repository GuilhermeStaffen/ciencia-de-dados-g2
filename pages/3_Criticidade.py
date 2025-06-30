import streamlit as st
import pandas as pd
import plotly.express as px
from data.carregar_dados import carregar_dados

st.set_page_config(page_title="Criticidade dos Acidentes", layout="wide")

df = carregar_dados()

st.title("Análise de Criticidade dos Acidentes")

st.sidebar.header("Filtros")
data_min = df['data'].min()
data_max = df['data'].max()

intervalo = st.sidebar.date_input(
    "Selecione o intervalo de datas:",
    value=[],
    min_value=data_min,
    max_value=data_max
)

if len(intervalo) == 2:
    data_inicio, data_fim = intervalo
    df_filtrado = df[(df['data'] >= pd.to_datetime(data_inicio)) & (df['data'] <= pd.to_datetime(data_fim))]
else:
    df_filtrado = df

top = df_filtrado.groupby('tipo_de_acidente')['criticidade'].sum().sort_values(ascending=False).head(10)
top_df = top.reset_index().rename(columns={'criticidade': 'total_criticidade'})

fig_top = px.bar(
    top_df.sort_values('total_criticidade'),
    x='total_criticidade',
    y='tipo_de_acidente',
    orientation='h',
    title="Top 10 Tipos de Acidente com Maior Número Total de Feridos e Mortos",
    labels={'total_criticidade': 'Total de Feridos/Mortos', 'tipo_de_acidente': 'Tipo de Acidente'},
    color='total_criticidade',
    color_continuous_scale='Reds',
    text='total_criticidade'
)
fig_top.update_layout(showlegend=False, height=450)
st.plotly_chart(fig_top, use_container_width=True)

st.subheader("Taxa de Criticidade por Ocorrência")

colunas_criticidade = ['levemente_feridos', 'moderadamente_feridos', 'gravemente_feridos', 'mortos']
df_filtrado['criticidade_total'] = df_filtrado[colunas_criticidade].sum(axis=1)

ocorrencias = df_filtrado['tipo_de_acidente'].value_counts().to_frame(name='total_ocorrencias')
criticidade = df_filtrado.groupby('tipo_de_acidente')[colunas_criticidade].sum()
criticidade['criticidade_total'] = criticidade.sum(axis=1)

dados_taxa = criticidade.join(ocorrencias)
dados_taxa['taxa_criticidade'] = dados_taxa['criticidade_total'] / dados_taxa['total_ocorrencias']
top_taxa = dados_taxa.sort_values('taxa_criticidade', ascending=False).head(10)

fig_taxa = px.bar(
    top_taxa,
    x='taxa_criticidade',
    y=top_taxa.index,
    orientation='h',
    title='Top 10 Tipos de Acidente com Maior Taxa de Feridos/Mortos por Ocorrência',
    labels={'taxa_criticidade': 'Taxa de Feridos/Mortos', 'tipo_de_acidente': 'Tipo de Acidente'},
    color='taxa_criticidade',
    color_continuous_scale='Reds',
    text='taxa_criticidade'
)
fig_taxa.update_layout(showlegend=False, height=450)
st.plotly_chart(fig_taxa, use_container_width=True)
