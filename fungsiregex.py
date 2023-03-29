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


def changealay(text):
    alay = dict(zip(df_kbbi['TIDAKBAKU'], df_kbbi['BAKU']))
    text = ' '.join([alay[word] if word in alay else word for word in text.split(' ')])
    return text