import pandas as pd

try:
    df = pd.read_csv("csv/despesas.csv", encoding="utf-8")
except UnicodeDecodeError:
    try:
        df = pd.read_csv("csv/despesas.csv", encoding="cp1252")
    except UnicodeDecodeError:
        df = pd.read_csv("csv/despesas.csv", encoding="latin1")

print(df.head())