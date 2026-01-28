import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. CONFIGURAÇÃO DE AMBIENTE ---
st.set_page_config(page_title="S.P.A. MASTER - FUSÃO TOTAL", layout="wide", page_icon="🛡️")

# --- 2. QUANTUM MEMORY (SOMA DE TODOS OS DADOS ACUMULADOS) ---
if 'db' not in st.session_state:
    st.session_state.db = {
        "OPERAÇÃO": {
            "ANA (PERFORMANCE)": {"ALO": 1200, "CON": 950, "CPC": 450, "VALOR": 45800.00, "PROJ": 91600.0, "LEGAL": "Art. 444 CLT", "FOR": "Script nível 5. Alta conversão.", "PERDA": 0.0},
            "MARCOS (SABOTAGEM)": {"ALO": 2500, "CON": 50, "CPC": 5, "VALOR": 0.00, "PROJ": 0.0, "LEGAL": "Art. 482, 'e' CLT", "FOR": "Cabo Desconectado/Ociosidade.", "PERDA": 1250.0},
            "RICARDO (OMISSÃO)": {"ALO": 800, "CON": 780, "CPC": 700, "VALOR": 150.00, "PROJ": 300.0, "LEGAL": "Art. 482, 'h' CLT", "FOR": "Mudo Proposital/Retenção.", "PERDA": 850.0}
        },
        "DISCADOR": {
            "MAILING_VIVO_JAN": {"TOTAL": 150000, "PEN": 65, "AUTO": 12.5, "SPC": "HIGIENIZADO", "QUALIDADE": "QUENTE", "TICKET": 185.0},
            "BASE_RECOVERY": {"TOTAL": 300000, "PEN": 15, "AUTO": 2.1, "SPC": "PENDENTE", "QUALIDADE": "FRIO", "TICKET": 420.0}
        },
        "TELEFONIA": {
            "VIVO (TRUNK IP)": {"STATUS": "BLOQUEADO", "LAT": "250ms", "FOR": "Queda de Link SIP.", "PERDA": 5000.0},
            "SIPvox (BACKUP)": {"STATUS": "LIBERADO", "LAT": "25ms", "FOR": "Rota Premium OK.", "PERDA": 0.0}
        }
    }

# --- 3. ESTRUTURA DE NAVEGAÇÃO ACUMULATIVA ---
st.title("🛰️ S.P.A. - SENTINELA DE PERFORMANCE ATIVA")
st.write(f"**COMANDANTE SIDNEY ALMEIDA** | {datetime.now().strftime('%d/%m/%Y %H:%M')}")

# Cada aba é um departamento, e a primeira é a soma de todos
aba_maisa, aba_op, aba_disc, aba_tel = st.tabs([
    "👑 01. VISÃO CONSOLIDADA (MAÍSA)", 
    "👥 02. GESTÃO DE OPERADORES", 
    "🧠 03. ESTRATÉGIA DE DISCADOR", 
    "📡 04. INFRA TELEFONIA"
])

# --- ABA 01: VISÃO MAÍSA (ADICIONADA COMO RESUMO) ---
with aba_maisa:
    st.header("📊 Cockpit Executivo - Resumo de Auditoria")
    c1, c2, c3, c4 = st.columns(4)
    
    total_rec = sum(item["VALOR"] for item in st.session_state.db["OPERAÇÃO"].values())
    total_perda = sum(item["PERDA"] for item in st.session_state.db["OPERAÇÃO"].values()) + st.session_state.db["TELEFONIA"]["VIVO (TRUNK IP)"]["PERDA"]
    bloqueios = sum(1 for item in st.session_state.db["OPERAÇÃO"].values() if item["VALOR"] == 0)
    
    c1.metric("RECUPERAÇÃO TOTAL", f"R$ {total_rec:,.2f}")
    c2.metric("PERDA POR SABOTAGEM/QUEDA", f"R$ {total_perda:,.2f}", delta="- PREJUÍZO", delta_color="inverse")
    c3.metric("ALERTAS DE BLOQUEIO", f"{bloqueios} ALVOS")
    c4.metric("SAÚDE DA MALHA", st.session_state.db["DISCADOR"]["MAILING_VIVO_JAN"]["QUALIDADE"])

    st.divider()
    st.subheader("📋 Tabela da Favelinha (Status Geral)")
    # Consolidação para a Maísa bater o olho
    resumo_favelinha = []
    for op, dados in st.session_state.db["OPERAÇÃO"].items():
        resumo_favelinha.append({
            "OPERADOR": op, "VALOR": dados["VALOR"], "CPC": dados["CPC"], 
            "PROJ X (-50%)": dados["PROJ"]*0.5, "LEGAL": dados["LEGAL"]
        })
    st.table(pd.DataFrame(resumo_favelinha))

# --- ABA 02: OPERAÇÃO (MANTIDA INTEGRAL) ---
with aba_op:
    st.header("👥 Detalhamento de Performance Individual")
    op_sel = st.selectbox("Auditar Operador:", list(st.session_state.db["OPERAÇÃO"].keys()), key="op_k")
    d_o = st.session_state.db["OPERAÇÃO"][op_sel]
    
    col1, col2, col3 = st.columns(3)
    col1.metric("ALÔ / CONTATO", f"{d_o['ALO']} / {d_o['CON']}")
    col2.metric("CPC EFETIVO", d_o["CPC"])
    col3.metric("ENQUADRAMENTO CLT", d_o["LEGAL"])
    st.info(f"**Análise Forense:** {d_o['FOR']}")

# --- ABA 03: DISCADOR (MANTIDA INTEGRAL) ---
with aba_disc:
    st.header("🧠 Inteligência de Mailing")
    ds_sel = st.selectbox("Mailing:", list(st.session_state.db["DISCADOR"].keys()), key="ds_k")
    d_d = st.session_state.db["DISCADOR"][ds_sel]
    st.write(f"**Autonomia:** {d_d['AUTO']} Dias | **SPC:** {d_d['SPC']}")
    st.progress(d_d["PEN"]/100, text=f"Penetração de Base: {d_d['PEN']}%")

# --- ABA 04: TELEFONIA (MANTIDA INTEGRAL) ---
with aba_tel:
    st.header("📡 Infraestrutura de Rede")
    tl_sel = st.selectbox("Trunk:", list(st.session_state.db["TELEFONIA"].keys()), key="tl_k")
    d_t = st.session_state.db["TELEFONIA"][tl_sel]
    st.metric("STATUS", d_t["STATUS"], delta=f"Latência: {d_t['LAT']}")

# --- 4. EXPORTAÇÃO ---
st.sidebar.divider()
st.sidebar.download_button("📊 EXPORTAR DOSSIÊ COMPLETO", pd.DataFrame(resumo_favelinha).to_csv(index=False).encode('utf-8-sig'), "DOSSIE_SPA.csv")
    
