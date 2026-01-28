import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. CONFIGURAÇÃO PADRÃO OURO ---
st.set_page_config(page_title="S.P.A. MASTER - SIDNEY ALMEIDA", layout="wide", page_icon="🛡️")

# --- 2. QUANTUM MEMORY: TODOS OS DADOS ACUMULADOS ---
if 'db' not in st.session_state:
    st.session_state.db = {
        "OPERAÇÃO": {
            "ANA (PERFORMANCE)": {"ALO": 1200, "CON": 950, "CPC": 450, "VALOR": 45800.0, "PROJ": 91600.0, "LEGAL": "Art. 444 CLT", "FOR": "Alta conversão.", "PERDA": 0.0},
            "MARCOS (SABOTAGEM)": {"ALO": 2500, "CON": 50, "CPC": 5, "VALOR": 0.0, "PROJ": 0.0, "LEGAL": "Art. 482, 'e' CLT", "FOR": "Cabo Desconectado.", "PERDA": 1250.0},
            "RICARDO (OMISSÃO)": {"ALO": 800, "CON": 780, "CPC": 700, "VALOR": 150.0, "PROJ": 300.0, "LEGAL": "Art. 482, 'h' CLT", "FOR": "Mudo Proposital.", "PERDA": 850.0},
            "JULIA (VÁCUO)": {"ALO": 100, "CON": 20, "CPC": 10, "VALOR": 800.0, "PROJ": 1600.0, "LEGAL": "Art. 482, 'e' CLT", "FOR": "IA Detectou Vácuo.", "PERDA": 450.0}
        },
        "DISCADOR": {
            "MAILING_VIVO_JAN": {"TOTAL": 150000, "PEN": 65, "AUTO": 12.5, "SPC": "HIGIENIZADO", "QUALIDADE": "QUENTE", "TICKET": 185.0},
            "BASE_RECOVERY": {"TOTAL": 300000, "PEN": 15, "AUTO": 2.1, "SPC": "PENDENTE", "QUALIDADE": "FRIO", "TICKET": 420.0}
        },
        "TELEFONIA": {
            "VIVO (TRUNK IP)": {"STATUS": "BLOQUEADO", "LAT": 250, "FOR": "Queda de Link SIP / Jitter.", "PERDA": 5000.0},
            "SIPvox (BACKUP)": {"STATUS": "LIBERADO", "LAT": 25, "FOR": "Rota Premium Estável.", "PERDA": 0.0}
        }
    }

# --- 3. INTERFACE DE NAVEGAÇÃO ---
st.title("🛰️ S.P.A. - SENTINELA DE PERFORMANCE ATIVA")
st.write(f"**COMANDANTE SIDNEY ALMEIDA** | {datetime.now().strftime('%d/%m/%Y %H:%M')}")

aba_maisa, aba_op, aba_disc, aba_tel = st.tabs([
    "👑 01. VISÃO CONSOLIDADA (MAÍSA)", 
    "👥 02. GESTÃO DE OPERADORES", 
    "🧠 03. ESTRATÉGIA DE DISCADOR", 
    "📡 04. INFRA TELEFONIA"
])

