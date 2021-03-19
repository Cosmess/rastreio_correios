# usuairo do serviço api.linketrack.com esta configurado  como usuario teste
import requests

codigo = input("Didite ou cole o codigo de rastreio:  ")
url = 'https://api.linketrack.com/track/json?user=teste&token=1abcd00b2731640e886fb41a8a9671ad1434c599dbaa0a0de9a5aa619f29a83f&codigo='+codigo

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)
dados = response.json() 

print('Codigo Rastreio: ' + dados['codigo'])
print('Serviço: ' + dados['servico'])
print('Quantidade: {}'.format(dados['quantidade']))
print('Ultimos Status da sua encomenda:')
print(dados['eventos'][0]['status'])
print(dados['eventos'][1]['local'])