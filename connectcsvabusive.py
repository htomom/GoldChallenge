import pandas as pd
import re

#load file abusive
df_abusive = pd.read_csv('D:/Binar/Challenge/BinarChallenge1/AssetChallenge/abusive.csv')
df_abusive


#load file kamus alay
df_kbbi = pd.read_csv('D:/Binar/Challenge/BinarChallenge1/AssetChallenge/new_kamusalay.csv', encoding='latin-1', header=None)
df_kbbi

#buat header data kamus alay
df_kbbi.columns = ['TIDAKBAKU', 'BAKU']
df_kbbi.head()
