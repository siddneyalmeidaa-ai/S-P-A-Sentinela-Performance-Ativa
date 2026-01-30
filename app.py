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
    /* AJUSTE DE FONTE REDUZIDA */
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

# CÁLCULO DA CONVERSÃO (CPCA / Promessa) conforme solicitado
conversao = (total_cpca / total_promessas) if total_promessas > 0 else 0

# MÉDIAS CONSOLIDADAS
media_tempo_min = df['TEMPO_LOGADO_MIN'].mean()
media_pausa_min = df['PAUSA_MINUTOS'].mean()

# --- 3. ARQUITETURA DE ABAS ---
abas = st.tabs(["👑 Cockpit", "👥 Gestão", "☎️ Discador", "📡 Telefonia", "🐍 Sabotagem", "⚖️ Jurídico", "📂 Exportação"])

# --- ABA 01: COCKPIT (INTERFACE AJUSTADA) ---
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
        st.markdown(f"""<div class='metric-card'>
            <h3>CONVERSÃO</h3><h2>{conversao:.1f}%</h2>
            <p>CPCA / Promessa</p>
        </div>""", unsafe_allow_html=True)

    st.divider()
    
    col_inf1, col_inf2 = st.columns(2)
    with col_inf1:
        st.markdown(f"**Tempo Logado Médio:** {int(media_tempo_min // 60)}h {int(media_tempo_min % 60)}min")
        st.markdown(f"**Média de Pausa:** {int(media_pausa_min)} min")
    with col_inf2:
        st.markdown(f"**Volume de Prova (ALÔ/CPC):** {total_alo} / {total_cpc}")
        if media_pausa_min > 45: st.error("⚠️ Alerta: Média de Pausa Excedida")

# --- ABA 03: VISÃO DISCADOR (DETALHADO) ---
with abas[2]:
    st.subheader("☎️ Discador - Diagnóstico Técnico")
    diag_disc = pd.DataFrame({
        'DIAGNÓSTICO': ['Vácuo Detectado (1.00x)', 'Mailing Saturado'],
        'PROGNÓSTICO': ['Quebra de Meta Próxima Rodada', 'Aumento de CPC Fantasma'],
        'SOLUÇÃO': ['Reset IA-Sentinela', 'Filtro de Higienização Ativo']
    })
    st.table(diag_disc)

# --- ABA 04: VISÃO TELEFONIA (DETALHADO) ---
with abas[3]:
    st.subheader("📡 Telefonia - Auditoria de Link")
    diag_tel = pd.DataFrame({
        'DIAGNÓSTICO': ['Latência > 50ms', 'Jitter Oscilante'],
        'PROGNÓSTICO': ['Delay no Diálogo', 'Perda de Pacotes'],
        'SOLUÇÃO': ['Reiniciar Rota SIP', 'Priorizar QoS no Firewall']
    })
    st.table(diag_tel)

# --- FOOTER ---
st.markdown(f"--- \n **SISTEMA V111 ATIVO** | STAKE: **1 Real**")
