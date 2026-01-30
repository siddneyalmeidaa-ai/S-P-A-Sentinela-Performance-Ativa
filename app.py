import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. SOBERANIA S.A. (CONFIGURAÇÃO VISUAL) ---
st.set_page_config(page_title="S.A. SUPREMO - V111", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    .stApp {background-color: #0E1117; color: #FFFFFF;}
    .selo-sidney {
        text-align: center; color: #FFD700; font-size: 20px; font-weight: bold; 
        border-bottom: 2px solid #FFD700; padding: 10px; margin-bottom: 15px;
    }
    .metric-card {
        background-color: #1A1C23; padding: 12px; border-radius: 8px;
        border-left: 4px solid #FFD700; margin: 5px 0;
    }
    .metric-card h3 { font-size: 13px; color: #FFD700; text-transform: uppercase; margin: 0; }
    .metric-card h2 { font-size: 24px; font-weight: bold; margin: 5px 0; }
    </style>
    <div class="selo-sidney">🔱 SIDNEY ALMEIDA - DASHBOARD SUPREMO V111 🔱</div>
    """, unsafe_allow_html=True)

# --- 2. CRIAÇÃO SEGURA DOS DADOS (BLOQUEIO DE KEYERROR) ---
# Garantindo que todas as colunas necessárias existam na inicialização
df_base = pd.DataFrame({
    'OPERADOR': ['PAULO', 'MARCOS', 'JESSICA'],
    'ALÔ': [150, 162, 100],
    'CPC': [90, 40, 50],
    'PROMESSA': [25, 5, 10],
    'VALOR': [2500.00, 500.00, 1200.00],
    'PAUSA_MIN': [35, 55, 40],
    'LOGADO_MIN': [540, 555, 530]
})

# CÁLCULOS TOTAIS
total_valor = df_base['VALOR'].sum()
total_promessas = df_base['PROMESSA'].sum()
total_cpc = df_base['CPC'].sum()

# CORREÇÃO DA FÓRMULA: PROMESSA / CPC
conversao_final = (total_promessas / total_cpc) * 100 if total_cpc > 0 else 0

# --- 3. ARQUITETURA DE ABAS ---
abas = st.tabs(["👑 Cockpit", "👥 Gestão", "☎️ Discador", "📡 Telefonia", "🐍 Sabotagem", "📂 Exportação"])

# --- ABA 01: COCKPIT (SUMÁRIO EXECUTIVO) ---
with abas[0]:
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"<div class='metric-card'><h3>VALOR TOTAL</h3><h2>R$ {total_valor:,.2f}</h2></div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div class='metric-card'><h3>PRODUTIVIDADE</h3><h2>{total_promessas}</h2></div>", unsafe_allow_html=True)
    with col3:
        st.markdown(f"<div class='metric-card'><h3>CONVERSÃO</h3><h2>{conversao_final:.1f}%</h2></div>", unsafe_allow_html=True)
    
    st.divider()
    
    # Médias exibidas de forma simples para evitar erro visual
    m_pau = int(df_base['PAUSA_MIN'].mean())
    m_log = int(df_base['LOGADO_MIN'].mean())
    st.write(f"**Tempo Logado Médio:** {m_log // 60}h {m_log % 60}min")
    st.write(f"**Média de Pausa:** {m_pau} min")
    if m_pau > 45: st.error("⚠️ Alerta: Média de Pausa Excedida")

# --- ABA 02: GESTÃO (OPERADORES RECUPERADOS) ---
with abas[1]:
    st.subheader("👥 Performance Detalhada")
    st.table(df_base) # Força a exibição da tabela completa

# --- ABAS TÉCNICAS (DIAGNÓSTICO E SOLUÇÃO) ---
with abas[2]: # Discador
    st.table(pd.DataFrame({'DIAGNÓSTICO': ['Vácuo 1.00x'], 'SOLUÇÃO': ['Reiniciar IA-Sentinela']}))

with abas[3]: # Telefonia
    st.table(pd.DataFrame({'DIAGNÓSTICO': ['Latência Alta'], 'SOLUÇÃO': ['Reset Rota SIP']}))

# --- FOOTER ---
st.markdown(f"--- \n **SISTEMA V111 ATIVO** | STAKE: **1 Real**")
