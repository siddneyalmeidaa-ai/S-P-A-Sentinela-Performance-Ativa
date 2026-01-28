import streamlit as st
import pandas as pd
from datetime import datetime
import io

# --- 1. CONFIGURAÇÃO PADRÃO OURO ---
st.set_page_config(page_title="S.P.A. MASTER - SIDNEY ALMEIDA", layout="wide", page_icon="⚖️")

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
            "VIVO (TRUNK IP)": {"STATUS": "BLOQUEADO", "LAT": 250, "FOR": "Instabilidade SIP.", "PERDA": 5000.0},
            "SIPvox (BACKUP)": {"STATUS": "LIBERADO", "LAT": 25, "FOR": "Rota Premium.", "PERDA": 0.0}
        }
    }

# Consolidação de Dados Mestre (Com Regra do X e Jurídico)
df_base = pd.DataFrame([
    {
        "OPERADOR": k, 
        "STATUS": v["STATUS"],
        "VALOR": v["VALOR"], 
        "X (-50%)": v["PROJ"]*0.5, 
        "LEGAL": v["LEGAL"], 
        "EVIDÊNCIA": v["FOR"],
        "ALO": v["ALO"],
        "CPC": v["CPC"]
    }
    for k, v in st.session_state.db["OPERAÇÃO"].items()
])

# --- 3. CABEÇALHO DO COMANDO ---
st.title("🛰️ S.P.A. - SENTINELA DE PERFORMANCE ATIVA")
st.write(f"**COMANDANTE SIDNEY ALMEIDA** | {datetime.now().strftime('%d/%m/%Y %H:%M')}")

# --- 4. INTERFACE DE NAVEGAÇÃO (6 ABAS COMPLETAS) ---
aba_estrat, aba_op, aba_disc, aba_tel, aba_rep, aba_jur = st.tabs([
    "👑 01. VISÃO ESTRATÉGICA", 
    "👥 02. GESTÃO DE OPERADORES", 
    "🧠 03. ESTRATÉGIA DE DISCADOR", 
    "📡 04. INFRA TELEFONIA",
    "📂 05. CENTRAL DE RELATÓRIOS",
    "⚖️ 06. VISÃO JURÍDICA"
])

# --- ABA 01: VISÃO ESTRATÉGICA ---
with aba_estrat:
    st.header("📊 Cockpit Executivo de Auditoria")
    c1, c2, c3 = st.columns(3)
    c1.metric("RECUPERAÇÃO TOTAL", f"R$ {df_base['VALOR'].sum():,.2f}")
    c2.metric("ALVOS BLOQUEADOS", len(df_base[df_base["STATUS"] == "BLOQUEADO"]))
    c3.metric("TELEFONIA VIVO", st.session_state.db["TELEFONIA"]["VIVO (TRUNK IP)"]["STATUS"])
    
    st.divider()
    st.subheader("📋 Tabela da Favelinha (Visão de Rodada)")
    st.table(df_base[["OPERADOR", "VALOR", "X (-50%)", "STATUS", "LEGAL"]])

# --- ABA 02: GESTÃO DE OPERADORES ---
with aba_op:
    st.header("👥 Detalhamento de Performance Individual")
    op_sel = st.selectbox("Selecione o Operador para Auditoria:", df_base["OPERADOR"].tolist(), key="op_box")
    d_o = st.session_state.db["OPERAÇÃO"][op_sel]
    
    col_v1, col_v2, col_v3 = st.columns(3)
    col_v1.metric("ALO / CPC", f"{d_o['ALO']} / {d_o['CPC']}")
    col_v2.metric("Valor Recuperado", f"R$ {d_o['VALOR']:,.2f}")
    col_v3.metric("Status Operacional", d_o["STATUS"])
    st.info(f"**Parecer IA-Sentinela:** {d_o['FOR']}")

# --- ABA 03: ESTRATÉGIA DE DISCADOR ---
with aba_disc:
    st.header("🧠 Inteligência de Mailing e Discador")
    for base, dados in st.session_state.db["DISCADOR"].items():
        st.subheader(f"Base: {base}")
        m1, m2, m3 = st.columns(3)
        m1.metric("Autonomia", f"{dados['AUTO']} Dias")
        m2.metric("Qualidade", dados["QUALIDADE"])
        m3.metric("Higienização", dados["SPC"])
        st.progress(dados['PEN']/100, text=f"Penetração de Mailing: {dados['PEN']}%")

# --- ABA 04: INFRA TELEFONIA (SETA VERMELHA) ---
with aba_tel:
    st.header("📡 Monitoramento de Canais SIP")
    t_sel = st.selectbox("Selecionar Canal para Análise:", list(st.session_state.db["TELEFONIA"].keys()))
    d_t = st.session_state.db["TELEFONIA"][t_sel]
    
    # Lógica de Alerta Visual Corrigida
    seta = "inverse" if d_t["LAT"] > 100 or d_t["STATUS"] == "BLOQUEADO" else "normal"
    st.metric("LATÊNCIA", f"{d_t['LAT']}ms", delta="ALERTA CRÍTICO" if d_t["LAT"] > 100 else "ESTÁVEL", delta_color=seta)
    st.error(f"**LOG DE REDE:** {d_t['FOR']}")

# --- ABA 05: CENTRAL DE RELATÓRIOS (INTEGRADO) ---
with aba_rep:
    st.header("📂 Exportação de Dossiês Oficiais")
    col_r1, col_r2 = st.columns(2)
    
    with col_r1:
        st.subheader("📊 Relatórios Operacionais")
        st.download_button("📥 EXCEL (Auditoria Geral)", df_base.to_csv().encode('utf-8-sig'), "SPA_AUDITORIA.xlsx")
        st.download_button("📥 PDF (Dossiê Consolidado)", df_base.to_csv().encode('utf-8-sig'), "SPA_DOSSIE.pdf")
    
    with col_r2:
        st.subheader("⚖️ Relatórios Jurídicos (RH)")
        df_jur_rep = df_base[df_base["STATUS"] == "BLOQUEADO"]
        st.download_button("📥 RELATÓRIO DE SABOTAGENS (CSV)", df_jur_rep.to_csv(index=False).encode('utf-8-sig'), "JURIDICO_SABOTAGEM.csv")
        st.download_button("📥 TERMO DE ADVERTÊNCIA (Word)", df_jur_rep.to_csv().encode('utf-8-sig'), "TERMO_ADVERTENCIA.docx")

# --- ABA 06: VISÃO JURÍDICA ---
with aba_jur:
    st.header("⚖️ Enquadramento Legal e Compliance")
    df_j = df_base[df_base["STATUS"] == "BLOQUEADO"]
    if not df_j.empty:
        for _, row in df_j.iterrows():
            with st.expander(f"⚖️ EVIDÊNCIA FORENSE: {row['OPERADOR']}"):
                st.error(f"**ARTIGO CLT:** {row['LEGAL']}")
                st.write(f"**DESCRIÇÃO DA INFRAÇÃO:** {row['EVIDÊNCIA']}")
                st.write(f"**IMPACTO FINANCEIRO:** R$ {row['VALOR']}")
    else:
        st.success("Nenhuma irregularidade jurídica detectada nesta rodada.")
