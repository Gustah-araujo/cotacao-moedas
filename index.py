import requests

element = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')

response = element.json()

coin = response['USDBRL']
coin2 = response['EURBRL']


print('-'*50)
print(coin['code'] + ' - ' + coin['codein'])
print(coin['bid'])

print('-'*50)
print(coin2['code'] + ' - ' + coin2['codein'])
print(coin2['bid'])