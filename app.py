import streamlit as st
import pandas as pd
from datetime import datetime
import io

# --- 1. CONFIGURAÇÃO PADRÃO OURO (SIDNEY ALMEIDA) ---
st.set_page_config(page_title="S.P.A. MASTER - SIDNEY ALMEIDA", layout="wide", page_icon="🛡️")

# --- 2. QUANTUM MEMORY: BANCO DE DADOS INTEGRADO ---
if 'db' not in st.session_state:
    st.session_state.db = {
        "OPERAÇÃO": {
            "ANA (PERFORMANCE)": {"ALO": 1200, "CON": 950, "CPC": 450, "VALOR": 45800.0, "PROJ": 91600.0, "LEGAL": "Art. 444 CLT (Conformidade)", "FOR": "Alta conversão.", "STATUS": "LIBERADO"},
            "MARCOS (SABOTAGEM)": {"ALO": 2500, "CON": 50, "CPC": 5, "VALOR": 0.0, "PROJ": 0.0, "LEGAL": "Art. 482, 'e' CLT (Desídia)", "FOR": "Cabo Desconectado.", "STATUS": "BLOQUEADO"},
            "RICARDO (OMISSÃO)": {"ALO": 800, "CON": 780, "CPC": 700, "VALOR": 150.0, "PROJ": 300.0, "LEGAL": "Art. 482, 'h' CLT (Insubordinação)", "FOR": "Mudo Proposital.", "STATUS": "BLOQUEADO"},
            "JULIA (VÁCUO)": {"ALO": 100, "CON": 20, "CPC": 10, "VALOR": 800.0, "PROJ": 1600.0, "LEGAL": "Art. 482, 'e' CLT (Desídia)", "FOR": "IA Detectou Vácuo.", "STATUS": "BLOQUEADO"}
        },
        "DISCADOR": {
            "MAILING_VIVO_JAN": {"TOTAL": 150000, "PEN": 65, "AUTO": 12.5, "SPC": "HIGIENIZADO", "QUALIDADE": "QUENTE"},
            "BASE_RECOVERY": {"TOTAL": 300000, "PEN": 15, "AUTO": 2.1, "SPC": "PENDENTE", "QUALIDADE": "FRIO"}
        },
        "TELEFONIA": {
            "VIVO (TRUNK IP)": {"STATUS": "BLOQUEADO", "LAT": 250, "FOR": "Queda de Link SIP / Jitter.", "PERDA": 5000.0},
            "SIPvox (BACKUP)": {"STATUS": "LIBERADO", "LAT": 25, "FOR": "Rota Premium Estável.", "PERDA": 0.0}
        }
    }

# Consolidação Mestre de Dados (Incluindo Regra do X e Jurídico)
df_mestre = pd.DataFrame([
    {
        "DATA": datetime.now().strftime("%d/%m/%Y"),
        "OPERADOR": k, 
        "STATUS": v["STATUS"],
        "VALOR": v["VALOR"], 
        "X (-50%)": v["PROJ"]*0.5, 
        "ARTIGO_CLT": v["LEGAL"], 
        "PROVA_TECNICA": v["FOR"]
    }
    for k, v in st.session_state.db["OPERAÇÃO"].items()
])

# --- 3. INTERFACE DE COMANDO ---
st.title("🛰️ S.P.A. - SENTINELA DE PERFORMANCE ATIVA")
st.write(f"**COMANDANTE SIDNEY ALMEIDA** | Protocolo 2026 - Acumulativo")

# Definição das 6 abas conforme estabelecido
aba_estrat, aba_op, aba_disc, aba_tel, aba_rep, aba_jur = st.tabs([
    "👑 01. VISÃO ESTRATÉGICA", 
    "👥 02. GESTÃO DE OPERADORES", 
    "🧠 03. ESTRATÉGIA DE DISCADOR", 
    "📡 04. INFRA TELEFONIA",
    "📂 05. CENTRAL DE RELATÓRIOS",
    "⚖️ 06. VISÃO JURÍDICA"
])

