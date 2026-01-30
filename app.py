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
        text-align: center; color: #FFD700; font-size: 28px; font-weight: bold; 
        border-bottom: 2px solid #FFD700; padding: 10px; margin-bottom: 25px;
    }
    .metric-card {
        background-color: #1A1C23; padding: 25px; border-radius: 12px;
        border-left: 6px solid #FFD700; margin: 10px 0;
    }
    .metric-card h3 { font-size: 20px; color: #FFD700; margin-bottom: 5px; }
    .metric-card h2 { font-size: 45px; font-weight: bold; margin: 0; }
    .metric-card p { font-size: 16px; color: #AAAAAA; margin-top: 5px; }
    </style>
    <div class="selo-sidney">🔱 SIDNEY ALMEIDA - SUMÁRIO EXECUTIVO INTEGRAL V111 🔱</div>
    """, unsafe_allow_html=True)

# --- 2. MEMÓRIA QUÂNTICA: DADOS ---
if 'dados' not in st.session_state:
    st.session_state.dados = {
        'OPERADOR': ['PAULO', 'MARCOS'],
        'ALÔ': [150, 162],
        'CPC': [90, 40],
        'CPCA': [90, 40],
        'PROMESSA': [25, 5],
        'VALOR': [2500.00, 500.00],
        'TEMPO_LOGADO_MIN': [540, 555],
        'PAUSA_MINUTOS': [35, 55]
    }

df = pd.DataFrame(st.session_state.dados)

# CÁLCULOS CONSOLIDADOS
total_valor = df['VALOR'].sum()
total_promessas = df['PROMESSA'].sum()
total_cpca = df['CPCA'].sum()
total_alo = df['ALÔ'].sum()
total_cpc = df['CPC'].sum()

# NOVA FÓRMULA: PROMESSA / CPCA
conversao_ajustada = (total_promessas / total_cpca) * 100 if total_cpca > 0 else 0

# MÉDIAS CONSOLIDADAS
media_tempo_min = df['TEMPO_LOGADO_MIN'].mean()
media_pausa_min = df['PAUSA_MINUTOS'].mean()

# --- 3. ARQUITETURA DE ABAS ---
abas = st.tabs(["👑 Cockpit", "👥 Gestão", "☎️ Discador", "📡 Telefonia", "🐍 Sabotagem", "⚖️ Jurídico", "📂 Exportação"])

# --- ABA 01: COCKPIT (CORRIGIDO E RESUMIDO) ---
with abas[0]:
    st.subheader("👑 Cockpit - Sumário Executivo")
    
    # LINHA 1: VALOR E PROMESSAS
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"""<div class='metric-card'>
            <h3>TOTAL DE VALOR</h3><h2>R$ {total_valor:.2f}</h2>
            <p>Meta X: R$ {total_valor * 0.5:.2f}</p>
        </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown(f"""<div class='metric-card'>
            <h3>TOTAL DE PROMESSAS</h3><h2>{total_promessas}</h2>
            <p>Volume de Prova</p>
        </div>""", unsafe_allow_html=True)
    
    # LINHA 2: CONVERSÃO E VOLUMES
    c3, c4 = st.columns(2)
    with c3:
        st.markdown(f"""<div class='metric-card'>
            <h3>CONVERSÃO</h3><h2>{conversao_ajustada:.1f}%</h2>
            <p>(Promessa / CPCA)</p>
        </div>""", unsafe_allow_html=True)
    with c4:
        st.markdown(f"""<div class='metric-card'>
            <h3>VOLUME DE PROVA (ALÔ/CPC)</h3><h2>{total_alo} / {total_cpc}</h2>
            <p>Sincronismo de Base</p>
        </div>""", unsafe_allow_html=True)

    st.divider()
    
    # MÉDIAS CONSOLIDADAS
    col_m1, col_m2 = st.columns(2)
    with col_m1:
        st.write(f"**Média Tempo Logado Consolidado:** {int(media_tempo_min // 60)}h {int(media_tempo_min % 60)}min")
    with col_m2:
        st.write(f"**Média Pausa Consolidada:** {int(media_pausa_min)} min")
        if media_pausa_min > 45: st.error("⚠️ MÉDIA DE PAUSA EXCEDIDA")

# --- ABA 03/04: DIAGNÓSTICO DETALHADO ---
with abas[2]: # Discador
    st.subheader("☎️ Discador: Diagnóstico / Prognóstico / Solução")
    st.table(pd.DataFrame({
        'DIAGNÓSTICO': ['Vácuo 1.00x'], 'PROGNÓSTICO': ['Perda de Meta'], 'SOLUÇÃO': ['Reset IA-Sentinela']
    }))

with abas[3]: # Telefonia
    st.subheader("📡 Telefonia: Diagnóstico / Prognóstico / Solução")
    st.table(pd.DataFrame({
        'DIAGNÓSTICO': ['Latência Alta'], 'PROGNÓSTICO': ['Delay Voz'], 'SOLUÇÃO': ['Reiniciar Rota']
    }))

# --- FOOTER ---
st.markdown(f"--- \n **SISTEMA V111 ATIVO** | STAKE: **1 Real**")
