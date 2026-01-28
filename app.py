import streamlit as st
import pandas as pd
from datetime import datetime
import io

# --- 1. CONFIGURAÇÃO PADRÃO OURO ---
st.set_page_config(page_title="S.P.A. MASTER - SIDNEY ALMEIDA", layout="wide", page_icon="⚖️")

# --- 2. QUANTUM MEMORY: BANCO DE DADOS INTEGRAL ---
if 'db' not in st.session_state:
    st.session_state.db = {
        "OPERAÇÃO": {
            "ANA (PERFORMANCE)": {"ALO": 1200, "CON": 950, "CPC": 450, "VALOR": 45800.0, "PROJ": 91600.0, "LEGAL": "Art. 444 CLT", "FOR": "Alta conversão.", "STATUS": "LIBERADO"},
            "MARCOS (SABOTAGEM)": {"ALO": 2500, "CON": 50, "CPC": 5, "VALOR": 0.0, "PROJ": 0.0, "LEGAL": "Art. 482, 'e' CLT", "FOR": "Cabo Desconectado.", "STATUS": "BLOQUEADO"},
            "RICARDO (OMISSÃO)": {"ALO": 800, "CON": 780, "CPC": 700, "VALOR": 150.0, "PROJ": 300.0, "LEGAL": "Art. 482, 'h' CLT", "FOR": "Mudo Proposital.", "STATUS": "BLOQUEADO"},
            "JULIA (VÁCUO)": {"ALO": 100, "CON": 20, "CPC": 10, "VALOR": 800.0, "PROJ": 1600.0, "LEGAL": "Art. 482, 'e' CLT", "FOR": "IA Detectou Vácuo.", "STATUS": "BLOQUEADO"}
        },
        "DISCADOR": {
            "MAILING_VIVO_JAN": {"TOTAL": 150000, "PEN": 65, "AUTO": 12.5, "SPC": "HIGIENIZADO", "QUALIDADE": "QUENTE"},
            "BASE_RECOVERY": {"TOTAL": 300000, "PEN": 15, "AUTO": 2.1, "SPC": "PENDENTE", "QUALIDADE": "FRIO"}
        },
        "TELEFONIA": {
            "VIVO (TRUNK IP)": {"STATUS": "BLOQUEADO", "LAT": 250, "FOR": "Instabilidade SIP.", "PERDA": 5000.0},
            "SIPvox (BACKUP)": {"STATUS": "LIBERADO", "LAT": 25, "FOR": "Rota Premium.", "PERDA": 0.0}
        }
    }

# Consolidação de Dados
df_base = pd.DataFrame([
    {"OPERADOR": k, "STATUS": v["STATUS"], "VALOR": v["VALOR"], "X (-50%)": v["PROJ"]*0.5, "LEGAL": v["LEGAL"], "EVIDÊNCIA": v["FOR"]}
    for k, v in st.session_state.db["OPERAÇÃO"].items()
])

# --- 3. CABEÇALHO DO COMANDO ---
st.title("🛰️ S.P.A. - SENTINELA DE PERFORMANCE ATIVA")
st.write(f"**COMANDANTE SIDNEY ALMEIDA** | {datetime.now().strftime('%d/%m/%Y %H:%M')}")

# --- 4. INTERFACE DE 6 ABAS (FORÇADAS) ---
tabs = st.tabs([
    "👑 01. VISÃO ESTRATÉGICA", 
    "👥 02. GESTÃO DE OPERADORES", 
    "🧠 03. ESTRATÉGIA DE DISCADOR", 
    "📡 04. INFRA TELEFONIA",
    "📂 05. CENTRAL DE RELATÓRIOS",
    "⚖️ 06. VISÃO JURÍDICA"
])

# --- ABA 01: VISÃO ESTRATÉGICA ---
with tabs[0]:
    st.header("📊 Cockpit de Auditoria")
    st.table(df_base[["OPERADOR", "VALOR", "X (-50%)", "STATUS"]])

# --- ABA 02: GESTÃO DE OPERADORES ---
with tabs[1]:
    st.header("👥 Detalhamento Individual")
    op = st.selectbox("Selecione:", df_base["OPERADOR"].tolist(), key="op_box")
    st.metric("Recuperado", f"R$ {st.session_state.db['OPERAÇÃO'][op]['VALOR']:,.2f}")
    st.info(f"Evidência: {st.session_state.db['OPERAÇÃO'][op]['FOR']}")

# --- ABA 03: ESTRATÉGIA DE DISCADOR ---
with tabs[2]:
    st.header("🧠 Inteligência de Mailing")
    for m, d in st.session_state.db["DISCADOR"].items():
        st.write(f"**{m}**: {d['PEN']}% de penetração.")

# --- ABA 04: INFRA TELEFONIA ---
with tabs[3]:
    st.header("📡 Monitoramento de Canais")
    d_t = st.session_state.db["TELEFONIA"]["VIVO (TRUNK IP)"]
    st.metric("LATÊNCIA VIVO", f"{d_t['LAT']}ms", delta="CRÍTICO", delta_color="inverse")

# --- ABA 05: CENTRAL DE RELATÓRIOS (BLINDADA) ---
with tabs[4]:
    st.header("📂 Exportação de Dossiês Oficiais")
    c_r1, c_r2 = st.columns(2)
    with c_r1:
        st.download_button("📥 EXCEL GERAL (CSV)", df_base.to_csv(index=False).encode('utf-8-sig'), "AUDITORIA_SPA.csv")
    with c_r2:
        df_jur = df_base[df_base["STATUS"] == "BLOQUEADO"]
        st.download_button("📥 DOSSIÊ JURÍDICO (TXT)", df_jur.to_csv(index=False).encode('utf-8-sig'), "DOSSIE_JURIDICO.txt")

# --- ABA 06: VISÃO JURÍDICA ---
with tabs[5]:
    st.header("⚖️ Enquadramento Legal")
    st.write(df_base[df_base["STATUS"] == "BLOQUEADO"][["OPERADOR", "LEGAL", "EVIDÊNCIA"]])
