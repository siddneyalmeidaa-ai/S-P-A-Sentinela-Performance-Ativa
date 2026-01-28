import streamlit as st
import pandas as pd
from datetime import datetime
import io

# --- 1. CONFIGURAÇÃO PADRÃO OURO ---
st.set_page_config(page_title="S.P.A. MASTER - SIDNEY ALMEIDA", layout="wide", page_icon="⚖️")

# --- 2. QUANTUM MEMORY: CENÁRIOS INTEGRADOS (ACUMULATIVO) ---
if 'db' not in st.session_state:
    st.session_state.db = {
        "OPERAÇÃO": {
            "ANA (PERFORMANCE)": {"ALO": 1200, "CON": 950, "CPC": 450, "VALOR": 45800.0, "PROJ": 91600.0, "LEGAL": "Art. 444 CLT (Conformidade)", "FOR": "Alta conversão.", "PERDA": 0.0, "STATUS": "LIBERADO"},
            "MARCOS (SABOTAGEM)": {"ALO": 2500, "CON": 50, "CPC": 5, "VALOR": 0.0, "PROJ": 0.0, "LEGAL": "Art. 482, 'e' CLT (Desídia)", "FOR": "Cabo Desconectado.", "PERDA": 1250.0, "STATUS": "BLOQUEADO"},
            "RICARDO (OMISSÃO)": {"ALO": 800, "CON": 780, "CPC": 700, "VALOR": 150.0, "PROJ": 300.0, "LEGAL": "Art. 482, 'h' CLT (Insubordinação)", "FOR": "Mudo Proposital.", "PERDA": 850.0, "STATUS": "BLOQUEADO"},
            "JULIA (VÁCUO)": {"ALO": 100, "CON": 20, "CPC": 10, "VALOR": 800.0, "PROJ": 1600.0, "LEGAL": "Art. 482, 'e' CLT (Desídia)", "FOR": "IA Detectou Vácuo.", "PERDA": 450.0, "STATUS": "BLOQUEADO"}
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
    {
        "OPERADOR": k, 
        "STATUS": v["STATUS"],
        "VALOR": v["VALOR"], 
        "X (-50%)": v["PROJ"]*0.5, 
        "LEGAL": v["LEGAL"], 
        "EVIDÊNCIA": v["FOR"]
    }
    for k, v in st.session_state.db["OPERAÇÃO"].items()
])

# --- 3. INTERFACE DE NAVEGAÇÃO ---
st.title("🛰️ S.P.A. - SENTINELA DE PERFORMANCE ATIVA")
st.write(f"**COMANDANTE SIDNEY ALMEIDA** | {datetime.now().strftime('%d/%m/%Y %H:%M')}")

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
    st.header("📊 Cockpit Estratégico")
    c1, c2, c3 = st.columns(3)
    c1.metric("RECUPERAÇÃO TOTAL", f"R$ {df_base['VALOR'].sum():,.2f}")
    c2.metric("ALVOS BLOQUEADOS", len(df_base[df_base["STATUS"] == "BLOQUEADO"]))
    c3.metric("TELEFONIA", st.session_state.db["TELEFONIA"]["VIVO (TRUNK IP)"]["STATUS"])
    st.table(df_base[["OPERADOR", "VALOR", "STATUS", "LEGAL"]])

# --- ABA 04: TELEFONIA ---
with aba_tel:
    t_sel = st.selectbox("Trunk:", list(st.session_state.db["TELEFONIA"].keys()))
    d_t = st.session_state.db["TELEFONIA"][t_sel]
    cor = "inverse" if d_t["LAT"] > 100 or d_t["STATUS"] == "BLOQUEADO" else "normal"
    st.metric("LATÊNCIA", f"{d_t['LAT']}ms", delta="ALERTA" if d_t["LAT"] > 100 else "OK", delta_color=cor)

# --- ABA 05: CENTRAL DE RELATÓRIOS (ADICIONADO RELATÓRIO JURÍDICO) ---
with aba_rep:
    st.header("📂 Central de Exportação de Dossiês")
    
    # Filtro apenas para infrações jurídicas
    df_jur_report = df_base[df_base["STATUS"] == "BLOQUEADO"][["OPERADOR", "LEGAL", "EVIDÊNCIA"]]
    
    col_rep1, col_rep2 = st.columns(2)
    with col_rep1:
        st.subheader("📊 Relatórios Operacionais")
        st.download_button("📥 EXCEL (Auditoria Geral)", df_base.to_csv().encode('utf-8-sig'), "SPA_GERAL.xlsx")
        st.download_button("📥 PDF (Consolidado)", df_base.to_csv().encode('utf-8-sig'), "SPA_CONSOLIDADO.pdf")

    with col_rep2:
        st.subheader("⚖️ Relatórios Jurídicos (RH)")
        # BOTÃO ADICIONAL: Relatório específico de infrações
        st.download_button(
            label="📥 BAIXAR DOSSIÊ JURÍDICO (Somente Sabotagens)",
            data=df_jur_report.to_csv(index=False).encode('utf-8-sig'),
            file_name=f"DOSSIE_JURIDICO_{datetime.now().strftime('%d_%m')}.csv",
            mime="text/csv",
            help="Extrai apenas os operadores com status BLOQUEADO e seus respectivos artigos da CLT."
        )
        st.download_button("📥 TERMO DE ADVERTÊNCIA (Word)", df_jur_report.to_csv().encode('utf-8-sig'), "TERMO_ADVERTENCIA.docx")

# --- ABA 06: VISÃO JURÍDICA ---
with aba_jur:
    st.header("⚖️ Dossiê de Enquadramento Legal")
    df_juridico = df_base[df_base["STATUS"] == "BLOQUEADO"]
    if not df_juridico.empty:
        for index, row in df_juridico.iterrows():
            with st.expander(f"⚖️ PROCESSO: {row['OPERADOR']}"):
                st.warning(f"**INFRAÇÃO:** {row['LEGAL']}")
                st.info(f"**EVIDÊNCIA FORENSE:** {row['EVIDÊNCIA']}")
        st.table(df_juridico[["OPERADOR", "LEGAL", "EVIDÊNCIA"]])
    else:
        st.success("Nenhuma infração grave detectada.")
        
