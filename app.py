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
        text-align: center; color: #FFD700; font-size: 22px; font-weight: bold; 
        border-bottom: 2px solid #FFD700; padding: 10px; margin-bottom: 20px;
    }
    .metric-card {
        background-color: #1A1C23; padding: 15px; border-radius: 10px;
        border-left: 5px solid #FFD700; margin: 10px 0;
    }
    .metric-card h3 { font-size: 14px; color: #FFD700; text-transform: uppercase; }
    .metric-card h2 { font-size: 28px; font-weight: bold; }
    </style>
    <div class="selo-sidney">🔱 SIDNEY ALMEIDA - DASHBOARD SUPREMO V111 🔱</div>
    """, unsafe_allow_html=True)

# --- 2. DADOS DOS OPERADORES (ESTRUTURA FIXA PARA EVITAR ERRO) ---
if 'dados' not in st.session_state:
    st.session_state.dados = {
        'OPERADOR': ['PAULO', 'MARCOS', 'JESSICA'],
        'ALÔ': [150, 162, 100],
        'CPC': [90, 40, 50],
        'PROMESSA': [25, 5, 10],
        'VALOR': [2500.00, 500.00, 1200.00],
        'PAUSA_MIN': [35, 55, 40],
        'LOGADO_MIN': [540, 555, 530]
    }

df = pd.DataFrame(st.session_state.dados)

# CÁLCULOS TOTAIS
total_valor = df['VALOR'].sum()
total_promessas = df['PROMESSA'].sum()
total_cpc = df['CPC'].sum()

# CORREÇÃO DA FÓRMULA: PROMESSA / CPC
conversao = (total_promessas / total_cpc) * 100 if total_cpc > 0 else 0

# --- 3. INTERFACE DE ABAS ---
abas = st.tabs(["👑 Cockpit", "👥 Gestão", "☎️ Discador", "📡 Telefonia", "🐍 Sabotagem", "📂 Exportação"])

# --- ABA 01: COCKPIT (SANEADO) ---
with abas[0]:
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f"<div class='metric-card'><h3>TOTAL VALOR</h3><h2>R$ {total_valor:,.2f}</h2></div>", unsafe_allow_html=True)
    with c2:
        st.markdown(f"<div class='metric-card'><h3>TOTAL PROMESSAS</h3><h2>{total_promessas}</h2></div>", unsafe_allow_html=True)
    with c3:
        st.markdown(f"<div class='metric-card'><h3>CONVERSÃO</h3><h2>{conversao:.1f}%</h2></div>", unsafe_allow_html=True)
    
    st.divider()
    
    # Médias seguras
    m_pau = int(df['PAUSA_MIN'].mean())
    st.write(f"**Média Tempo Logado:** {int(df['LOGADO_MIN'].mean() // 60)}h | **Média de Pausa:** {m_pau} min")
    if m_pau > 45: st.error("⚠️ Alerta: Média de Pausa Excedida")

# --- ABA 02: GESTÃO (ONDE ESTAVAM OS OPERADORES) ---
with abas[1]:
    st.subheader("👥 Detalhamento por Operador")
    st.table(df) # Uso de table para garantir que apareça sempre

# --- ABAS TÉCNICAS (DETALHAMENTO CLÍNICO) ---
with abas[2]: # Discador
    st.table(pd.DataFrame({'DIAGNÓSTICO': ['Vácuo 1.00x'], 'PROGNÓSTICO': ['Perda de Meta'], 'SOLUÇÃO': ['Reset IA-Sentinela']}))

with abas[3]: # Telefonia
    st.table(pd.DataFrame({'DIAGNÓSTICO': ['Latência Alta'], 'PROGNÓSTICO': ['Delay Voz'], 'SOLUÇÃO': ['Reset Rota SIP']}))

# --- FOOTER ---
st.markdown(f"--- \n **SISTEMA V111 ATIVO** | STAKE: **1 Real**")
                 
