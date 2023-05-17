import requests as re
import pandas as pd 
import matplotlib.pyplot as plt
from datetime import datetime

url = "https://www.mercadobitcoin.net/api/BTC/trades"
resp = re.get(url)
dados = resp.json()

df = pd.DataFrame.from_dict(dados)

df['date']=(pd.to_datetime(df['date'],unit='s'))

print(df.describe())#
print(df.head())
