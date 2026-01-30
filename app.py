import streamlit as st
import pandas as pd
from datetime import datetime
import hashlib

# --- 1. CAMADA DE SOBERANIA (BLINDAGEM S.A.) ---
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
    .metric-card h3 { font-size: 16px; color: #FFD700; margin-bottom: 5px; text-transform: uppercase; }
    .metric-card h2 { font-size: 32px; font-weight: bold; margin: 0; color: #FFFFFF; }
    .metric-card p { font-size: 14px; color: #AAAAAA; margin-top: 5px; }
    </style>
    <div class="selo-sidney">🔱 SIDNEY ALMEIDA - DASHBOARD SUPREMO V111 🔱</div>
    """, unsafe_allow_html=True)

# --- 2. MEMÓRIA QUÂNTICA: DADOS ---
if 'dados' not in st.session_state:
    st.session_state.dados = {
        'OPERADOR': ['PAULO', 'MARCOS'],
        'ALÔ': [150, 162],
        'CPC': [90, 40],
        'PROMESSA': [25, 5],
        'VALOR': [2500.00, 500.00],
        'TEMPO_LOGADO_MIN': [540, 555],
        'PAUSA_MINUTOS': [35, 55]
    }

df = pd.DataFrame(st.session_state.dados)

# CÁLCULOS CONSOLIDADOS
total_valor = df['VALOR'].sum()
total_promessas = df['PROMESSA'].sum()
total_cpc = df['CPC'].sum()
total_alo = df['ALÔ'].sum()

# CORREÇÃO DA FÓRMULA: PROMESSA / CPC
conversao_ajustada = (total_promessas / total_cpc) * 100 if total_cpc > 0 else 0

# MÉDIAS CONSOLIDADAS
media_tempo_min = df['TEMPO_LOGADO_MIN'].mean()
media_pausa_min = df['PAUSA_MINUTOS'].mean()

# --- 3. ARQUITETURA DE ABAS ---
abas = st.tabs(["👑 Cockpit", "👥 Gestão", "☎️ Discador", "📡 Telefonia", "🐍 Sabotagem", "⚖️ Jurídico", "📂 Exportação"])

# --- ABA 01: COCKPIT (SANEADO E CORRIGIDO) ---
with abas[0]:
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f"""<div class='metric-card'>
            <h3>TOTAL DE VALOR</h3><h2>R$ {total_valor:,.2f}</h2>
            <p>Meta X: R$ {total_valor * 0.5:,.2f}</p>
        </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown(f"""<div class='metric-card'>
            <h3>TOTAL DE PROMESSAS</h3><h2>{total_promessas}</h2>
            <p>Volume de Prova</p>
        </div>""", unsafe_allow_html=True)
    with c3:
        # AQUI FOI APLICADA A CORREÇÃO: PROMESSA / CPC
        st.markdown(f"""<div class='metric-card'>
            <h3>CONVERSÃO</h3><h2>{conversao_ajustada:.1f}%</h2>
            <p>Fórmula: Promessa / CPC</p>
        </div>""", unsafe_allow_html=True)

    st.divider()
    
    col_inf1, col_inf2 = st.columns(2)
    with col_inf1:
        st.markdown(f"**Tempo Logado Médio:** {int(media_tempo_min // 60)}h {int(media_tempo_min % 60)}min")
    with col_inf2:
        st.markdown(f"**Média de Pausa Consolidada:** {int(media_pausa_min)} min")
        if media_pausa_min > 45: 
            st.error("⚠️ MÉDIA DE PAUSA EXCEDIDA")

# --- VISÕES TÉCNICAS (DETALHAMENTO CLÍNICO) ---
with abas[2]: # Discador
    st.subheader("☎️ Discador - Diagnóstico, Prognóstico e Solução")
    st.table(pd.DataFrame({
        'DIAGNÓSTICO': ['Vácuo Detectado'], 'PROGNÓSTICO': ['Perda de Meta'], 'SOLUÇÃO': ['Reiniciar IA-Sentinela']
    }))

with abas[3]: # Telefonia
    st.subheader("📡 Telefonia - Diagnóstico, Prognóstico e Solução")
    st.table(pd.DataFrame({
        'DIAGNÓSTICO': ['Latência Oscilante'], 'PROGNÓSTICO': ['Delay Voz'], 'SOLUÇÃO': ['Reset Rota SIP']
    }))

# --- FOOTER ---
st.markdown(f"--- \n **SISTEMA V111 ATIVO** | STAKE: **1 Real**")
