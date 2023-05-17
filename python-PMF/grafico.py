# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from datetime import datetime 
import time
import requests as re
import pandas as pd 

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

df = pd.DataFrame.from_dict(dados)
print(df)

print(hoje = datetime.today())
#formatted_date2 = time.strptime(hoje, "%d/%m/%Y")

##print(formatted_date1)
##print(formatted_date2)

df = pd.DataFrame.from_dict(dados)
print(df)

'''    
3600 em tempo unit é igual a 1hora
'''