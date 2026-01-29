import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. CONFIGURAÇÃO DE INTERFACE E OCULTAÇÃO DE MENUS (PADRÃO OURO) ---
st.set_page_config(page_title="S.P.A. MASTER - SIDNEY ALMEIDA", layout="wide", page_icon="🛰️")

# Injeção de CSS para ocultar menus e estilizar o Manifesto S.A.
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display:none;}
    
    /* Estilização do Bloco Autoral S.A. */
    .manifesto-container {
        background-color: #050505;
        border-left: 5px solid #00FF41;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 25px;
    }
    .quote-text {
        color: #00FF41;
        font-size: 20px;
        font-weight: bold;
        font-style: italic;
    }
    .signature {
        color: #D4AF37;
        font-size: 12px;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    </style>
""", unsafe_allow_html=True)

# --- 2. BANCO DE DADOS INTEGRAL (QUANTUM MEMORY) ---
if 'db' not in st.session_state:
    st.session_state.db = {
        "OPERAÇÃO": {
            "ANA (PERFORMANCE)": {
                "VALOR": 45800.0, "PROJ": 91600.0, "STATUS": "85% LIBERADO", "LEGAL": "Art. 444 CLT",
                "LOG_TIME": "06:12:00", "PROD": 92, "QTD_PAUSAS": 3, "TOTAL_PAUSAS": "00:40:00"
            },
            "MARCOS (SABOTAGEM)": {
                "VALOR": 0.0, "PROJ": 0.0, "STATUS": "0% BLOQUEADO", "LEGAL": "Art. 482 CLT",
                "LOG_TIME": "04:30:00", "PROD": 0, "QTD_PAUSAS": 12, "TOTAL_PAUSAS": "02:15:00"
            },
            "RICARDO (OMISSÃO)": {
                "VALOR": 150.0, "PROJ": 300.0, "STATUS": "0% BLOQUEADO", "LEGAL": "Art. 482 CLT",
                "LOG_TIME": "05:15:00", "PROD": 5, "QTD_PAUSAS": 8, "TOTAL_PAUSAS": "01:10:00"
            },
            "JULIA (VÁCUO)": {
                "VALOR": 800.0, "PROJ": 1600.0, "STATUS": "0% BLOQUEADO", "LEGAL": "Art. 482 CLT",
                "LOG_TIME": "02:20:00", "PROD": 12, "QTD_PAUSAS": 5, "TOTAL_PAUSAS": "00:45:00"
            }
        },
        "DISCADOR": {"PEN": 65, "SPC": 15},
        "TELEFONIA": {"LAT": 250, "STATUS": "CRÍTICO"}
    }

# Lógica da Tabela da Favelinha (Regra do X -50% da Projeção)
df_audit = pd.DataFrame([
    {
        "OPERADOR": k, 
        "VALOR REAL": v['VALOR'],
        "PROJEÇÃO": v['PROJ'],
        "X (-50%)": v['PROJ'] * 0.5, 
        "STATUS": v["STATUS"],
        "LEGAL": v["LEGAL"]
    }
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
st.write(f"**COMANDANTE SIDNEY ALMEIDA** | Console Consolidado | {datetime.now().strftime('%H:%M:%S')}")

# --- 4. INTERFACE DE 6 ABAS (FIXAS - CONFORME PADRÃO OURO) ---
aba1, aba2, aba3, aba4, aba5, aba6 = st.tabs([
    "👑 01. VISÃO ESTRATÉGICA", 
    "👥 02. GESTÃO DE OPERADORES", 
    "🧠 03. ESTRATÉGIA DE DISCADOR", 
    "📡 04. INFRA TELEFONIA",
    "📂 05. CENTRAL DE RELATÓRIOS",
    "⚖️ 06. VISÃO JURÍDICA"
])

# --- ABA 01: VISÃO ESTRATÉGICA ---
with aba1:
    st.header("📊 Cockpit Consolidado (Painel de Comando)")
    col1, col2, col3 = st.columns(3)
    col1.metric("📡 REDE VIVO", f"{st.session_state.db['TELEFONIA']['LAT']}ms", "CRÍTICO", delta_color="inverse")
    col2.metric("🧠 IPI DISCADOR", f"{st.session_state.db['DISCADOR']['PEN']}%", f"{st.session_state.db['DISCADOR']['SPC']}% SPC")
    col3.metric("👥 STATUS RH", "3 BLOQUEADOS", "SABOTAGEM", delta_color="inverse")
    st.divider()
    st.subheader("🏁 Tabela da Favelinha - Auditoria de X")
    st.dataframe(df_audit.style.format({
        "VALOR REAL": "R$ {:,.2f}", 
        "PROJEÇÃO": "R$ {:,.2f}", 
        "X (-50%)": "R$ {:,.2f}"
    }), use_container_width=True)

# --- ABA 02: GESTÃO DE OPERADORES (COM PAUSAS) ---
with aba2:
    st.header("👥 Auditoria de Comportamento e Frequência de Pausas")
    op = st.selectbox("Selecione o Operador para Auditoria:", list(st.session_state.db["OPERAÇÃO"].keys()), key="fix_aba2")
    data = st.session_state.db["OPERAÇÃO"][op]
    
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Tempo Logado", data["LOG_TIME"])
    c2.metric("Qtd. Total de Pausas", f"{data['QTD_PAUSAS']}x")
    c3.metric("Tempo Acumulado", data["TOTAL_PAUSAS"], delta="EXCESSO" if data['QTD_PAUSAS'] > 8 else None, delta_color="inverse")
    c4.metric("Eficiência Real", f"{data['PROD']}%")
    
    st.divider()
    if data['QTD_PAUSAS'] > 10 or data['PROD'] < 10:
        st.error(f"🚨 ALERTA CRÍTICO: Operador {op} em padrão de Sabotagem ou Omissão detectado.")
    else:
        st.success(f"✔️ Operador {op} operando dentro dos parâmetros aceitáveis.")

# --- ABA 03: ESTRATÉGIA DE DISCADOR ---
with aba3:
    st.header("🧠 Inteligência de Mailing")
    st.write("Monitoramento de penetração e comportamento de discagem.")
    st.progress(st.session_state.db['DISCADOR']['PEN'], text=f"Penetração Ativa: {st.session_state.db['DISCADOR']['PEN']}%")

# --- ABA 04: INFRA TELEFONIA ---
with aba4:
    st.header("📡 Infraestrutura de Telefonia")
    st.error(f"ALERTA: Latência de {st.session_state.db['TELEFONIA']['LAT']}ms detectada no servidor VIVO.")
    st.info(f"Status Atual do Link: {st.session_state.db['TELEFONIA']['STATUS']}")

# --- ABA 05: CENTRAL DE RELATÓRIOS ---
with aba5:
    st.header("📂 Exportação Blindada (HTML)")
    # Formato seguro para evitar erros de acento no celular
    html_f = f"<html><meta charset='utf-8'><body><h2>DOSSIÊ JURÍDICO - S.A.</h2>{df_audit.to_html(index=False)}</body></html>"
    st.download_button("📥 BAIXAR DOSSIÊ (MOBILE READY)", html_f.encode('utf-8-sig'), "RELATORIO_SA.html", "text/html")

# --- ABA 06: VISÃO JURÍDICA ---
with aba6:
    st.header("⚖️ Auditoria Jurídica (CLT)")
    st.warning("Relatório focado em provas de Omissão e Sabotagem para Justa Causa.")
    st.table(df_audit[df_audit["X (-50%)"] == 0 or df_audit["LEGAL"] == "Art. 482 CLT"][["OPERADOR", "LEGAL", "STATUS"]])
