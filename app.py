import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. CONFIGURAÇÃO E BLINDAGEM DE ESTILO ---
st.set_page_config(page_title="S.P.A. MASTER - SIDNEY ALMEIDA", layout="wide", page_icon="🛰️")

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;} header {visibility: hidden;} footer {visibility: hidden;}
    .stDeployButton {display:none;}
    .manifesto-container {
        background-color: #050505; border-left: 5px solid #00FF41;
        padding: 20px; border-radius: 10px; margin-bottom: 25px;
    }
    .quote-text { color: #00FF41; font-size: 18px; font-weight: bold; font-style: italic; }
    .signature { color: #D4AF37; font-size: 12px; text-transform: uppercase; letter-spacing: 2px; }
    </style>
""", unsafe_allow_html=True)

# --- 2. BANCO DE DADOS INTEGRAL (CORREÇÃO DE TODOS OS PRINTS DE ERRO) ---
if 'db' not in st.session_state:
    st.session_state.db = {
        "OPERAÇÃO": {
            "ANA (PERFORMANCE)": {
                "VALOR_REAL": 45800.0, "PROJ": 91600.0, "VALOR_NEGOCIADO": 125400.0,
                "STATUS": "85% LIBERADO", "MINUTOS_PAUSA": 40, "DISCADAS": 1200, 
                "ALO": 450, "CPC": 120, "CPCA": 95, "PROMESSAS_N": 70,
                "P1": "00:10:00", "P2": "00:10:00", "LANCHE": "00:20:00", "BANHEIRO": "00:00:00"
            },
            "MARCOS (SABOTAGEM)": {
                "VALOR_REAL": 0.0, "PROJ": 0.0, "VALOR_NEGOCIADO": 0.0,
                "STATUS": "0% BLOQUEADO", "MINUTOS_PAUSA": 125, "DISCADAS": 800, 
                "ALO": 12, "CPC": 0, "CPCA": 0, "PROMESSAS_N": 0,
                "P1": "00:25:00", "P2": "00:30:00", "LANCHE": "01:00:00", "BANHEIRO": "00:30:00"
            }
        },
        "DISCADOR": {"PEN": 65, "MAILING": "Ativo 2026", "TOTAL_DISCADAS": 2500},
        "TELEFONIA": {"LAT": 250, "STATUS": "CRÍTICO", "SERVER": "Vivo Cloud"}
    }

# --- 3. LÓGICA DE AUDITORIA (X -50%) ---
df_list = []
for k, v in st.session_state.db["OPERAÇÃO"].items():
    alo = v.get("ALO", 0)
    disc = v.get("DISCADAS", 1)
    df_list.append({
        "OPERADOR": k,
        "LOC %": (alo / disc * 100),
        "CPCA": v.get("CPCA", 0),
        "NEGOCIADO": v.get("VALOR_NEGOCIADO", 0.0),
        "REAL": v.get("VALOR_REAL", 0.0),
        "PROJEÇÃO": v.get("PROJ", 0.0),
        "X (-50%)": v.get("PROJ", 0.0) * 0.5,
        "STATUS": v.get("STATUS", "PENDENTE"),
        "MINUTOS": v.get("MINUTOS_PAUSA", 0)
    })
df_audit = pd.DataFrame(df_list)

# --- 4. INTERFACE DE COMANDO ---
st.markdown(f"""
    <div class="manifesto-container">
        <div class="quote-text">"Enquanto o mundo olha para o avião que sobe, eu governo o código que o faz voar."</div>
        <div class="signature">👊🚀📊⚖️🏁💎 — Comandante S.A.</div>
    </div>
""", unsafe_allow_html=True)

st.title("🛰️ S.P.A. - SENTINELA DE PERFORMANCE ATIVA")

aba1, aba2, aba3, aba4, aba5, aba6 = st.tabs([
    "👑 01. COCKPIT", "👥 02. GESTÃO", "🧠 03. DISCADOR", "📡 04. TELEFONIA", "📂 05. RELATÓRIOS", "⚖️ 06. JURÍDICO"
])

with aba1:
    st.header("📊 Cockpit Consolidado")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Localização Geral", f"{(df_audit['REAL'].count()):.1f}%", "EFICÁCIA")
    m2.metric("Contatos (CPCA)", f"{int(df_audit['CPCA'].sum())}", "MÃO NA MASSA")
    m3.metric("Financeiro Real", f"R$ {df_audit['REAL'].sum():,.2f}")
    m4.metric("Pausa Equipe", f"{df_audit['MINUTOS'].sum()} min", delta_color="inverse")

    st.subheader("🏁 Tabela da Favelinha")
    st.dataframe(df_audit.style.format({
        "REAL": "R$ {:,.2f}", "PROJEÇÃO": "R$ {:,.2f}", "X (-50%)": "R$ {:,.2f}", "NEGOCIADO": "R$ {:,.2f}", "LOC %": "{:.1f}%"
    }), use_container_width=True)

with aba2:
    st.header("👥 Detalhamento")
    op = st.selectbox("Selecione:", df_audit["OPERADOR"].tolist())
    res = df_audit[df_audit["OPERADOR"] == op].iloc[0]
    st.metric("CPCA Individual", int(res["CPCA"]))
    st.metric("Valor Negociado", f"R$ {res['NEGOCIADO']:,.2f}")

with aba5:
    csv = df_audit.to_csv(index=False).encode('utf-8-sig')
    st.download_button("📥 EXPORTAR AUDITORIA V52", csv, "S_A_SPA_V52.csv", "text/csv")
    
