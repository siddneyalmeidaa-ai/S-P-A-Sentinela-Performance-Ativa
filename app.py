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
            "BASE_VIVO": {"PEN": 65, "AUTO": 12},
            "BASE_RECOVERY": {"PEN": 15, "AUTO": 2}
        },
        "TELEFONIA": {
            "VIVO (TRUNK IP)": {"STATUS": "BLOQUEADO", "LAT": 250, "FOR": "Instabilidade SIP.", "PERDA": 5000.0}
        }
    }

# Consolidação de Dados Mestre
df_base = pd.DataFrame([
    {"OPERADOR": k, "STATUS": r["STATUS"], "VALOR": r["VALOR"], "X (-50%)": r["PROJ"]*0.5, "LEGAL": r["LEGAL"], "EVIDÊNCIA": r["FOR"]}
    for k, r in st.session_state.db["OPERAÇÃO"].items()
])

# --- 3. CABEÇALHO ---
st.title("🛰️ S.P.A. - SENTINELA DE PERFORMANCE ATIVA")
st.write(f"**COMANDANTE SIDNEY ALMEIDA** | Protocolo 2026")

# --- 4. INTERFACE DE 6 ABAS (FORÇADAS) ---
# Aqui garantimos que as 6 abas sejam criadas e populadas uma a uma
aba1, aba2, aba3, aba4, aba5, aba6 = st.tabs([
    "👑 01. VISÃO ESTRATÉGICA", 
    "👥 02. GESTÃO DE OPERADORES", 
    "🧠 03. ESTRATÉGIA DE DISCADOR", 
    "📡 04. INFRA TELEFONIA",
    "📂 05. CENTRAL DE RELATÓRIOS",
    "⚖️ 06. VISÃO JURÍDICA"
])

with aba1:
    st.header("📊 Cockpit de Auditoria")
    st.table(df_base[["OPERADOR", "VALOR", "X (-50%)", "STATUS"]])

with aba2:
    st.header("👥 Performance Individual")
    op_sel = st.selectbox("Selecione o Operador:", df_base["OPERADOR"].tolist())
    st.metric("Recuperação Individual", f"R$ {st.session_state.db['OPERAÇÃO'][op_sel]['VALOR']:,.2f}")
    st.warning(f"Evidência Técnica: {st.session_state.db['OPERAÇÃO'][op_sel]['FOR']}")

with aba3:
    st.header("🧠 Estratégia de Discador")
    for b, d in st.session_state.db["DISCADOR"].items():
        st.write(f"**{b}**: Penetração de {d['PEN']}%")

with aba4:
    st.header("📡 Infraestrutura de Telefonia")
    d_t = st.session_state.db["TELEFONIA"]["VIVO (TRUNK IP)"]
    st.metric("LATÊNCIA VIVO", f"{d_t['LAT']}ms", delta="ALERTA CRÍTICO", delta_color="inverse")
    st.error(f"Motivo do Bloqueio: {d_t['FOR']}")

with aba5:
    st.header("📂 Central de Relatórios Blindada")
    st.info("⚠️ Arquivos otimizados para telemóvel (HTML/CSV).")
    c1, c2 = st.columns(2)
    with c1:
        st.download_button("📥 EXCEL GERAL (CSV)", df_base.to_csv(index=False).encode('utf-8-sig'), "S_P_A_AUDITORIA.csv")
    with c2:
        df_jur = df_base[df_base["STATUS"] == "BLOQUEADO"]
        html_jur = f"<html><body><h2>DOSSIÊ JURÍDICO</h2>{df_jur.to_html(index=False)}</body></html>"
        st.download_button("📥 DOSSIÊ JURÍDICO (WEB)", html_jur.encode('utf-8-sig'), "DOSSIE_JURIDICO.html", "text/html")

with aba6:
    st.header("⚖️ Enquadramento Jurídico")
    st.table(df_base[df_base["STATUS"] == "BLOQUEADO"][["OPERADOR", "LEGAL", "EVIDÊNCIA"]])
