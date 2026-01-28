import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. CONFIGURAÇÃO ---
st.set_page_config(page_title="S.P.A. MASTER - CORREÇÃO VISUAL", layout="wide", page_icon="🛡️")

# --- 2. QUANTUM MEMORY (DADOS ACUMULADOS E SEGREGAÇÃO) ---
if 'db' not in st.session_state:
    st.session_state.db = {
        "OPERAÇÃO": {
            "ANA (PERFORMANCE)": {"ALO": 1200, "CON": 950, "CPC": 450, "VALOR": 45800.00, "PROJ": 91600.0, "LEGAL": "Art. 444 CLT", "FOR": "Alta conversão.", "PERDA": 0.0},
            "MARCOS (SABOTAGEM)": {"ALO": 2500, "CON": 50, "CPC": 5, "VALOR": 0.00, "PROJ": 0.0, "LEGAL": "Art. 482, 'e' CLT", "FOR": "Cabo Desconectado.", "PERDA": 1250.0},
            "RICARDO (OMISSÃO)": {"ALO": 800, "CON": 780, "CPC": 700, "VALOR": 150.00, "PROJ": 300.0, "LEGAL": "Art. 482, 'h' CLT", "FOR": "Mudo Proposital.", "PERDA": 850.0}
        },
        "DISCADOR": {
            "MAILING_VIVO_JAN": {"TOTAL": 150000, "PEN": 65, "AUTO": 12.5, "SPC": "HIGIENIZADO", "QUALIDADE": "QUENTE"},
            "BASE_RECOVERY": {"TOTAL": 300000, "PEN": 15, "AUTO": 2.1, "SPC": "PENDENTE", "QUALIDADE": "FRIO"}
        },
        "TELEFONIA": {
            "VIVO (TRUNK IP)": {"STATUS": "BLOQUEADO", "LAT": 250, "FOR": "Instabilidade de Jitter/Queda Link.", "PERDA": 5000.0},
            "SIPvox (BACKUP)": {"STATUS": "LIBERADO", "LAT": 25, "FOR": "Rota Premium Estável.", "PERDA": 0.0}
        }
    }

# --- 3. INTERFACE POR ABAS ---
st.title("🛰️ S.P.A. - SENTINELA DE PERFORMANCE ATIVA")

aba_maisa, aba_op, aba_disc, aba_tel = st.tabs([
    "👑 01. VISÃO CONSOLIDADA (MAÍSA)", 
    "👥 02. GESTÃO DE OPERADORES", 
    "🧠 03. ESTRATÉGIA DE DISCADOR", 
    "📡 04. INFRA TELEFONIA"
])

# --- ABA 01: VISÃO MAÍSA ---
with aba_maisa:
    st.header("📊 Cockpit Executivo")
    c1, c2, c3 = st.columns(3)
    total_rec = sum(item["VALOR"] for item in st.session_state.db["OPERAÇÃO"].values())
    c1.metric("RECUPERAÇÃO TOTAL", f"R$ {total_rec:,.2f}")
    c2.metric("MAILING ATIVO", st.session_state.db["DISCADOR"]["MAILING_VIVO_JAN"]["QUALIDADE"])
    c3.metric("INFRAESTRUTURA", st.session_state.db["TELEFONIA"]["VIVO (TRUNK IP)"]["STATUS"])
    
    st.divider()
    st.subheader("📋 Tabela da Favelinha (Visão de Rodada)")
    resumo = [{"OPERADOR": k, "CPC": v["CPC"], "VALOR": v["VALOR"], "X (-50%)": v["PROJ"]*0.5, "LEGAL": v["LEGAL"]} 
              for k, v in st.session_state.db["OPERAÇÃO"].items()]
    st.table(pd.DataFrame(resumo))

# --- ABA 04: INFRA TELEFONIA (FOCO NA CORREÇÃO DA SETA) ---
with aba_tel:
    st.header("📡 Monitoramento de Conectividade")
    t_sel = st.selectbox("Selecione o Trunk:", list(st.session_state.db["TELEFONIA"].keys()))
    d_t = st.session_state.db["TELEFONIA"][t_sel]
    
    col_t1, col_t2 = st.columns(2)
    col_t1.metric("STATUS DO LINK", d_t["STATUS"])
    
    # Lógica da Seta: Se latência > 100 ou Status é BLOQUEADO, seta vermelha (inverse)
    cor_seta = "inverse" if d_t["LAT"] > 100 or d_t["STATUS"] == "BLOQUEADO" else "normal"
    
    col_t2.metric(
        label="LATÊNCIA DE ROTA", 
        value=f"{d_t['LAT']}ms", 
        delta="ALTA / INSTÁVEL" if d_t["LAT"] > 100 else "ESTÁVEL",
        delta_color=cor_seta
    )
    
    st.divider()
    st.error(f"**Análise de Risco:** {d_t['FOR']}")

# Manutenção das outras abas (Omitidas aqui para brevidade, mas mantidas no código real)
with aba_op: st.write("Módulo de Operadores Ativo.")
with aba_disc: st.write("Módulo de Discador Ativo.")
    
