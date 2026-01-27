import streamlit as st
import pandas as pd
import datetime

# --- CONFIGURAÇÃO DA INTERFACE S.P.A. ---
st.set_page_config(page_title="S.P.A. Dashboard", layout="wide", page_icon="🛰️")

# --- CABEÇALHO ---
st.title("🛰️ S.P.A. - SENTINELA DE PERFORMANCE ATIVA")
st.subheader("PROPRIEDADE INTELECTUAL: SIDNEY ALMEIDA")
st.write(f"**Gestor Geral:** S.A. | **Status:** Sincronizado")
st.divider()

# --- MÉTRICAS ---
c1, c2, c3 = st.columns(3)
with c1:
    st.metric("ESTORNO RECUPERADO", "R$ 1.250,40", "+R$ 180,20")
with c2:
    st.metric("EFICIÊNCIA MAILING", "88%", "-4% vácuo")
with c3:
    st.metric("ALERTAS DE CONDUTA", "5", "Bloco 1")

# --- TABELA DA FAVELINHA ---
st.subheader("📊 Tabela da Favelinha - Controle Realtime")
dados = {
    "OPERADOR": ["MARCOS", "ANA", "RICARDO", "JULIA"],
    "STATUS": ["PENDENTE", "LIBERADO", "BLOQUEADO", "LIBERADO"],
    "META X (%)": [50.0, 100.0, 0.0, 100.0],
    "FALHAS (B1)": [2, 0, 3, 0]
}
st.table(pd.DataFrame(dados))

# --- RODAPÉ ---
st.divider()
st.info(f"💡 **Sistema SPA V2.5** - Desenvolvido por Sidney Almeida.")
st.caption(f"Servidor Online: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
