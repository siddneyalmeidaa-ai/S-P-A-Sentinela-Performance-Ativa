import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. CONFIGURAÇÃO DE INTERFACE E OCULTAÇÃO DE MENUS ---
st.set_page_config(page_title="S.P.A. MASTER - SIDNEY ALMEIDA", layout="wide", page_icon="🛰️")

# Injeção de CSS para ocultar a parte de cima (MainMenu e Header) e o rodapé
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display:none;}
    /* Forçar abas a ocuparem a largura total e serem visíveis */
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    </style>
""", unsafe_allow_html=True)

# --- 2. BANCO DE DADOS INTEGRAL (QUANTUM MEMORY) ---
if 'db' not in st.session_state:
    st.session_state.db = {
        "OPERAÇÃO": {
            "ANA (PERFORMANCE)": {"VALOR": 45800.0, "PROJ": 91600.0, "STATUS": "LIBERADO", "LEGAL": "Art. 444 CLT"},
            "MARCOS (SABOTAGEM)": {"VALOR": 0.0, "PROJ": 0.0, "STATUS": "BLOQUEADO", "LEGAL": "Art. 482 CLT"},
            "RICARDO (OMISSÃO)": {"VALOR": 150.0, "PROJ": 300.0, "STATUS": "BLOQUEADO", "LEGAL": "Art. 482 CLT"},
            "JULIA (VÁCUO)": {"VALOR": 800.0, "PROJ": 1600.0, "STATUS": "BLOQUEADO", "LEGAL": "Art. 482 CLT"}
        },
        "DISCADOR": {"PEN": 65, "SPC": 15},
        "TELEFONIA": {"LAT": 250, "STATUS": "CRÍTICO"}
    }

# Lógica da Tabela da Favelinha (Regra do X -50%)
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
st.title("🛰️ S.P.A. - SENTINELA DE PERFORMANCE ATIVA")
st.write(f"**COMANDANTE SIDNEY ALMEIDA** | Console Consolidado 01-06")

# --- 4. INTERFACE DE 6 ABAS (FIXAS - NÃO PODEM SUMIR) ---
# A lista explícita abaixo garante que o Streamlit renderize todas as 6 posições.
aba1, aba2, aba3, aba4, aba5, aba6 = st.tabs([
    "👑 01. VISÃO ESTRATÉGICA", 
    "👥 02. GESTÃO DE OPERADORES", 
    "🧠 03. ESTRATÉGIA DE DISCADOR", 
    "📡 04. INFRA TELEFONIA",
    "📂 05. CENTRAL DE RELATÓRIOS",
    "⚖️ 06. VISÃO JURÍDICA"
])

# --- CONTEÚDO OBRIGATÓRIO EM CADA ABA ---

with aba1:
    st.header("📊 Cockpit Consolidado (Painel de Comando)")
    col1, col2, col3 = st.columns(3)
    col1.metric("📡 REDE VIVO", f"{st.session_state.db['TELEFONIA']['LAT']}ms", "CRÍTICO", delta_color="inverse")
    col2.metric("🧠 DISCADOR", f"{st.session_state.db['DISCADOR']['PEN']}%", f"{st.session_state.db['DISCADOR']['SPC']}% SPC")
    col3.metric("👥 STATUS RH", "3 BLOQUEADOS", "SABOTAGEM", delta_color="inverse")
    st.divider()
    st.dataframe(df_audit.style.format({"VALOR REAL": "R$ {:,.2f}", "PROJEÇÃO": "R$ {:,.2f}", "X (-50%)": "R$ {:,.2f}"}))

with aba2:
    st.header("👥 Gestão de Agentes")
    op = st.selectbox("Auditoria:", df_audit["OPERADOR"].tolist(), key="fix_aba2")
    st.metric("Recuperado Individual", f"R$ {st.session_state.db['OPERAÇÃO'][op]['VALOR']:,.2f}")

with aba3:
    st.header("🧠 Inteligência de Mailing")
    st.progress(st.session_state.db['DISCADOR']['PEN'], text="Penetração Ativa")

with aba4:
    st.header("📡 Infraestrutura de Telefonia")
    st.error(f"Latência de {st.session_state.db['TELEFONIA']['LAT']}ms detectada.")

with aba5:
    st.header("📂 Exportação Blindada (HTML)")
    # Formato seguro para celular
    html_f = f"<html><body><h2>DOSSIÊ JURÍDICO</h2>{df_audit.to_html(index=False)}</body></html>"
    st.download_button("📥 ABRIR DOSSIÊ (WEB)", html_f.encode('utf-8-sig'), "DOSSIE.html", "text/html")

with aba6:
    st.header("⚖️ Auditoria Jurídica")
    st.table(df_audit[df_audit["STATUS"] == "BLOQUEADO"][["OPERADOR", "LEGAL", "STATUS"]])
