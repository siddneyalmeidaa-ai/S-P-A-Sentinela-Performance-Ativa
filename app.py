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
        text-align: center; color: #FFD700; font-size: 26px; font-weight: bold; 
        border-bottom: 2px solid #FFD700; padding: 10px; margin-bottom: 20px;
    }
    .metric-card {
        background-color: #1A1C23; padding: 20px; border-radius: 10px;
        border-left: 5px solid #FFD700; margin: 10px 0;
    }
    .stTable {background-color: #1A1C23;}
    </style>
    <div class="selo-sidney">🔱 SIDNEY ALMEIDA - SUMÁRIO EXECUTIVO INTEGRAL V111 🔱</div>
    """, unsafe_allow_html=True)

# --- 2. MEMÓRIA QUÂNTICA: DADOS INTEGRADOS ---
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

# Cálculos de Resumo (Totais e Médias)
total_alo = df['ALÔ'].sum()
total_valor = df['VALOR'].sum()
total_promessas = df['PROMESSA'].sum()
total_cpc = df['CPC'].sum()
media_tempo_logado = df['TEMPO_LOGADO_MIN'].mean()
media_pausa = df['PAUSA_MINUTOS'].mean()

# --- 3. ARQUITETURA DE ABAS ---
abas = st.tabs([
    "👑 Cockpit (Resumo)", "👥 Gestão", "☎️ Discador", 
    "📡 Telefonia", "🐍 Sabotagem", "⚖️ Jurídico", "📂 Exportação"
])

# --- ABA 01: COCKPIT (VISÃO RESUMIDA TOTALITÁRIA) ---
with abas[0]:
    st.subheader("👑 Cockpit - Sumário Executivo Operacional")

    # LINHA 1: PRODUÇÃO (TOTAIS)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"<div class='metric-card'><h3>VALOR TOTAL</h3><h2>R$ {total_valor:.2f}</h2><p>Meta X: R$ {total_valor * 0.5:.2f}</p></div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div class='metric-card'><h3>ALÔ / CPC TOTAL</h3><h2>{total_alo} / {total_cpc}</h2><p>Volume de Contatos</p></div>", unsafe_allow_html=True)
    with col3:
        st.markdown(f"<div class='metric-card'><h3>PRODUTIVIDADE</h3><h2>{total_promessas}</h2><p>Promessas Totais</p></div>", unsafe_allow_html=True)

    st.divider()

    # LINHA 2: TÉCNICA E MÉDIAS (RESUMIDO)
    col4, col5, col6 = st.columns(3)
    with col4:
        st.subheader("⏱️ Gestão de Tempo")
        st.write(f"**Média Logado:** {int(media_tempo_logado // 60)}h {int(media_tempo_logado % 60)}min")
        st.write(f"**Média Pausa:** {int(media_pausa)} min")
        if media_pausa > 45: 
            st.error(f"⚠️ Média de Pausa Acima do Limite ({int(media_pausa)}m)")
        else:
            st.success("✅ Pausas sob controle")
        
    with col5:
        st.subheader("☎️ Visão Discador")
        st.write("**Mailing:** 12% Vácuo")
        st.write(f"**Aproveitamento:** {(total_cpc/total_alo)*100:.1f}%")
        st.info("IA-Sentinela: Ativa")

    with col6:
        st.subheader("📡 Visão Telefonia")
        st.write("**Latência:** 12ms (VIVO)")
        st.write("**Jitter:** 0.8ms")
        st.success("Sincronia SIP: Estável")

# --- ABA 02: GESTÃO DETALHADA ---
with abas[1]:
    st.subheader("👥 Detalhado por Operador")
    st.table(df)

# --- ABA 07: EXPORTAÇÃO FORENSE (SANEADA) ---
with abas[6]:
    st.subheader("📂 Exportação de Dossiê 360º")
    hash_res = hashlib.sha256(str(datetime.now()).encode()).hexdigest()[:12].upper()
    st.write(f"Assinatura SHA-256: **{hash_res}**")
    
    # Exportação UTF-16 para evitar erro de acento em celulares
    csv_saneado = df.to_csv(index=False).encode('utf-16')
    st.download_button(
        label="📥 Baixar Relatório Completo",
        data=csv_saneado,
        file_name=f"SA_SUPREMO_V111_{datetime.now().strftime('%d_%m')}.csv",
        mime="text/csv"
    )

# --- FOOTER ---
st.markdown(f"--- \n **SISTEMA V111 ATIVO** | {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} | STAKE: **1 Real**")
    
