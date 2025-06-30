import unicodedata
import streamlit as st
import pandas as pd

@st.cache_data
def carregar_dados():
    dt = pd.read_csv('data/demostrativo_acidentes_viabrasil.csv', encoding='ISO-8859-1', sep=';', on_bad_lines='skip')
    dt = pd.read_csv('data/demostrativo_acidentes_viabrasil.csv', encoding='ISO-8859-1', sep=';', on_bad_lines='skip')
    dt['km'] = dt['km'].str.replace(',', '.').astype(float).astype(int)
    veiculos_cols = [
        'automovel', 'bicicleta', 'caminhao', 'moto', 'onibus', 'outros',
        'tracao_animal', 'transporte_de_cargas_especiais', 'trator_maquinas', 'utilitarios'
    ]
    dt = dt[~(dt[veiculos_cols] == 0).all(axis=1)].reset_index(drop=True)
    dt = dt.drop(columns=['n_da_ocorrencia', 'tipo_de_ocorrencia', 'tracao_animal','transporte_de_cargas_especiais', 'trator_maquinas'])
    dt['data'] = pd.to_datetime(dt['data'], format='%d/%m/%Y')
    dt['horario'] = pd.to_datetime(dt['horario'], format='%H:%M:%S').dt.time
    dt['sentido'] = dt['sentido'].replace({
        'Crescente': 'Norte',
        'Decrescente': 'Sul'
    })
    colunas_feridos = ['levemente_feridos', 'moderadamente_feridos', 'gravemente_feridos', 'mortos']
    for c in colunas_feridos:
        dt[c] = pd.to_numeric(dt[c], errors='coerce').fillna(0)
    dt['teve_feridos'] = dt[colunas_feridos].sum(axis=1) > 0
    dt['tipo_de_acidente'] = dt['tipo_de_acidente'].fillna("Não informado")
    dt['tipo_de_acidente'] = dt['tipo_de_acidente'].apply(lambda x: unicodedata.normalize('NFD', x).encode('ascii', 'ignore').decode('utf-8').upper())
    dt['data'] = pd.to_datetime(dt['data'], format='%d/%m/%Y', errors='coerce')
    dt['tipo_de_acidente'] = dt['tipo_de_acidente'].fillna("Não informado")
    colunas = ['levemente_feridos', 'moderadamente_feridos', 'gravemente_feridos', 'mortos']
    for c in colunas:
        dt[c] = pd.to_numeric(dt[c], errors='coerce').fillna(0)
    dt['criticidade'] = dt[colunas].sum(axis=1)
    return dt