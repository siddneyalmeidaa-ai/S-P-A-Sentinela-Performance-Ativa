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
        text-align: center; color: #FFD700; font-size: 32px; font-weight: bold; 
        border-bottom: 3px solid #FFD700; padding: 15px; margin-bottom: 30px;
    }
    .metric-card {
        background-color: #1A1C23; padding: 30px; border-radius: 15px;
        border-left: 8px solid #FFD700; margin: 15px 0;
        box-shadow: 5px 5px 15px rgba(0,0,0,0.5);
    }
    .metric-card h3 { font-size: 22px; color: #FFD700; margin-bottom: 10px; text-transform: uppercase; }
    .metric-card h2 { font-size: 55px; font-weight: bold; margin: 0; color: #FFFFFF; }
    .metric-card p { font-size: 18px; color: #AAAAAA; margin-top: 10px; }
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

# CÁLCULO DA CONVERSÃO (Promessa / CPCA)
conversao = (total_promessas / total_cpca) * 100 if total_cpca > 0 else 0

# MÉDIAS CONSOLIDADAS
media_tempo_min = df['TEMPO_LOGADO_MIN'].mean()
media_pausa_min = df['PAUSA_MINUTOS'].mean()

# --- 3. ARQUITETURA DE ABAS ---
abas = st.tabs(["👑 Cockpit", "👥 Gestão", "☎️ Discador", "📡 Telefonia", "🐍 Sabotagem", "⚖️ Jurídico", "📂 Exportação"])

# --- ABA 01: COCKPIT (INTERFACE REFORMULADA) ---
with abas[0]:
    # LINHA 1: PODER FINANCEIRO E PROVAS
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"""<div class='metric-card'>
            <h3>TOTAL DE VALOR</h3><h2>R$ {total_valor:,.2f}</h2>
            <p>Meta X (Liberado): R$ {total_valor * 0.5:,.2f}</p>
        </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown(f"""<div class='metric-card'>
            <h3>TOTAL DE PROMESSAS</h3><h2>{total_promessas}</h2>
            <p>Volume de Prova Acumulado</p>
        </div>""", unsafe_allow_html=True)
    
    # LINHA 2: CONVERSÃO E PERFORMANCE TÉCNICA
    c3, c4 = st.columns(2)
    with c3:
        st.markdown(f"""<div class='metric-card'>
            <h3>CONVERSÃO</h3><h2>{conversao:.1f}%</h2>
            <p>Fórmula: Promessa / CPCA</p>
        </div>""", unsafe_allow_html=True)
    with c4:
        st.markdown(f"""<div class='metric-card'>
            <h3>VOLUME DE PROVA (ALÔ/CPC)</h3><h2>{total_alo} / {total_cpc}</h2>
            <p>Sincronismo de Base e Mailing</p>
        </div>""", unsafe_allow_html=True)

    st.divider()
    
    # LINHA 3: MÉDIAS CONSOLIDADAS (O QUE ESTAVA FALTANDO)
    m1, m2, m3 = st.columns(3)
    with m1:
        st.info(f"**Média Tempo Logado:** {int(media_tempo_min // 60)}h {int(media_tempo_min % 60)}min")
    with m2:
        if media_pausa_min > 45:
            st.error(f"**Média Pausa Consolidada:** {int(media_pausa_min)} min (EXCEDIDO)")
        else:
            st.success(f"**Média Pausa Consolidada:** {int(media_pausa_min)} min")
    with m3:
        st.warning(f"**Status Técnico:** Link VIVO 12ms | Vácuo 12%")

# --- ABA 03: VISÃO DISCADOR (DETALHADO) ---
with abas[2]:
    st.subheader("☎️ Discador - Diagnóstico Técnico")
    diag_disc = pd.DataFrame({
        'DIAGNÓSTICO': ['Vácuo Detectado (1.00x)', 'Mailing Saturado'],
        'PROGNÓSTICO': ['Queda de 20% na Conversão', 'Aumento de Pausas'],
        'SOLUÇÃO': ['Reset IA-Sentinela', 'Trocar Base Imediato']
    })
    st.table(diag_disc)

# --- ABA 04: VISÃO TELEFONIA (DETALHADO) ---
with abas[3]:
    st.subheader("📡 Telefonia - Auditoria de Link")
    diag_tel = pd.DataFrame({
        'DIAGNÓSTICO': ['Latência Oscilante', 'Jitter em 0.8ms'],
        'PROGNÓSTICO': ['Voz Robótica/Delay', 'Queda de Chamadas'],
        'SOLUÇÃO': ['Reiniciar Rota SIP', 'Check QoS Roteador']
    })
    st.table(diag_tel)

# --- FOOTER ---
st.markdown(f"--- \n **SISTEMA V111 ATIVO** | {datetime.now().strftime('%H:%M')} | STAKE: **1 Real**")
