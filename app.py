import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. CONFIGURAÇÃO DE INTERFACE (PADRÃO OURO S.A.) ---
st.set_page_config(page_title="S.P.A. MASTER - SIDNEY ALMEIDA", layout="wide", page_icon="🛰️")

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;} header {visibility: hidden;} footer {visibility: hidden;}
    .stDeployButton {display:none;}
    .manifesto-container {
        background-color: #050505;
        border-left: 5px solid #00FF41;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 25px;
    }
    .quote-text { color: #00FF41; font-size: 18px; font-weight: bold; font-style: italic; }
    .signature { color: #D4AF37; font-size: 12px; text-transform: uppercase; letter-spacing: 2px; }
    </style>
""", unsafe_allow_html=True)

# --- 2. BANCO DE DADOS INTEGRAL (QUANTUM MEMORY) - CORREÇÃO DEFINITIVA ---
if 'db' not in st.session_state:
    st.session_state.db = {
        "OPERAÇÃO": {
            "ANA (PERFORMANCE)": {
                "VALOR": 45800.0, "PROJ": 91600.0, "STATUS": "85% LIBERADO", "LEGAL": "Art. 444 CLT",
                "LOG_TIME": "06:12:00", "PROD": 92, "QTD_PAUSAS": 3, 
                "P1": "00:10:00", "P2": "00:10:00", "LANCHE": "00:20:00", "BANHEIRO": "00:05:00", "TOTAL_PAUSAS": "00:45:00"
            },
            "MARCOS (SABOTAGEM)": {
                "VALOR": 0.0, "PROJ": 0.0, "STATUS": "0% BLOQUEADO", "LEGAL": "Art. 482 CLT",
                "LOG_TIME": "04:30:00", "PROD": 0, "QTD_PAUSAS": 15, 
                "P1": "00:25:00", "P2": "00:30:00", "LANCHE": "01:00:00", "BANHEIRO": "01:10:00", "TOTAL_PAUSAS": "03:05:00"
            },
            "RICARDO (OMISSÃO)": {
                "VALOR": 150.0, "PROJ": 300.0, "STATUS": "0% BLOQUEADO", "LEGAL": "Art. 482 CLT",
                "LOG_TIME": "05:15:00", "PROD": 5, "QTD_PAUSAS": 8, 
                "P1": "00:15:00", "P2": "00:15:00", "LANCHE": "00:30:00", "BANHEIRO": "00:10:00", "TOTAL_PAUSAS": "01:10:00"
            },
            "JULIA (VÁCUO)": {
                "VALOR": 800.0, "PROJ": 1600.0, "STATUS": "0% BLOQUEADO", "LEGAL": "Art. 482 CLT",
                "LOG_TIME": "02:20:00", "PROD": 12, "QTD_PAUSAS": 6, 
                "P1": "00:10:00", "P2": "00:10:00", "LANCHE": "00:20:00", "BANHEIRO": "00:15:00", "TOTAL_PAUSAS": "00:55:00"
            }
        },
        "DISCADOR": {"PEN": 65, "SPC": 15, "MAILING": "Ativo 2026"},
        "TELEFONIA": {"LAT": 250, "STATUS": "CRÍTICO", "SERVER": "Vivo Cloud"}
    }

df_audit = pd.DataFrame([
    {"OPERADOR": k, "VALOR REAL": v['VALOR'], "PROJEÇÃO": v['PROJ'], "X (-50%)": v['PROJ'] * 0.5, "STATUS": v["STATUS"], "LEGAL": v["LEGAL"]}
    for k, v in st.session_state.db["OPERAÇÃO"].items()
])

# --- 3. CABEÇALHO COM MANIFESTO AUTORAL S.A. ---
st.markdown(f"""
    <div class="manifesto-container">
        <div class="quote-text">"Enquanto o mundo olha para o avião que sobe, eu governo o código que o faz voar."</div>
        <div class="signature">👊🚀📊⚖️🏁💎 — Frase autoral: Comandante S.A.</div>
    </div>
""", unsafe_allow_html=True)

st.title("🛰️ S.P.A. - SENTINELA DE PERFORMANCE ATIVA")
st.write(f"**CONSOLIDE 01-06** | SISTEMA SINCRONIZADO | {datetime.now().strftime('%H:%M:%S')}")

# --- 4. INTERFACE DE 6 ABAS ---
aba1, aba2, aba3, aba4, aba5, aba6 = st.tabs([
    "👑 01. VISÃO ESTRATÉGICA", "👥 02. GESTÃO DE OPERADORES", "🧠 03. ESTRATÉGIA DE DISCADOR", 
    "📡 04. INFRA TELEFONIA", "📂 05. CENTRAL DE RELATÓRIOS", "⚖️ 06. VISÃO JURÍDICA"
])

# --- ABA 01: VISÃO ESTRATÉGICA (O CONSOLIDADO) ---
with aba1:
    st.header("📊 Cockpit Consolidado (Resumo Geral)")
    
    # Resumo das 6 frentes em métricas rápidas
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Rede (Aba 04)", f"{st.session_state.db['TELEFONIA']['LAT']}ms", "CRÍTICO")
    m2.metric("IPI (Aba 03)", f"{st.session_state.db['DISCADOR']['PEN']}%", "PENETRAÇÃO")
    m3.metric("Omissão (Aba 02)", "3 Casos", "ALERTA RH")
    m4.metric("Financeiro (Aba 01)", f"R$ {df_audit['VALOR REAL'].sum():,.2f}", "TOTAL RECUPERADO")

    st.divider()
    st.subheader("🏁 Tabela da Favelinha - Auditoria de X (-50%)")
    st.dataframe(df_audit.style.format({"VALOR REAL": "R$ {:,.2f}", "PROJEÇÃO": "R$ {:,.2f}", "X (-50%)": "R$ {:,.2f}"}), use_container_width=True)

# --- ABA 02: GESTÃO DE OPERADORES (DETALHE COMPORTAMENTAL) ---
with aba2:
    st.header("👥 Auditoria de Comportamento e Pausas")
    op = st.selectbox("Selecione para análise profunda:", list(st.session_state.db["OPERAÇÃO"].keys()), key="sel_op_v29")
    data = st.session_state.db["OPERAÇÃO"][op]
    
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Logado", data["LOG_TIME"])
    c2.metric("Pausas", f"{data['QTD_PAUSAS']}x")
    c3.metric("Total Pausas", data["TOTAL_PAUSAS"])
    c4.metric("Eficiência", f"{data['PROD']}%")
    
    st.divider()
    st.subheader("🛰️ Anatomia das Pausas")
    p1, p2, p3, p4 = st.columns(4)
    p1.info(f"P1 (NR17): {data['P1']}")
    p2.info(f"P2 (NR17): {data['P2']}")
    p3.success(f"Lanche: {data['LANCHE']}")
    p4.warning(f"Banheiro: {data['BANHEIRO']}")

# --- ABA 03: ESTRATÉGIA DE DISCADOR ---
with aba3:
    st.header("🧠 Inteligência de Mailing")
    st.write(f"Status do Mailing: **{st.session_state.db['DISCADOR']['MAILING']}**")
    st.progress(st.session_state.db['DISCADOR']['PEN'])

# --- ABA 04: INFRA TELEFONIA ---
with aba4:
    st.header("📡 Infraestrutura de Telefonia")
    st.error(f"Servidor: {st.session_state.db['TELEFONIA']['SERVER']} | Latência: {st.session_state.db['TELEFONIA']['LAT']}ms")

# --- ABA 05: CENTRAL DE RELATÓRIOS ---
with aba5:
    st.header("📂 Exportação de Dossiê Jurídico")
    html_f = f"<html><meta charset='utf-8'><body><h2>S.A. CONSOLIDE</h2>{df_audit.to_html()}</body></html>"
    st.download_button("📥 BAIXAR HTML (AUDITORIA)", html_f.encode('utf-8-sig'), "RELATORIO_SA.html", "text/html")

# --- ABA 06: VISÃO JURÍDICA ---
with aba6:
    st.header("⚖️ Auditoria Jurídica")
    st.table(df_audit[["OPERADOR", "LEGAL", "STATUS"]])
    
