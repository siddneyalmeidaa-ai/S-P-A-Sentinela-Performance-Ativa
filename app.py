import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. CONFIGURAÇÃO E BLINDAGEM ---
st.set_page_config(page_title="S.A. SUPREMO - V111", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    .stApp {background-color: #0E1117; color: #FFFFFF;}
    .selo-sidney {
        text-align: center; color: #FFD700; font-size: 24px; font-weight: bold; 
        border-bottom: 2px solid #FFD700; padding: 10px; margin-bottom: 20px;
    }
    .metric-card {
        background-color: #1A1C23; padding: 15px; border-radius: 10px;
        border-left: 5px solid #FFD700; margin: 10px 0;
    }
    .metric-card h3 { font-size: 16px; color: #FFD700; }
    .metric-card h2 { font-size: 32px; font-weight: bold; }
    </style>
    <div class="selo-sidney">🔱 SIDNEY ALMEIDA - DASHBOARD SUPREMO V111 🔱</div>
    """, unsafe_allow_html=True)

# --- 2. DADOS (OS OPERADORES ESTÃO AQUI) ---
if 'dados' not in st.session_state:
    st.session_state.dados = {
        'OPERADOR': ['PAULO', 'MARCOS'],
        'ALÔ': [150, 162],
        'CPC': [90, 40],
        'PROMESSA': [25, 5],
        'VALOR': [2500.00, 500.00],
        'TEMPO_LOGADO': ['09:00', '09:15'],
        'PAUSA_MIN': [35, 55]
    }

df = pd.DataFrame(st.session_state.dados)

# CÁLCULOS
total_valor = df['VALOR'].sum()
total_promessas = df['PROMESSA'].sum()
total_cpc = df['CPC'].sum()
# NOVA FÓRMULA: PROMESSA / CPC
conversao = (total_promessas / total_cpc) * 100 if total_cpc > 0 else 0

# --- 3. INTERFACE DE ABAS ---
abas = st.tabs(["👑 Cockpit", "👥 Gestão", "☎️ Discador", "📡 Telefonia", "🐍 Sabotagem", "📂 Exportação"])

# --- ABA 01: COCKPIT (RESUMO) ---
with abas[0]:
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f"<div class='metric-card'><h3>TOTAL VALOR</h3><h2>R$ {total_valor:,.2f}</h2></div>", unsafe_allow_html=True)
    with c2:
        st.markdown(f"<div class='metric-card'><h3>TOTAL PROMESSAS</h3><h2>{total_promessas}</h2></div>", unsafe_allow_html=True)
    with c3:
        st.markdown(f"<div class='metric-card'><h3>CONVERSÃO</h3><h2>{conversao:.1f}%</h2></div>", unsafe_allow_html=True)
    
    st.divider()
    st.write(f"**Média de Pausa:** {int(df['PAUSA_MIN'].mean())} min")

# --- ABA 02: GESTÃO (ONDE ESTÃO OS OPERADORES) ---
with abas[1]:
    st.subheader("👥 Detalhamento por Operador")
    # AQUI ELES VOLTARAM:
    st.dataframe(df, use_container_width=True)
    
    st.divider()
    st.subheader("🔥 Mapa de Calor de Pausas")
    for _, row in df.iterrows():
        if row['PAUSA_MIN'] > 45:
            st.error(f"ALERTA: {row['OPERADOR']} excedeu a Trava 45 ({row['PAUSA_MIN']}min)")
        else:
            st.success(f"{row['OPERADOR']}: {row['PAUSA_MIN']}min (Dentro da meta)")

# --- ABAS TÉCNICAS (DIAGNÓSTICO/PROGNÓSTICO/SOLUÇÃO) ---
with abas[2]: # Discador
    st.table(pd.DataFrame({
        'DIAGNÓSTICO': ['Vácuo 1.00x'], 'PROGNÓSTICO': ['Perda de Meta'], 'SOLUÇÃO': ['Reset IA-Sentinela']
    }))

with abas[3]: # Telefonia
    st.table(pd.DataFrame({
        'DIAGNÓSTICO': ['Latência Alta'], 'PROGNÓSTICO': ['Delay Voz'], 'SOLUÇÃO': ['Reset Rota SIP']
    }))

# --- FOOTER ---
st.markdown(f"--- \n **SISTEMA V111 ATIVO** | STAKE: **1 Real**")
    
