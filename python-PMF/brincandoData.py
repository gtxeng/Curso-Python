from datetime import datetime 
import time
import requests as re
import pandas as pd 
import matplotlib.pyplot as plt

#Pegar data de compra do token
ticker = "BTC" #input("ticker: ")
dia = "17"     #input("dia: ")
mes = "10"     #input("mês: ")
ano = "2020"   #input("ano: ")

link2 = ano + "/" + mes + "/" + dia
link1 = 'https://www.mercadobitcoin.net/api/' + ticker + '/day-summary/'
url = link1 + link2 
print(url)
resp = re.get(url)
dados = resp.json()
print(dados)
diaCompra = dia + "/" + mes + "/" + ano
comparado = time.strptime(diaCompra, "%d/%m/%Y")
hoje = datetime.strftime(datetime.now(),"%d/%m/%y")
print(hoje)
print(comparado)
df = pd.DataFrame.from_dict(resp)

while hoje > comparado:
 )
print("-------------------------------")
print(df)

y= df['price']
plt.plot(x,y)
plt.show()

df.to_csv("arquivo.csv",	index=False)

'''    
3600 em tempo unit é igual a 1hora
'''