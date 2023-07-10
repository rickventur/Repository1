# Passo 1: Importar base de dados
import pandas as pd
from twilio.rest import Client

dataFrame = pd.read_csv(r"C:\Users\Austin\Desktop\Portifólio\Travel Bonus Analisys\clientes.csv", encoding='latin', sep=';')

# Passo 2: Objetivos
#   entender as informações disponíveis

print(dataFrame.info())

#   procurar erros na base de dados --> Unnamed: 8 <--

dataFrame = dataFrame.drop(['Unnamed: 8'], axis=1)

# Passo 3: tratamento no formato errado
#   valores no formato errado

pd.to_numeric(dataFrame['Salário Anual (R$)'], errors='coerce')
print(dataFrame)

#   valores vazios --> 36 valores vazios <--
# Passo 4: Analise inicial - entender a nota do cliente

import plotly.express as px

graph = px.histogram()

for colunas in dataFrame.columns:
    graph = px.histogram(dataFrame, histfunc='avg')
    graph.show()
# Passo 5: Analise completa traçar o perfil ideal do cliente
#   entender como cada característica do cliente impacta na nota
#   entender como a faixa etária do cliente mostra se é um cliente bom ou ruim

# Abrir os arquivos em Excel
# Para cada arquivo:
# Verificar se algum valor na coluna Vendas do arquivo é maior que 55.000
# Se for maior que 55.000 -> Enviar SMS com nome, mes e vendas

# Your Account SID from twilio.com/console
account_sid = "AC2628af3ef76cd40c0089afb9bfa8d7bf"
# Your Auth Token from twilio.com/console
auth_token  = "efcf79aafdb10f0a995188d8825be60d"
client = Client(account_sid, auth_token)

# Caso contário não faça nada

