import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. CONFIGURAÇÃO DE INTERFACE ---
st.set_page_config(page_title="S.P.A. MASTER - SIDNEY ALMEIDA", layout="wide", page_icon="🛰️")

# --- 2. BANCO DE DADOS INTEGRAL (FIXO) ---
# Estrutura robusta para evitar o KeyError dos prints 01:07 e 01:09
if 'db' not in st.session_state:
    st.session_state.db = {
        "OPERAÇÃO": {
            "ANA (PERFORMANCE)": {"VALOR": 45800.0, "PROJ": 91600.0, "STATUS": "LIBERADO", "LEGAL": "Art. 444 CLT"},
            "MARCOS (SABOTAGEM)": {"VALOR": 0.0, "PROJ": 0.0, "STATUS": "BLOQUEADO", "LEGAL": "Art. 482 CLT (Desídia)"},
            "RICARDO (OMISSÃO)": {"VALOR": 150.0, "PROJ": 300.0, "STATUS": "BLOQUEADO", "LEGAL": "Art. 482 CLT (Insubordinação)"},
            "JULIA (VÁCUO)": {"VALOR": 800.0, "PROJ": 1600.0, "STATUS": "BLOQUEADO", "LEGAL": "Art. 482 CLT (Vácuo)"}
        },
        "DISCADOR": {"PEN": 65, "SPC": 15, "QUALIDADE": "QUENTE"},
        "TELEFONIA": {"LAT": 250, "STATUS": "CRÍTICO", "OPERADORA": "VIVO"}
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
st.write(f"**COMANDANTE SIDNEY ALMEIDA** | Console Consolidado Integral (Abas 01-06)")

# --- 4. INTERFACE DE 6 ABAS (FIXAS E OBRIGATÓRIAS) ---
# A definição por variáveis individuais força o Streamlit a manter as 6 abas no menu superior.
aba1, aba2, aba3, aba4, aba5, aba6 = st.tabs([
    "👑 01. VISÃO ESTRATÉGICA", 
    "👥 02. GESTÃO DE OPERADORES", 
    "🧠 03. ESTRATÉGIA DE DISCADOR", 
    "📡 04. INFRA TELEFONIA",
    "📂 05. CENTRAL DE RELATÓRIOS",
    "⚖️ 06. VISÃO JURÍDICA"
])

# --- CONTEÚDO DAS ABAS ---

with aba1:
    st.header("📊 Cockpit Consolidado (Total)")
    # Correção do erro de métrica (c1, c2, c3 definidos corretamente)
    col1, col2, col3 = st.columns(3)
    col1.metric("📡 REDE VIVO", f"{st.session_state.db['TELEFONIA']['LAT']}ms", "CRÍTICO", delta_color="inverse")
    col2.metric("🧠 DISCADOR", f"{st.session_state.db['DISCADOR']['PEN']}%", f"{st.session_state.db['DISCADOR']['SPC']}% SPC")
    col3.metric("👥 STATUS RH", "3 BLOQUEADOS", "SABOTAGEM", delta_color="inverse")
    st.divider()
    st.subheader("📋 Tabela da Favelinha (Visão Geral)")
    st.dataframe(df_audit.style.format({"VALOR REAL": "R$ {:,.2f}", "PROJEÇÃO": "R$ {:,.2f}", "X (-50%)": "R$ {:,.2f}"}))

with aba2:
    st.header("👥 Gestão Individual")
    op_sel = st.selectbox("Selecione para Auditoria:", df_audit["OPERADOR"].tolist(), key="v29_op")
    st.write(f"**Situação Jurídica:** {st.session_state.db['OPERAÇÃO'][op_sel]['LEGAL']}")
    st.metric("Resultado Recuperado", f"R$ {st.session_state.db['OPERAÇÃO'][op_sel]['VALOR']:,.2f}")

with aba3:
    st.header("🧠 Inteligência de Discagem")
    st.info(f"Qualidade atual do Mailing: {st.session_state.db['DISCADOR']['QUALIDADE']}")
    st.progress(st.session_state.db['DISCADOR']['PEN'])

with aba4:
    st.header("📡 Infraestrutura de Telefonia")
    st.error(f"Latência de {st.session_state.db['TELEFONIA']['LAT']}ms na rota {st.session_state.db['TELEFONIA']['OPERADORA']}")

with aba5:
    st.header("📂 Exportação de Dossiês (Modo Web)")
    # Formato HTML validado que abre no seu celular (conforme print 01:02)
    html_f = f"<html><body style='font-family:sans-serif;'><h2>DOSSIÊ JURÍDICO</h2>{df_audit.to_html(index=False)}</body></html>"
    st.download_button("📥 ABRIR DOSSIÊ JURÍDICO (WEB)", html_f.encode('utf-8-sig'), "DOSSIE.html", "text/html")
    st.download_button("📥 EXCEL (CSV)", df_audit.to_csv(index=False).encode('utf-8-sig'), "AUDITORIA.csv", "text/csv")

with aba6:
    st.header("⚖️ Auditoria Jurídica (RH)")
    st.table(df_audit[df_audit["STATUS"] == "BLOQUEADO"][["OPERADOR", "LEGAL", "STATUS"]])
    
