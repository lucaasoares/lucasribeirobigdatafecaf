import pandas as pd
from sqlalchemy import create_engine

# conexão com banco
engine = create_engine("postgresql://postgres:123456@localhost:5432/iot_db")

# ler CSV
df = pd.read_csv("data/IOT-temp.csv")

print(df.head())

# enviar para o banco
df.to_sql("temperature_readings", engine, if_exists="replace", index=False)

print("Dados enviados com sucesso!")