# --- ABA 01: VISÃO MAÍSA (CONSOLIDADO EXECUTIVO) ---
with aba_maisa:
    st.header("📊 Cockpit Executivo de Auditoria")
    c1, c2, c3, c4 = st.columns(4)
    
    total_rec = sum(item["VALOR"] for item in st.session_state.db["OPERAÇÃO"].values())
    total_perda = sum(item["PERDA"] for item in st.session_state.db["OPERAÇÃO"].values()) + st.session_state.db["TELEFONIA"]["VIVO (TRUNK IP)"]["PERDA"]
    bloqueios = sum(1 for item in st.session_state.db["OPERAÇÃO"].values() if item["VALOR"] == 0)
    
    c1.metric("RECUPERAÇÃO TOTAL", f"R$ {total_rec:,.2f}")
    c2.metric("PERDA OPERACIONAL", f"R$ {total_perda:,.2f}", delta="- PREJUÍZO", delta_color="inverse")
    c3.metric("BLOQUEIOS ATIVOS", f"{bloqueios} ALVOS")
    c4.metric("STATUS TELEFONIA", st.session_state.db["TELEFONIA"]["VIVO (TRUNK IP)"]["STATUS"])

    st.divider()
    st.subheader("📋 Tabela da Favelinha (Visão Resumo)")
    resumo_favelinha = []
    for op, dados in st.session_state.db["OPERAÇÃO"].items():
        resumo_favelinha.append({
            "OPERADOR": op, "ALO": dados["ALO"], "CPC": dados["CPC"], 
            "VALOR": dados["VALOR"], "PROJ X (-50%)": dados["PROJ"]*0.5, "LEGAL": dados["LEGAL"]
        })
    st.table(pd.DataFrame(resumo_favelinha))

# --- ABA 02: OPERAÇÃO (DETALHAMENTO TÉCNICO) ---
with aba_op:
    st.header("👥 Auditoria de Performance e Sabotagem")
    op_sel = st.selectbox("Selecione para Dossiê:", list(st.session_state.db["OPERAÇÃO"].keys()), key="op_k")
    d_o = st.session_state.db["OPERAÇÃO"][op_sel]
    
    col1, col2, col3 = st.columns(3)
    col1.metric("ALÔ / CONTATO", f"{d_o['ALO']} / {d_o['CON']}")
    col2.metric("CPC EFETIVO", d_o["CPC"])
    col3.metric("VALOR", f"R$ {d_o['VALOR']:,.2f}")
    
    st.divider()
    st.error(f"**ENQUADRAMENTO JURÍDICO:** {d_o['LEGAL']}")
    st.info(f"**PARECER FORENSE:** {d_o['FOR']}")

# --- ABA 03: DISCADOR (ESTRATÉGIA DE MAILING) ---
with aba_disc:
    st.header("🧠 Inteligência de Malha e Capacity")
    ds_sel = st.selectbox("Carga Ativa:", list(st.session_state.db["DISCADOR"].keys()), key="ds_k")
    d_d = st.session_state.db["DISCADOR"][ds_sel]
    
    m1, m2, m3 = st.columns(3)
    m1.metric("QUALIDADE", d_d["QUALIDADE"])
    m2.metric("AUTONOMIA", f"{d_d['AUTO']} Dias")
    m3.metric("ESTEIRA SPC", d_d["SPC"])
    st.progress(d_d["PEN"]/100, text=f"Penetração: {d_d['PEN']}%")

# --- ABA 04: TELEFONIA (INFRAESTRUTURA COM CORREÇÃO VISUAL) ---
with aba_tel:
    st.header("📡 Monitoramento de Canais IP")
    tl_sel = st.selectbox("Trunk:", list(st.session_state.db["TELEFONIA"].keys()), key="tl_k")
    d_t = st.session_state.db["TELEFONIA"][tl_sel]
    
    t1, t2 = st.columns(2)
    t1.metric("STATUS", d_t["STATUS"])
    
    # CORREÇÃO: Seta vermelha para latência alta ou bloqueio
    seta_alerta = "inverse" if d_t["LAT"] > 100 or d_t["STATUS"] == "BLOQUEADO" else "normal"
    t2.metric("LATÊNCIA", f"{d_t['LAT']}ms", delta="ALERTA TÉCNICO" if d_t["LAT"] > 100 else "ESTÁVEL", delta_color=seta_alerta)
    
    st.divider()
    st.warning(f"**LOG DE REDE:** {d_t['FOR']}")

# --- 5. EXPORTAÇÃO ---
st.sidebar.download_button("📊 EXPORTAR PADRÃO OURO", pd.DataFrame(resumo_favelinha).to_csv(index=False).encode('utf-8-sig'), "SPA_AUDITORIA_SIDNEY.csv")
    
