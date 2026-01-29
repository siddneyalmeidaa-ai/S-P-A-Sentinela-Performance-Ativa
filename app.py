import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. CONFIGURAÇÃO DE INTERFACE E PADRÃO OURO ---
st.set_page_config(page_title="S.P.A. MASTER - SIDNEY ALMEIDA", layout="wide", page_icon="🛰️")

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display:none;}
    .manifesto-container {
        background-color: #050505;
        border-left: 5px solid #00FF41;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 25px;
    }
    .quote-text { color: #00FF41; font-size: 20px; font-weight: bold; font-style: italic; }
    .signature { color: #D4AF37; font-size: 12px; text-transform: uppercase; letter-spacing: 2px; }
    </style>
""", unsafe_allow_html=True)

# --- 2. BANCO DE DADOS INTEGRAL (QUANTUM MEMORY) ---
if 'db' not in st.session_state:
    st.session_state.db = {
        "OPERAÇÃO": {
            "ANA (PERFORMANCE)": {"VALOR": 45800.0, "PROJ": 91600.0, "STATUS": "85% LIBERADO", "LOG_TIME": "06:12:00", "PROD": 92, "LEGAL": "Art. 444 CLT"},
            "MARCOS (SABOTAGEM)": {"VALOR": 0.0, "PROJ": 0.0, "STATUS": "0% BLOQUEADO", "LOG_TIME": "04:30:00", "PROD": 0, "LEGAL": "Art. 482 CLT"},
            "RICARDO (OMISSÃO)": {"VALOR": 150.0, "PROJ": 300.0, "STATUS": "0% BLOQUEADO", "LOG_TIME": "05:15:00", "PROD": 5, "LEGAL": "Art. 482 CLT"},
            "JULIA (VÁCUO)": {"VALOR": 800.0, "PROJ": 1600.0, "STATUS": "0% BLOQUEADO", "LOG_TIME": "02:20:00", "PROD": 12, "LEGAL": "Art. 482 CLT"}
        },
        "DISCADOR": {"PEN": 65, "SPC": 15},
        "TELEFONIA": {"LAT": 250, "STATUS": "CRÍTICO"}
    }

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

# --- 3. CABEÇALHO DO COMANDO ---
st.markdown(f"""
    <div class="manifesto-container">
        <div class="quote-text">"Enquanto o mundo olha para o avião que sobe, eu governo o código que o faz voar."</div>
        <div class="signature">👊🚀📊⚖️🏁💎 — COMANDANTE SIDNEY ALMEIDA</div>
    </div>
""", unsafe_allow_html=True)

# --- 4. INTERFACE DE 6 ABAS ---
aba1, aba2, aba3, aba4, aba5, aba6 = st.tabs([
    "👑 01. VISÃO ESTRATÉGICA", 
    "👥 02. GESTÃO DE OPERADORES", 
    "🧠 03. INTELIGÊNCIA MAILING", 
    "📡 04. INFRA TELEFONIA",
    "📂 05. CENTRAL DE RELATÓRIOS",
    "⚖️ 06. VISÃO JURÍDICA"
])

with aba1:
    st.header("📊 Cockpit Consolidado")
    c1, c2, c3 = st.columns(3)
    c1.metric("📡 REDE", f"{st.session_state.db['TELEFONIA']['LAT']}ms", "LATÊNCIA")
    c2.metric("🧠 IPI", f"{st.session_state.db['DISCADOR']['PEN']}%", "PENETRAÇÃO")
    c3.metric("👥 ALERTA", "3 BLOQUEIOS", "SABOTAGEM", delta_color="inverse")
    st.dataframe(df_audit.style.format({"VALOR REAL": "R$ {:,.2f}", "PROJEÇÃO": "R$ {:,.2f}", "X (-50%)": "R$ {:,.2f}"}), use_container_width=True)

with aba2:
    st.header("👥 Auditoria de Comportamento (Operador)")
    op = st.selectbox("Selecione para análise profunda:", df_audit["OPERADOR"].tolist())
    
    col_x, col_y, col_z = st.columns(3)
    # Lógica de detecção de Omissão/Sabotagem integrada aqui
    prod_real = st.session_state.db['OPERAÇÃO'][op]['PROD']
    alert_color = "normal" if prod_real > 50 else "inverse"
    
    col_x.metric("Tempo Logado", st.session_state.db['OPERAÇÃO'][op]['LOG_TIME'])
    col_y.metric("Eficiência Real", f"{prod_real}%", delta="- OMISSÃO" if prod_real < 10 else "OK", delta_color=alert_color)
    col_z.metric("Recuperado", f"R$ {st.session_state.db['OPERAÇÃO'][op]['VALOR']:,.2f}")
    
    if prod_real < 10:
        st.error(f"⚠️ ALERTA DE SABOTAGEM: Operador {op} logado há mais de 2h com produção próxima a zero.")

with aba3:
    st.header("🧠 Inteligência de Mailing")
    st.write("Foco em Penetração de Leads e Estratégia de Discagem.")
    st.progress(st.session_state.db['DISCADOR']['PEN'])

with aba4:
    st.header("📡 Infraestrutura")
    st.warning("Servidor Vivo - Latência Crítica detectada.")

with aba5:
    st.header("📂 Exportação de Dossiê")
    html_f = f"<html><meta charset='utf-8'><body><h2>RELATÓRIO S.A.</h2>{df_audit.to_html(index=False)}</body></html>"
    st.download_button("📥 BAIXAR DOSSIÊ", html_f.encode('utf-8-sig'), "RELATORIO_SA.html", "text/html")

with aba6:
    st.header("⚖️ Visão Jurídica (CLT)")
    st.table(df_audit[df_audit["VALOR REAL"] == 0][["OPERADOR", "LEGAL", "STATUS"]])
    
