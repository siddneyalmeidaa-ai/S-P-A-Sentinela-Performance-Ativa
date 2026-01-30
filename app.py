import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. SOBERANIA S.A. (CONFIGURAÇÃO) ---
st.set_page_config(page_title="S.A. SUPREMO - V111", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    .stApp {background-color: #0E1117; color: #FFFFFF;}
    .selo-sidney {
        text-align: center; color: #FFD700; font-size: 22px; font-weight: bold; 
        border-bottom: 2px solid #FFD700; padding: 10px; margin-bottom: 15px;
    }
    .metric-card {
        background-color: #1A1C23; padding: 15px; border-radius: 10px;
        border-left: 5px solid #FFD700; margin: 8px 0;
    }
    .metric-card h3 { font-size: 14px; color: #FFD700; margin-bottom: 2px; }
    .metric-card h2 { font-size: 28px; font-weight: bold; margin: 0; }
    .metric-card p { font-size: 12px; color: #AAAAAA; }
    </style>
    <div class="selo-sidney">🔱 SIDNEY ALMEIDA - DASHBOARD SUPREMO V111 🔱</div>
    """, unsafe_allow_html=True)

# --- 2. DADOS DOS OPERADORES (RECUPERADOS) ---
if 'dados' not in st.session_state:
    st.session_state.dados = {
        'OPERADOR': ['PAULO', 'MARCOS', 'JESSICA'],
        'ALÔ': [150, 162, 100],
        'CPC': [90, 40, 50],
        'PROMESSA': [25, 5, 10],
        'VALOR': [2500.00, 500.00, 1200.00],
        'PAUSA_MIN': [35, 55, 40],
        'TEMPO_LOGADO_MIN': [540, 555, 530]
    }

df = pd.DataFrame(st.session_state.dados)

# CÁLCULOS TOTAIS
total_valor = df['VALOR'].sum()
total_promessas = df['PROMESSA'].sum()
total_cpc = df['CPC'].sum()
total_alo = df['ALÔ'].sum()
# CORREÇÃO: PROMESSA / CPC
conversao = (total_promessas / total_cpc) * 100 if total_cpc > 0 else 0

# --- 3. INTERFACE DE ABAS ---
abas = st.tabs(["👑 Cockpit", "👥 Gestão", "☎️ Discador", "📡 Telefonia", "🐍 Sabotagem", "📂 Exportação"])

# --- ABA 01: COCKPIT (SANEADO) ---
with abas[0]:
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f"<div class='metric-card'><h3>TOTAL VALOR</h3><h2>R$ {total_valor:,.2f}</h2><p>Meta X: R$ {total_valor*0.5:,.2f}</p></div>", unsafe_allow_html=True)
    with c2:
        st.markdown(f"<div class='metric-card'><h3>TOTAL PROMESSAS</h3><h2>{total_promessas}</h2><p>Volume de Prova Acumulado</p></div>", unsafe_allow_html=True)
    with c3:
        st.markdown(f"<div class='metric-card'><h3>CONVERSÃO</h3><h2>{conversao:.1f}%</h2><p>Promessa / CPC</p></div>", unsafe_allow_html=True)
    
    st.divider()
    
    m1, m2 = st.columns(2)
    with m1:
        st.write(f"**Tempo Logado Médio:** {int(df['TEMPO_LOGADO_MIN'].mean() // 60)}h {int(df['TEMPO_LOGADO_MIN'].mean() % 60)}min")
    with m2:
        media_p = int(df['PAUSA_MIN'].mean())
        if media_p > 45:
            st.error(f"**Média de Pausa Consolidada:** {media_p} min (EXCEDIDO)")
        else:
            st.success(f"**Média de Pausa Consolidada:** {media_p} min")

# --- ABA 02: GESTÃO (OPERADORES DE VOLTA) ---
with abas[1]:
    st.subheader("👥 Performance Detalhada")
    st.dataframe(df, use_container_width=True)

# --- ABA 03: DISCADOR (DETALHADO) ---
with abas[2]:
    st.subheader("☎️ Clínica do Discador")
    st.table(pd.DataFrame({
        'DIAGNÓSTICO': ['Vácuo Detectado (1.00x)', 'Mailing Saturado'],
        'PROGNÓSTICO': ['Queda de Performance', 'Aumento de Custos'],
        'SOLUÇÃO': ['Reset IA-Sentinela', 'Filtro de Higienização']
    }))

# --- ABA 04: TELEFONIA (DETALHADO) ---
with abas[3]:
    st.subheader("📡 Clínica de Telefonia")
    st.table(pd.DataFrame({
        'DIAGNÓSTICO': ['Latência > 50ms', 'Voz Robótica'],
        'PROGNÓSTICO': ['Delay no Atendimento', 'Queda de Chamadas'],
        'SOLUÇÃO': ['Trocar Rota SIP', 'Ajustar QoS']
    }))

# --- FOOTER ---
st.markdown(f"--- \n **SISTEMA V111 ATIVO** | STAKE: **1 Real**")
