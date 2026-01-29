import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. CONFIGURAÇÃO DE INTERFACE (PADRÃO OURO S.A.) ---
st.set_page_config(page_title="S.P.A. MASTER - SIDNEY ALMEIDA", layout="wide", page_icon="🛰️")

# Correção do erro de sintaxe do print: unsafe_allow_html
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;} header {visibility: hidden;} footer {visibility: hidden;}
    .stDeployButton {display:none;}
    .manifesto-container {
        background-color: #050505;
        border-left: 5px solid #00FF41;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 25px;
    }
    .quote-text { color: #00FF41; font-size: 18px; font-weight: bold; font-style: italic; }
    .signature { color: #D4AF37; font-size: 12px; text-transform: uppercase; letter-spacing: 2px; }
    </style>
""", unsafe_allow_html=True)

# --- 2. BANCO DE DADOS INTEGRAL (QUANTUM MEMORY V39) ---
if 'db' not in st.session_state:
    st.session_state.db = {
        "OPERAÇÃO": {
            "ANA (PERFORMANCE)": {
                "VALOR_REAL": 45800.0, "PROJ": 91600.0, "STATUS": "85% LIBERADO",
                "LOG_TIME": "06:12:00", "MINUTOS_PAUSA": 40, "DISCADAS": 1200,
                "ALO": 450, "CPC": 120, "CPCA": 85, "PROMESSAS_QTD": 70,
                "P1": "00:10:00", "P2": "00:10:00", "LANCHE": "00:20:00", "BANHEIRO": "00:00:00"
            },
            "MARCOS (SABOTAGEM)": {
                "VALOR_REAL": 0.0, "PROJ": 0.0, "STATUS": "0% BLOQUEADO",
                "LOG_TIME": "04:30:00", "MINUTOS_PAUSA": 125, "DISCADAS": 800,
                "ALO": 12, "CPC": 0, "CPCA": 0, "PROMESSAS_QTD": 0,
                "P1": "00:25:00", "P2": "00:30:00", "LANCHE": "01:00:00", "BANHEIRO": "00:30:00"
            },
            "JULIA (VÁCUO)": {
                "VALOR_REAL": 800.0, "PROJ": 1600.0, "STATUS": "12% OK",
                "LOG_TIME": "02:20:00", "MINUTOS_PAUSA": 55, "DISCADAS": 500,
                "ALO": 85, "CPC": 8, "CPCA": 2, "PROMESSAS_QTD": 1,
                "P1": "00:10:00", "P2": "00:10:00", "LANCHE": "00:20:00", "BANHEIRO": "00:15:00"
            }
        },
        "DISCADOR": {"PEN": 65, "MAILING": "Ativo 2026", "TOTAL_DISCADAS_GERAL": 2500},
        "TELEFONIA": {"LAT": 250, "STATUS": "CRÍTICO", "SERVER": "Vivo Cloud"}
    }

# Processamento de Auditoria (Tratamento de Erros de Coluna)
df_list = []
for k, v in st.session_state.db["OPERAÇÃO"].items():
    disc = v.get("DISCADAS", 1)
    df_list.append({
        "OPERADOR": k,
        "LOC %": f"{(v.get('ALO', 0) / disc * 100):.1f}%",
        "ALÔ": v.get("ALO", 0),
        "CPC": v.get("CPC", 0),
        "PROMESSAS (Nº)": v.get("PROMESSAS_QTD", 0),
        "VALOR REAL": v.get("VALOR_REAL", 0.0),
        "PROJEÇÃO": v.get("PROJ", 0.0),
        "X (-50%)": v.get("PROJ", 0.0) * 0.5,
        "STATUS": v.get("STATUS", "PENDENTE"),
        "MINUTOS": v.get("MINUTOS_PAUSA", 0)
    })

df_audit = pd.DataFrame(df_list)
total_pausa_equipe = df_audit["MINUTOS"].sum()

# --- 3. CABEÇALHO ---
st.markdown(f"""
    <div class="manifesto-container">
        <div class="quote-text">"Enquanto o mundo olha para o avião que sobe, eu governo o código que o faz voar."</div>
        <div class="signature">👊🚀📊⚖️🏁💎 — Frase autoral: Comandante S.A.</div>
    </div>
""", unsafe_allow_html=True)

st.title("🛰️ S.P.A. - SENTINELA DE PERFORMANCE ATIVA")
st.write(f"**CONSOLIDE 01-06** | SISTEMA INTEGRAL | {datetime.now().strftime('%H:%M:%S')}")

# --- 4. ESTRUTURA DE 6 ABAS (REGRA ACUMULATIVA) ---
aba1, aba2, aba3, aba4, aba5, aba6 = st.tabs([
    "👑 01. COCKPIT VISÃO CONSOLIDADA", "👥 02. GESTÃO DE OPERADORES", "🧠 03. ESTRATÉGIA DE DISCADOR", 
    "📡 04. INFRA TELEFONIA", "📂 05. CENTRAL DE RELATÓRIOS", "⚖️ 06. VISÃO JURÍDICA"
])

# --- ABA 01: COCKPIT VISÃO CONSOLIDADA (RESUMO GERAL) ---
with aba1:
    st.header("📊 Cockpit Estratégico Unificado")
    
    # Linha 1: Operacional e Mailing
    c1, c2, c3 = st.columns(3)
    total_alo = df_audit["ALÔ"].sum()
    total_disc = st.session_state.db["DISCADOR"]["TOTAL_DISCADAS_GERAL"]
    taxa_loc = (total_alo / total_disc * 100) if total_disc > 0 else 0
    c1.metric("Taxa Localização (Mailing)", f"{taxa_loc:.1f}%", "EFICÁCIA")
    
    # Promessas em NÚMERO (conforme solicitado)
    total_prom = df_audit["PROMESSAS (Nº)"].sum()
    c2.metric("Promessas (Nº)", f"{total_prom} Acordos", "VOLUME")
    
    c3.metric("Financeiro Real", f"R$ {df_audit['VALOR REAL'].sum():,.2f}", "RECUPERADO")

    # Linha 2: Infra e Comportamento
    c4, c5, c6 = st.columns(3)
    c4.metric("Latência Rede (Aba 04)", f"{st.session_state.db['TELEFONIA']['LAT']}ms", st.session_state.db['TELEFONIA']['STATUS'], delta_color="inverse")
    c5.metric("IPI Discador (Aba 03)", f"{st.session_state.db['DISCADOR']['PEN']}%", "PENETRAÇÃO")
    
    # Alerta de Pausa Coletiva
    cor_pausa = "inverse" if total_pausa_equipe > 45 else "normal"
    c6.metric("Pausa Coletiva (Aba 02)", f"{total_pausa_equipe} min", f"{total_pausa_equipe-45}m excesso" if total_pausa_equipe > 45 else "DENTRO DO LIMITE", delta_color=cor_pausa)

    st.divider()
    st.subheader("🏁 Tabela da Favelinha - Auditoria de X")
    st.dataframe(df_audit.style.format({
        "VALOR REAL": "R$ {:,.2f}", "PROJEÇÃO": "R$ {:,.2f}", "X (-50%)": "R$ {:,.2f}"
    }), use_container_width=True)

# --- ABA 02: GESTÃO DE OPERADORES ---
with aba2:
    st.header("👥 Anatomia do Funil e Pausas")
    op = st.selectbox("Selecione o Operador:", list(st.session_state.db["OPERAÇÃO"].keys()), key="v39_op")
    data = st.session_state.db["OPERAÇÃO"][op]
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Alô", data.get("ALO", 0))
    col2.metric("CPC", data.get("CPC", 0))
    col3.metric("Promessas (Nº)", data.get("PROMESSAS_QTD", 0))
    col4.metric("Tempo em Pausa", f"{data.get('MINUTOS_PAUSA', 0)} min")
    
    st.divider()
    st.subheader("🛰️ Detalhes de Log")
    st.info(f"Tempo Logado: {data.get('LOG_TIME')}")
    st.write(f"P1: {data.get('P1')} | P2: {data.get('P2')} | Lanche: {data.get('LANCHE')} | Banheiro: {data.get('BANHEIRO')}")

# --- ABAS TÉCNICAS (CONFORMIDADE ACUMULATIVA) ---
with aba3:
    st.header("🧠 Estratégia de Discador")
    st.write(f"Status do Mailing: **{st.session_state.db['DISCADOR']['MAILING']}**")
    st.metric("Índice de Penetração (IPI)", f"{st.session_state.db['DISCADOR']['PEN']}%")

with aba4:
    st.header("📡 Infra Telefonia")
    st.write(f"Servidor: {st.session_state.db['TELEFONIA']['SERVER']}")
    st.error(f"Latência detectada: {st.session_state.db['TELEFONIA']['LAT']}ms")

with aba5:
    st.header("📂 Central de Relatórios")
    st.download_button("📥 Exportar Auditor
    
