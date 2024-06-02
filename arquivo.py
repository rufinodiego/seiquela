
#Bibliotecas necessárias para as dashboards
import cufflinks as cf
from plotly.offline import plot, iplot
import plotly.offline as py
import pandas as pd
import numpy as np
import plotly.graph_objs as go
import plotly.io as pio
import plotly.express as px
import matplotlib.pyplot as plt
from dash import Dash, html, dcc
import chart_studio.dashboard_objs as dashboard
import matplotlib.pyplot as plt
import seaborn as sns
from plotly.subplots import make_subplots

cf.go_offline()
pio.renderers.default = 'colab'

import chart_studio
chart_studio.tools.set_credentials_file(username='paotheon', api_key='Asvx48GFjvPNyqwsuOmf')

import chart_studio.plotly as pyo

arquivo = '/content/drive/MyDrive/recife/Dashboard/empresas_ativas_tratadas_DEFINITIVO.csv'
dt_geral_novo = pd.read_csv(arquivo, header=0)

pio.renderers.default = 'colab'



import streamlit as st
import pandas as pd

paleta_cores = ['#4e79a7', '#f28e2c', '#e15759', '#76b7b2', '#59a14f', '#edc949', '#b07aa1', '#ff9da7', '#9c755f', '#bab0ac',
                '#ffbf79', '#eafc8d', '#82c6e2', '#ce7d7d', '#6fc69c', '#4e79a7', '#f28e2c', '#e15759', '#76b7b2', '#59a14f']

# Adicionar uma opção 'Todos' no início da lista de bairros
bairros = ['Todos'] + sorted(dt_geral_novo['nome_bairro'].unique())

# Definir o layout do aplicativo
st.title('Distribuição de Serviços em Recife')

# Dropdown para selecionar o bairro
selected_bairro = st.selectbox('Selecione um bairro', bairros)

# Atualizar o gráfico de barras com base na seleção do bairro
if selected_bairro == 'Todos':
    # Se 'Todos' é selecionado, não há necessidade de filtrar os dados
    filtered_data = dt_geral_novo
    titulo = 'Distribuição de Serviços em Recife'
else:
    # Filtrar os dados com base no bairro selecionado
    filtered_data = dt_geral_novo[dt_geral_novo['nome_bairro'] == selected_bairro]
    titulo = f'Distribuição de Serviços no Bairro {selected_bairro}'

contagem_servicos = filtered_data['nome_grupo'].value_counts()

# Criar o gráfico de barras
data = go.Bar(x=contagem_servicos.index, y=contagem_servicos.values, marker=dict(color=paleta_cores[:len(contagem_servicos)]))
layout = go.Layout(title=titulo, xaxis=dict(title='Tipo de Serviço'), yaxis=dict(title='Quantidade do serviço oferecido'))
fig = go.Figure(data=[data], layout=layout)

# Exibir o gráfico no Streamlit
st.plotly_chart(fig)
