import streamlit as st
import pandas as pd
from datetime import datetime
import io

# --- 1. CONFIGURAÇÃO PADRÃO OURO ---
st.set_page_config(page_title="S.P.A. MASTER - SIDNEY ALMEIDA", layout="wide", page_icon="🛰️")

# --- 2. BANCO DE DADOS INTEGRAL (QUANTUM MEMORY) ---
if 'db' not in st.session_state:
    st.session_state.db = {
        "OPERAÇÃO": {
            "ANA (PERFORMANCE)": {"ALO": 1200, "CON": 950, "CPC": 450, "VALOR": 45800.0, "PROJ": 91600.0, "STATUS": "LIBERADO", "LEGAL": "Art. 444 CLT"},
            "MARCOS (SABOTAGEM)": {"ALO": 2500, "CON": 50, "CPC": 5, "VALOR": 0.0, "PROJ": 0.0, "STATUS": "BLOQUEADO", "LEGAL": "Art. 482 CLT (Desídia)"},
            "RICARDO (OMISSÃO)": {"ALO": 800, "CON": 780, "CPC": 700, "VALOR": 150.0, "PROJ": 300.0, "STATUS": "BLOQUEADO", "LEGAL": "Art. 482 CLT (Insubordinação)"},
            "JULIA (VÁCUO)": {"ALO": 100, "CON": 20, "CPC": 10, "VALOR": 800.0, "PROJ": 1600.0, "STATUS": "BLOQUEADO", "LEGAL": "Art. 482 CLT (Vácuo)"}
        },
        "DISCADOR": {"PENETRACAO": 65, "SPC_PENDENTE": 15, "QUALIDADE": "QUENTE", "AUTONOMIA": 12},
        "TELEFONIA": {"LATENCIA": 250, "STATUS": "CRÍTICO", "OPERADORA": "VIVO", "PERDA_EST": 7500.0}
    }

# Lógica da Tabela da Favelinha (Regra do X -50%) [cite: 2025-12-29, 2026-01-16]
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
st.write(f"**COMANDANTE SIDNEY ALMEIDA** | Console Consolidado Integral")

# --- 4. INTERFACE DE 6 ABAS OBRIGATÓRIAS (FORÇANDO RENDERIZAÇÃO) ---
# Aqui listamos as 6 abas explicitamente para garantir que apareçam de 1 a 6.
aba1, aba2, aba3, aba4, aba5, aba6 = st.tabs([
    "👑 01. VISÃO ESTRATÉGICA", 
    "👥 02. GESTÃO DE OPERADORES", 
    "🧠 03. ESTRATÉGIA DE DISCADOR", 
    "📡 04. INFRA TELEFONIA",
    "📂 05. CENTRAL DE RELATÓRIOS",
    "⚖️ 06. VISÃO JURÍDICA"
])

# --- ABA 01: VISÃO ESTRATÉGICA (CONSOLIDADO) ---
with aba1:
    st.header("📊 Painel Consolidado de Comando")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("📡 TELEFONIA", f"{st.session_state.db['TELEFONIA']['LATENCIA']}ms", "CRÍTICO", delta_color="inverse")
    col2.metric("🧠 DISCADOR", f"{st.session_state.db['DISCADOR']['PENETRACAO']}%", f"{st.session_state.db['DISCADOR']['SPC_PENDENTE']}% SPC")
    col3.metric("👥 BLOQUEIOS", "3 AGENTES", "SABOTAGEM", delta_color="inverse")
    col4.metric("💰 PERDA", f"R$ {st.session_state.db['TELEFONIA']['PERDA_EST']:,.2f}", "-7.5k", delta_color="inverse")
    st.divider()
    st.subheader("📋 Tabela da Favelinha (Regra do X)")
    st.dataframe(df_audit.style.format({"VALOR REAL": "R$ {:,.2f}", "PROJEÇÃO": "R$ {:,.2f}", "X (-50%)": "R$ {:,.2f}"}))

# --- ABA 02: GESTÃO DE OPERADORES ---
with aba2:
    st.header("👥 Análise Individual de Agentes")
    op_sel = st.selectbox("Auditar Operador:", df_audit["OPERADOR"].tolist(), key="v26_op")
    st.write(st.session_state.db["OPERAÇÃO"][op_sel])

# --- ABA 03: ESTRATÉGIA DE DISCADOR ---
with aba3:
    st.header("🧠 Métricas de Inteligência do Discador")
    st.metric("Penetração de Mailing", f"{st.session_state.db['DISCADOR']['PENETRACAO']}%")
    st.write(f"Qualidade: {st.session_state.db['DISCADOR']['QUALIDADE']}")

# --- ABA 04: INFRA TELEFONIA ---
with aba4:
    st.header("📡 Monitoramento de Canais VIVO")
    st.error(f"Alerta de Latência: {st.session_state.db['TELEFONIA']['LATENCIA']}ms")
    st.warning(f"Operadora sob Auditoria: {st.session_state.db['TELEFONIA']['OPERADORA']}")

# --- ABA 05: CENTRAL DE RELATÓRIOS (BLINDADA) ---
with aba5:
    st.header("📂 Exportação de Dossiês Oficiais")
    # Gerando HTML seguro que abre no seu celular [cite: 2026-01-28]
    html_data = f"<html><body><h2>DOSSIÊ JURÍDICO</h2>{df_audit[df_audit['STATUS'] == 'BLOQUEADO'].to_html()}</body></html>"
    st.download_button("📥 ABRIR DOSSIÊ JURÍDICO (WEB)", html_data.encode('utf-8-sig'), "DOSSIE.html", "text/html")
    st.download_button("📥 EXCEL GERAL (CSV)", df_audit.to_csv(index=False).encode('utf-8-sig'), "AUDITORIA.csv", "text/csv")

# --- ABA 06: VISÃO JURÍDICA ---
with aba6:
    st.header("⚖️ Dossiê CLT e Evidências Forenses")
    st.table(df_audit[df_audit["STATUS"] == "BLOQUEADO"][["OPERADOR", "LEGAL", "STATUS"]])
    
