import connectcsvabusive
import pandas as pd
import re

abusiveword = [df['ABUSIVE']]
print(abusiveword)

def censor(replaceword):
    for word in abusiveword:
        replaceword = re.sub(abusiveword, '*', * len(word), flags=re.IGNORECASE)
        print(f"Forbidden word REMOVED: {word}")
    return replaceword

df = censor(D:/Binar/Challenge/Binar Challenge 1/Asset Challenge/data.csv)
print(df)