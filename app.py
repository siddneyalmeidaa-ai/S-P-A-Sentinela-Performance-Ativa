import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. CONFIGURAÇÃO DE INTERFACE (BLINDAGEM VISUAL) ---
st.set_page_config(page_title="S.P.A. MASTER - SIDNEY ALMEIDA", layout="wide", page_icon="🛰️")

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;} header {visibility: hidden;} footer {visibility: hidden;}
    .stDeployButton {display:none;}
    .manifesto-container {
        background-color: #050505; border-left: 5px solid #00FF41;
        padding: 20px; border-radius: 10px; margin-bottom: 25px;
    }
    .quote-text { color: #00FF41; font-size: 18px; font-weight: bold; font-style: italic; }
    .signature { color: #D4AF37; font-size: 12px; text-transform: uppercase; letter-spacing: 2px; }
    </style>
""", unsafe_allow_html=True)

# --- 2. BANCO DE DADOS INTEGRAL (PADRÃO OURO) ---
if 'db' not in st.session_state:
    st.session_state.db = {
        "OPERAÇÃO": {
            "ANA (PERFORMANCE)": {
                "VALOR_REAL": 46600.0, "PROJ": 93200.0, "VALOR_NEGOCIADO": 125400.0,
                "STATUS": "85% LIBERADO", "MINUTOS_PAUSA": 40, "DISCADAS": 1200, 
                "ALO": 450, "CPC": 120, "CPCA": 95, "PROMESSAS_N": 70,
                "P1": "00:10:00", "P2": "00:10:00", "LANCHE": "00:20:00", "BANHEIRO": "00:00:00"
            },
            "MARCOS (SABOTAGEM)": {
                "VALOR_REAL": 0.0, "PROJ": 0.0, "VALOR_NEGOCIADO": 0.0,
                "STATUS": "0% PENDENTE", "MINUTOS_PAUSA": 125, "DISCADAS": 800, 
                "ALO": 12, "CPC": 0, "CPCA": 0, "PROMESSAS_N": 0,
                "P1": "00:25:00", "P2": "00:30:00", "LANCHE": "01:00:00", "BANHEIRO": "00:30:00"
            },
            "JULIA (VÁCUO)": {
                "VALOR_REAL": 800.0, "PROJ": 1600.0, "VALOR_NEGOCIADO": 2500.0,
                "STATUS": "12% PENDENTE", "MINUTOS_PAUSA": 55, "DISCADAS": 500, 
                "ALO": 85, "CPC": 8, "CPCA": 4, "PROMESSAS_N": 1,
                "P1": "00:10:00", "P2": "00:10:00", "LANCHE": "00:20:00", "BANHEIRO": "00:15:00"
            }
        },
        "DISCADOR": {"PEN": 65, "MAILING": "Ativo 2026", "TOTAL_DISCADAS": 2500},
        "TELEFONIA": {"LAT": 250, "STATUS": "CRÍTICO", "SERVER": "Vivo Cloud"}
    }

# --- 3. PROCESSAMENTO E CÁLCULOS (X = PROJEÇÃO - 50%) ---
df_list = []
for k, v in st.session_state.db["OPERAÇÃO"].items():
    alo = v.get("ALO", 0)
    disc = v.get("DISCADAS", 1)
    proj = v.get("PROJ", 0.0)
    df_list.append({
        "OPERADOR": k,
        "LOC %": (alo / disc * 100),
        "CPCA": v.get("CPCA", 0),
        "NEGOCIADO": v.get("VALOR_NEGOCIADO", 0.0),
        "REAL": v.get("VALOR_REAL", 0.0),
        "PROJEÇÃO": proj,
        "X (-50%)": proj * 0.5,
        "STATUS": v.get("STATUS", "PENDENTE"),
        "MINUTOS": v.get("MINUTOS_PAUSA", 0),
        "PROMESSAS": v.get("PROMESSAS_N", 0)
    })
df_audit = pd.DataFrame(df_list)

# --- 4. CABEÇALHO DE COMANDO ---
st.markdown(f"""
    <div class="manifesto-container">
        <div class="quote-text">"Enquanto o mundo olha para o avião que sobe, eu governo o código que o faz voar."</div>
        <div class="signature">👊🚀📊⚖️🏁💎 — Comandante S.A.</div>
    </div>
""", unsafe_allow_html=True)

st.title("🛰️ S.P.A. - SENTINELA DE PERFORMANCE ATIVA")
st.write(f"**CONSOLIDE 01-06** | SISTEMA SINCRONIZADO | {datetime.now().strftime('%H:%M:%S')}")

# --- 5. ESTRUTURA DE ABAS (VISÃO INTEGRAL) ---
aba1, aba2, aba3, aba4, aba5, aba6 = st.tabs([
    "👑 01. COCKPIT", "👥 02. GESTÃO", "🧠 03. DISCADOR", 
    "📡 04. TELEFONIA", "📂 05. RELATÓRIOS", "⚖️ 06. JURÍDICO"
])

# --- ABA 01: COCKPIT (VISÃO CONSOLIDADA) ---
with aba1:
    st.header("📊 Cockpit Consolidado")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Localização Geral", f"{(df_audit['LOC %'].mean()):.1f}%", "EFICÁCIA")
    m2.metric("Contatos (CPCA)", f"{int(df_audit['CPCA'].sum())}", "MÃO NA MASSA")
    m3.metric("Financeiro Real", f"R$ {df_audit['REAL'].sum():,.2f}", "RECUPERADO")
    m4.metric("Pausa Equipe", f"{df_audit['MINUTOS'].sum()} min", delta_color="inverse")

    st.divider()
    st.subheader("🏁 Tabela da Favelinha")
    st.dataframe(df_audit[["OPERADOR", "LOC %", "CPCA", "NEGOCIADO", "REAL", "PROJEÇÃO", "X (-50%)", "STATUS"]].style.format({
        "REAL": "R$ {:,.2f}", "PROJEÇÃO": "R$ {:,.2f}", "X (-50%)": "R$ {:,.2f}", 
        "NEGOCIADO": "R$ {:,.2f}", "LOC %": "{:.1f}%"
    }), use_container_width=True)

# --- ABA 02: GESTÃO (INCLUSÃO DE CPCA E LOCALIZAÇÃO) ---
with aba2:
    st.header("👥 Anatomia do Funil Individual")
    op_sel = st.selectbox("Selecione Operador para Auditoria:", df_audit["OPERADOR"].tolist())
    res_op = df_audit[df_audit["OPERADOR"] == op_sel].iloc[0]
    
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Taxa Localização", f"{res_op['LOC %']:.1f}%")
    c2.metric("CPCA (Contatos)", int(res_op["CPCA"]))
    c3.metric("Valor Negociado", f"R$ {res_op['NEGOCIADO']:,.2f}")
    c4.metric("Promessas (Nº)", int(res_op["PROMESSAS"]))
    
    st.divider()
    p_raw = st.session_state.db["OPERAÇÃO"][op_sel]
    st.info(f"Monitor de Pausas: P1: {p_raw['P1']} | P2: {p_raw['P2']} | Lanche: {p_raw['LANCHE']} | Banheiro: {p_raw['BANHEIRO']}")

# --- ABA 03: DISCADOR ---
with aba3:
    st.header("🧠 Estratégia de Discador")
    st.metric("IPI (Padrão Ouro)", f"{st.session_state.db['DISCADOR']['PEN']}%")
    st.write(f"Mailing em uso: **{st.session_state.db['DISCADOR']['MAILING']}**")

# --- ABA 04: TELEFONIA ---
with aba4:
    st.header("📡 Infraestrutura de Rede")
    st.metric("Latência", f"{st.session_state.db['TELEFONIA']['LAT']}ms")
    st.error(f"Servidor: {st.session_state.db['TELEFONIA']['SERVER']} | Status: {st.session_state.db['TELEFONIA']['STATUS']}")

# --- ABA 05: RELATÓRIOS (CORREÇÃO DE ACENTOS) ---
with aba5:
    st.header("📂 Exportação de Dados")
    csv = df_audit.to_csv(index=False).encode('utf-8-sig')
    st.download_button("📥 EXPORTAR AUDITORIA V55", csv, "S_A_SPA_AUDITORIA.csv", "text/csv")

# --- ABA 06: JURÍDICO ---
with aba6:
    st.header("⚖️ Auditoria de Status")
    st.table(df_audit[["OPERADOR", "STATUS"]])
