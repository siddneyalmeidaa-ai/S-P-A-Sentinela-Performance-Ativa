import streamlit as st
import pandas as pd
from datetime import datetime
import io

# --- 1. CONFIGURAÇÃO PADRÃO OURO (IMUTÁVEL) ---
st.set_page_config(page_title="S.P.A. MASTER - SIDNEY ALMEIDA", layout="wide", page_icon="🛰️")

# --- 2. QUANTUM MEMORY: BANCO DE DADOS INTEGRAL ---
if 'db' not in st.session_state:
    st.session_state.db = {
        "OPERAÇÃO": {
            "ANA (PERFORMANCE)": {"VALOR": 45800.0, "PROJ": 91600.0, "STATUS": "LIBERADO", "LEGAL": "Art. 444 CLT"},
            "MARCOS (SABOTAGEM)": {"VALOR": 0.0, "PROJ": 0.0, "STATUS": "BLOQUEADO", "LEGAL": "Art. 482 CLT"},
            "RICARDO (OMISSÃO)": {"VALOR": 150.0, "PROJ": 300.0, "STATUS": "BLOQUEADO", "LEGAL": "Art. 482 CLT"},
            "JULIA (VÁCUO)": {"VALOR": 800.0, "PROJ": 1600.0, "STATUS": "BLOQUEADO", "LEGAL": "Art. 482 CLT"}
        },
        "DISCADOR": {"PENETRACAO": 65, "SPC": 15, "QUALIDADE": "QUENTE"},
        "TELEFONIA": {"LATENCIA": 250, "STATUS": "CRÍTICO", "OPERADORA": "VIVO"}
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

# --- 4. INTERFACE DE 6 ABAS (FIXAS - NÃO PODEM SER REMOVIDAS) ---
# O sistema agora força a criação das 6 variáveis de aba para garantir visibilidade total.
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
    st.header("📊 Cockpit Consolidado (Operação + Discador + Rede)")
    c1, c2, c3 = st.columns(3)
    c1.metric("📡 REDE VIVO", f"{st.session_state.db['TELEFONIA']['LATENCIA']}ms", "CRÍTICO", delta_color="inverse")
    c2.metric("🧠 DISCADOR", f"{st.session_state.db['DISCADOR']['PENETRACAO']}%", f"{st.session_state.db['DISCADOR']['SPC']}% SPC")
    c3.metric("👥 STATUS RH", "3 BLOQUEADOS", "SABOTAGEM", delta_color="inverse")
    st.divider()
    st.subheader("📋 Tabela da Favelinha (Regra do X)")
    st.dataframe(df_audit.style.format({"VALOR REAL": "R$ {:,.2f}", "PROJEÇÃO": "R$ {:,.2f}", "X (-50%)": "R$ {:,.2f}"}))

with aba2:
    st.header("👥 Gestão de Operadores")
    op_sel = st.selectbox("Auditoria Detalhada:", df_audit["OPERADOR"].tolist(), key="aba2_fix")
    st.write(f"**Enquadramento:** {st.session_state.db['OPERAÇÃO'][op_sel]['LEGAL']}")
    st.metric("Resultado Atual", f"R$ {st.session_state.db['OPERAÇÃO'][op_sel]['VALOR']:,.2f}")

with aba3:
    st.header("🧠 Inteligência de Mailing")
    st.write(f"Qualidade da Base: **{st.session_state.db['DISCADOR']['QUALIDADE']}**")
    st.progress(st.session_state.db['DISCADOR']['PENETRACAO'])

with aba4:
    st.header("📡 Infraestrutura de Telefonia")
    st.error(f"Latência Crítica detectada na Operadora: {st.session_state.db['TELEFONIA']['OPERADORA']}")
    st.metric("Latência SIP", f"{st.session_state.db['TELEFONIA']['LATENCIA']}ms")

with aba5:
    st.header("📂 Central de Relatórios Blindada")
    # Formato HTML validado para não corromper no seu celular [cite: 2026-01-28]
    html_f = f"<html><body><h2>DOSSIÊ S.P.A.</h2>{df_audit.to_html()}</body></html>"
    st.download_button("📥 ABRIR DOSSIÊ JURÍDICO (WEB)", html_f.encode('utf-8-sig'), "DOSSIE.html", "text/html")
    st.download_button("📥 EXCEL GERAL (CSV)", df_audit.to_csv(index=False).encode('utf-8-sig'), "AUDITORIA.csv", "text/csv")

with aba6:
    st.header("⚖️ Visão Jurídica (RH)")
    st.table(df_audit[df_audit["STATUS"] == "BLOQUEADO"][["OPERADOR", "LEGAL", "STATUS"]])
    
