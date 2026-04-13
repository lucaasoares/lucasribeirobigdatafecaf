import pandas as pd
import streamlit as st
from sqlalchemy import create_engine

# conexão com banco
engine = create_engine("postgresql://postgres:123456@localhost:5432/iot_db")

st.set_page_config(page_title="Dashboard IoT", layout="wide")

st.title("📊 Monitoramento de Temperatura IoT")

# =========================
# CARREGAR DADOS
# =========================
df = pd.read_sql("SELECT * FROM temperature_readings", engine)

# corrigir nomes de colunas
df.columns = df.columns.str.replace("/", "_")

# converter data
df["noted_date"] = pd.to_datetime(df["noted_date"], dayfirst=True)

# =========================
# 📁 DADOS BRUTOS
# =========================
st.subheader("📁 Dados Brutos")
st.dataframe(df)

# =========================
# 📊 MÉDIA POR DISPOSITIVO
# =========================
st.subheader("📊 Média de Temperatura por Dispositivo")

media = df.groupby("room_id_id")["temp"].mean()
st.bar_chart(media)

# =========================
# 🔥 TEMPERATURA MÁXIMA
# =========================
st.subheader("🔥 Temperatura Máxima por Dispositivo")

max_temp = df.groupby("room_id_id")["temp"].max()
st.bar_chart(max_temp)

# =========================
# ⏱ LEITURAS POR HORA (GRÁFICO GRANDE)
# =========================
st.subheader("⏱ Leituras por Hora")

# agrupar por hora
df["hora"] = df["noted_date"].dt.floor("h")

leituras = df.groupby("hora")["temp"].count()

st.line_chart(leituras)