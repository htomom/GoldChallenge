import connectcsv
import pandas as pd
import re

df_abusive
df_kbbi

def censor(text):
    abusiveword = df_abusive['ABUSIVE'].tolist()
    for word in abusiveword:
        pattern = re.compile(r'\b{}\b'.format(word))
        length = len(word)
        replacement = '*' * length
        text = pattern.sub(replacement, text.lower())
    
    return text


def changealay(txt):
    alay = dict(zip(df_kbbi['TIDAKBAKU'], df_kbbi['BAKU']))
    txt = ' '.join([alay[word] if word in alay else word for word in txt.split(' ')])
return txt