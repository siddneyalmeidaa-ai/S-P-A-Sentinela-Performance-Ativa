import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. CONFIGURAÇÃO E BLINDAGEM ---
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

# --- 2. BANCO DE DADOS INTEGRAL (PADRÃO OURO) ---
if 'db' not in st.session_state:
    st.session_state.db = {
        "OPERAÇÃO": {
            "ANA (PERFORMANCE)": {
                "VALOR_REAL": 46600.0, "PROJ": 93200.0, "VALOR_NEGOCIADO": 125400.0,
                "STATUS": "85% LIBERADO", "MINUTOS_PAUSA": 40, "DISCADAS": 1200, 
                "ALO": 450, "CPC": 120, "CPCA": 95, "PROMESSAS_N": 70,
                "P1": "00:10:00", "P2": "00:10:00", "LANCHE": "00:20:00", "BANHEIRO": "00:00:00"
            },
            "MARCOS (SABOTAGEM)": {
                "VALOR_REAL": 0.0, "PROJ": 0.0, "VALOR_NEGOCIADO": 0.0,
                "STATUS": "0% PENDENTE", "MINUTOS_PAUSA": 125, "DISCADAS": 800, 
                "ALO": 12, "CPC": 0, "CPCA": 0, "PROMESSAS_N": 0,
                "P1": "00:25:00", "P2": "00:30:00", "LANCHE": "01:00:00", "BANHEIRO": "00:30:00"
            },
            "JULIA (VÁCUO)": {
                "VALOR_REAL": 800.0, "PROJ": 1600.0, "VALOR_NEGOCIADO": 2500.0,
                "STATUS": "12% PENDENTE", "MINUTOS_PAUSA": 55, "DISCADAS": 500, 
                "ALO": 85, "CPC": 8, "CPCA": 4, "PROMESSAS_N": 1,
                "P1": "00:10:00", "P2": "00:10:00", "LANCHE": "00:20:00", "BANHEIRO": "00:15:00"
            }
        },
        "DISCADOR": {"PEN": 65, "MAILING": "Ativo 2026", "TOTAL_DISCADAS": 2500},
        "TELEFONIA": {"LAT": 250, "STATUS": "CRÍTICO", "SERVER": "Vivo Cloud"}
    }

# --- 3. PROCESSAMENTO (X = PROJEÇÃO - 50%) ---
df_list = []
for k, v in st.session_state.db["OPERAÇÃO"].items():
    alo = v.get("ALO", 0)
    disc = v.get("DISCADAS", 1)
    proj = v.get("PROJ", 0.0)
    df_list.append({
        "OPERADOR": k,
        "LOC %": (alo / disc * 100),
        "CPCA": v.get("CPCA", 0),
        "NEGOCIADO": v.get("VALOR_NEGOCIADO", 0.0),
        "REAL": v.get("VALOR_REAL", 0.0),
        "PROJEÇÃO": proj,
        "X (-50%)": proj * 0.5,
        "STATUS": v.get("STATUS", "PENDENTE"),
        "MINUTOS": v.get("MINUTOS_PAUSA", 0)
    })
df_audit = pd.DataFrame(df_list)

# --- 4. CABEÇALHO ---
st.markdown(f"""
    <div class="manifesto-container">
        <div class="quote-text">"Enquanto o mundo olha para o avião que sobe, eu governo o código que o faz voar."</div>
        <div class="signature">👊🚀📊⚖️🏁💎 — Comandante S.A.</div>
    </div>
""", unsafe_allow_html=True)

st.title("🛰️ S.P.A. - SENTINELA DE PERFORMANCE ATIVA")
st.write(f"**CONSOLIDE 01-06** | SISTEMA SINCRONIZADO | {datetime.now().strftime('%H:%M:%S')}")

aba1, aba2, aba3, aba4, aba5, aba6 = st.tabs([
    "👑 01. COCKPIT", "👥 02. GESTÃO", "🧠 03. DISCADOR", 
    "📡 04. TELEFONIA", "📂 05. RELATÓRIOS", "⚖️ 06. JURÍDICO"
])

# --- ABA 01: COCKPIT (AGORA COM DISCADOR E TELEFONIA INTEGRADOS) ---
with aba1:
    st.header("📊 Cockpit Consolidado de Comando")
    
    # Linha 1: Financeiro e Operação
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Localização Geral", f"{(df_audit['LOC %'].mean()):.1f}%", "EFICÁCIA")
    col2.metric("Contatos (CPCA)", f"{int(df_audit['CPCA'].sum())}", "MÃO NA MASSA")
    col3.metric("Financeiro Real", f"R$ {df_audit['REAL'].sum():,.2f}")
    col4.metric("Pausa Coletiva", f"{df_audit['MINUTOS'].sum()} min", delta_color="inverse")

    # Linha 2: Discador e Telefonia (AQUI ESTÁ A INFORMAÇÃO QUE FALTAVA)
    st.divider()
    st.subheader("🧠 Status de Infraestrutura (Discador & Rede)")
    d1, d2, d3 = st.columns(3)
    d1.metric("IPI (Discador)", f"{st.session_state.db['DISCADOR']['PEN']}%", "PADRÃO OURO")
    d2.metric("Latência Rede", f"{st.session_state.db['TELEFONIA']['LAT']}ms", delta="CRÍTICO", delta_color="inverse")
    d3.metric("Mailing", st.session_state.db['DISCADOR']['MAILING'])

    st.divider()
    st.subheader("🏁 Tabela da Favelinha")
    st.dataframe(df_audit[["OPERADOR", "LOC %", "CPCA", "NEGOCIADO", "REAL", "PROJEÇÃO", "X (-50%)", "STATUS"]].style.format({
        "REAL": "R$ {:,.2f}", "PROJEÇÃO": "R$ {:,.2f}", "X (-50%)":
    
