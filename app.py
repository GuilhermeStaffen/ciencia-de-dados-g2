import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard Acidentes ViaBrasil", layout="wide")

st.title("Dashboard de Acidentes - ViaBrasil")

st.markdown("""
Bem-vindo ao painel interativo que explora dados de acidentes nas rodovias da ViaBrasil.

Esse painel foi desenvolvido como trabalho final para a disciplina de Ciencia de Dados no primeiro semestre de 2025.

### Desenvolvido por:
- Crystopher Kochler
- Eduardo Kochler  
- Guilherme Staffen

### Como navegar:
- Use o menu lateral para explorar diferentes aspectos dos dados.
    - Na aba "Resumo Geral", você vai encontrar uma visão geral dos acidentes, incluindo gráficos de distribuição por KM e por sentido.
    - Na aba "Tipos de Acidente", você poderá analisar os tipos de acidentes mais frequentes e suas distribuições ao longo da rodovia, assim como sua criticidade e veiculos envolvidos.
    - Na aba "Criticidade", você encontra uma visualização da criticidade dos acidentes.
- Filtros serão aplicados em cada seção conforme disponíveis.
    - Na aba "Resumo Geral", no gráfico "Distribuição por Sentido", você pode remover uma ou mais direções clicando em sua legenda.
    - Na aba "Tipos de Acidentes", você pode selecionar um tipo específico de acidente para análise detalhada, verificando a ocorrência do tipo de acidente selecionado nos diferentes trexos da rodovia, assim como sua criticidade e veiculos envolvidos.
    - Na aba "Criticidade", será exibido na lateral esquerda um filtro de período, onde você pode selecionar o intervalo de datas para análise dos acidentes.

### Objetivo:
Este dashboard tem como propósito facilitar a análise dos acidentes registrados na BR-163 entre os anos de 2022 e 2025, utilizando dados fornecidos pela ANTT e referentes ao trecho sob responsabilidade da Concessionária ViaBrasil.
A ferramenta permite uma visualizacao clara e interativa das informações, auxiliando na identificação de padrões, meses com maior incidência de algum tipo de acidente, tipos de acidentes mais críticos e tipo de veículos envolvidos.
""")
