import streamlit as st
import plotly.graph_objects as go
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