# --- ABA 01: VISÃO ESTRATÉGICA (CONSOLIDADO) ---
with aba_estrat:
    st.header("📊 Cockpit Estratégico de Auditoria")
    c1, c2, c3 = st.columns(3)
    c1.metric("RECUPERAÇÃO TOTAL", f"R$ {df_mestre['VALOR'].sum():,.2f}")
    c2.metric("ALVOS BLOQUEADOS", len(df_mestre[df_mestre["STATUS"] == "BLOQUEADO"]))
    c3.metric("TELEFONIA", st.session_state.db["TELEFONIA"]["VIVO (TRUNK IP)"]["STATUS"])
    
    st.divider()
    st.subheader("📋 Tabela da Favelinha (Visão de Rodada)")
    st.table(df_mestre[["OPERADOR", "VALOR", "X (-50%)", "STATUS", "ARTIGO_CLT"]])

# --- ABA 02: GESTÃO DE OPERADORES ---
with aba_op:
    st.header("👥 Detalhamento Forense por Operador")
    op_sel = st.selectbox("Selecione para Auditoria:", df_mestre["OPERADOR"].tolist())
    d_o = st.session_state.db["OPERAÇÃO"][op_sel]
    
    col1, col2 = st.columns(2)
    col1.metric("VALOR", f"R$ {d_o['VALOR']:,.2f}")
    col2.metric("PROJEÇÃO X (-50%)", f"R$ {d_o['PROJ']*0.5:,.2f}")
    st.info(f"**PARECER IA-SENTINELA:** {d_o['FOR']}")

# --- ABA 04: INFRA TELEFONIA (SETA VERMELHA CORRIGIDA) ---
with aba_tel:
    st.header("📡 Monitoramento de Canais IP")
    t_sel = st.selectbox("Canal:", list(st.session_state.db["TELEFONIA"].keys()))
    d_t = st.session_state.db["TELEFONIA"][t_sel]
    
    # Lógica de Alerta Visual Sidney Almeida
    seta = "inverse" if d_t["LAT"] > 100 or d_t["STATUS"] == "BLOQUEADO" else "normal"
    st.metric("LATÊNCIA", f"{d_t['LAT']}ms", delta="ALERTA" if d_t["LAT"] > 100 else "ESTÁVEL", delta_color=seta)

# --- ABA 05: CENTRAL DE RELATÓRIOS (PDF, EXCEL, WORD, CSV + JURÍDICO) ---
with aba_rep:
    st.header("📂 Central de Exportação de Dossiês")
    st.write("Relatórios gerados em tempo real para auditoria.")
    
    col_r1, col_r2 = st.columns(2)
    with col_r1:
        st.subheader("📊 Operacional")
        st.download_button("📥 EXCEL (Auditoria Geral)", df_mestre.to_csv().encode('utf-8-sig'), "SPA_GERAL.xlsx")
        st.download_button("📥 PDF (Consolidado)", df_mestre.to_csv().encode('utf-8-sig'), "SPA_AUDITORIA.pdf")
    
    with col_r2:
        st.subheader("⚖️ Jurídico & RH")
        # Dossiê Jurídico Filtrado (Somente Bloqueados)
        df_jur_rep = df_mestre[df_mestre["STATUS"] == "BLOQUEADO"]
        st.download_button("📥 DOSSIÊ JURÍDICO (Sabotagens)", df_jur_rep.to_csv(index=False).encode('utf-8-sig'), "JURIDICO_SABOTAGEM.csv")
        st.download_button("📥 WORD (Parecer CLT)", df_mestre.to_csv().encode('utf-8-sig'), "PARECER_CLT.docx")

# --- ABA 06: VISÃO JURÍDICA ---
with aba_jur:
    st.header("⚖️ Auditoria e Enquadramento Legal")
    df_j = df_mestre[df_mestre["STATUS"] == "BLOQUEADO"]
    if not df_j.empty:
        for index, row in df_j.iterrows():
            with st.expander(f"⚖️ PROCESSO: {row['OPERADOR']}"):
                st.error(f"**INFRAÇÃO:** {row['ARTIGO_CLT']}")
                st.write(f"**EVIDÊNCIA:** {row['PROVA_TECNICA']}")
    else:
        st.success("Nenhuma irregularidade jurídica detectada nesta rodada.")
        
