import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. CONFIGURAÇÃO DE INTERFACE PADRÃO OURO ---
st.set_page_config(page_title="S.P.A. - SENTINELA INTEGRAL", layout="wide", page_icon="⚖️")

# --- 2. QUANTUM MEMORY: CENÁRIOS TÉCNICOS INTEGRADOS (DADOS ACUMULADOS) ---
if 'db_ficticio' not in st.session_state:
    st.session_state.db_ficticio = {
        # OPERAÇÃO: ALÔ -> CONTATO -> CPC | VALOR | PROJEÇÃO | LEI | PERDA
        "ANA (PERFORMANCE)": {
            "ALO": 1200, "CON": 950, "CPC": 450, "VALOR": 45800.00, "STATUS": "LIBERADO", 
            "TAB": "Promessa Firmada", "FOR": "Script nível 5. Alta conversão de mailing classe A.", 
            "LEGAL": "Art. 444 CLT (Conformidade)", "PERDA": 0.0, "PROJ": 91600.0},
        
        "MARCOS (CABO DESCONECTADO)": {
            "ALO": 2500, "CON": 50, "CPC": 5, "VALOR": 0.00, "STATUS": "BLOQUEADO", 
            "TAB": "Sabotagem de Hardware", "FOR": "Desconexão física para ociosidade forçada.", 
            "LEGAL": "Art. 482, 'e' CLT (Desídia/Sabotagem)", "PERDA": 1250.0, "PROJ": 0.0},
            
        "RICARDO (MUDO PROPOSITAL)": {
            "ALO": 800, "CON": 780, "CPC": 700, "VALOR": 150.00, "STATUS": "BLOQUEADO", 
            "TAB": "Retenção de Linha", "FOR": "Uso de mute para evitar atendimento real.", 
            "LEGAL": "Art. 482, 'h' CLT (Insubordinação)", "PERDA": 850.0, "PROJ": 300.0},
            
        "JULIA (VÁCUO/OMISSÃO)": {
            "ALO": 100, "CON": 20, "CPC": 10, "VALOR": 800.00, "STATUS": "BLOQUEADO", 
            "TAB": "Pulo de Rodada", "FOR": "IA-SENTINELA detectou vácuo operacional.", 
            "LEGAL": "Art. 482, 'e' CLT (Desídia)", "PERDA": 450.0, "PROJ": 1600.0},

        # DISCADOR: MEIO | SPC | PENETRAÇÃO | CAPACITY | TICKET
        "MAILING_VIVO_MÓVEL_JAN": {
            "ALO": 150000, "CON": 85000, "CPC": 42000, "VALOR": 0, "STATUS": "PENDENTE",
            "TAB": "AUDITORIA MAILING", "FOR": "Mailing Quente - Alta Penetração.",
            "LEGAL": "LGPD/Compliance", "PERDA": 0.0, "AUTO": 12.5, "SPC": "HIGIENIZADO", "PEN": 65, "TICKET": 185.0, "PROJ": 0},
            
        "ESTEIRA_RECOVERY_SPC": {
            "ALO": 300000, "CON": 45000, "CPC": 9000, "VALOR": 0, "STATUS": "BLOQUEADO",
            "TAB": "ENRIQUECIMENTO", "FOR": "Base morta - Necessita reprocessamento urgente.",
            "LEGAL": "Higienização", "PERDA": 2500.0, "AUTO": 2.1, "SPC": "PENDENTE", "PEN": 15, "TICKET": 420.0, "PROJ": 0},

        "VIVO (TRUNK IP)": {
            "ALO": 500000, "CON": 480000, "CPC": 120000, "STATUS": "BLOQUEADO", 
            "TAB": "Queda de Link", "FOR": "Latência instável no Gateway.", "LEGAL": "SLA Técnica", "PERDA": 5000.0, "PROJ": 0}
    }

if 'historico' not in st.session_state:
    st.session_state.historico = pd.DataFrame(columns=[
        "DATA", "ALVO", "VISAO", "TABULACAO", "VALOR", "ALO", "CONTATO", "CPC", 
        "STATUS", "LEGAL", "PERDA", "PROJECAO_X", "QUALIDADE", "ESTEIRA_SPC", "AUTO"
    ])

# --- 3. BARRA LATERAL: CENTRAL DE COMANDO ---
with st.sidebar:
    st.title("🛰️ S.P.A. MASTER")
    visao_ativa = st.radio("SISTEMA:", ["📈 OPERAÇÃO & JURÍDICO", "🧠 DISCADOR (ESTEIRA)", "📡 TELEFONIA"])
    
    st.divider()
    if visao_ativa == "📈 OPERAÇÃO & JURÍDICO":
        alvo = st.selectbox("ALVO AUDITADO:", ["ANA (PERFORMANCE)", "MARCOS (CABO DESCONECTADO)", "RICARDO (MUDO PROPOSITAL)", "JULIA (VÁCUO/OMISSÃO)"])
    elif visao_ativa == "🧠 DISCADOR (ESTEIRA)":
        alvo = st.selectbox("IDENTIFICAÇÃO DO MEIO:", ["MAILING_VIVO_MÓVEL_JAN", "ESTEIRA_RECOVERY_SPC"])
    else:
        alvo = st.selectbox("CANAL DE REDE:", ["VIVO (TRUNK IP)"])

    d = st.session_state.db_ficticio[alvo]

    if st.button("🚀 EXECUTAR INTEGRAÇÃO TOTAL"):
        # REGRA DO X: PROJEÇÃO - 50%
        x_calc = d.get("PROJ", 0.0) * 0.50
        
        novo = pd.DataFrame([{
            "DATA": datetime.now().strftime("%H:%M:%S"), "ALVO": alvo, "VISAO": visao_ativa,
            "TABULACAO": d.get("TAB"), "VALOR": d.get("VALOR", 0.0), 
            "ALO": d.get("ALO"), "CONTATO": d.get("CON"), "CPC": d.get("CPC"),
            "STATUS": d.get("STATUS"), "LEGAL": d.get("LEGAL"), 
            "PERDA": d.get("PERDA"), "PROJECAO_X": x_calc,
            "QUALIDADE": d.get("MEIO", "N/A"), "ESTEIRA_SPC": d.get("SPC", "N/A"),
            "AUTO": d.get("AUTO", 0)
        }])
        st.session_state.historico = pd.concat([st.session_state.historico, novo], ignore_index=True)

# --- 4. DASHBOARD INTEGRADO (VISUAL MILIONÁRIO) ---
st.title("🛰️ S.P.A. - SENTINELA DE PERFORMANCE ATIVA")

# --- TABELA DA FAVELINHA (SEMPRE VISÍVEL - AÇÃO IMEDIATA) ---
st.subheader("📊 Tabela da Favelinha (Visão de Auditoria)")
if not st.session_state.historico.empty:
    st.table(st.session_state.historico.tail(5)[["ALVO", "ALO", "CPC", "VALOR", "PROJECAO_X", "STATUS", "LEGAL"]])
else:
    st.info("Aguardando sincronização de dados...")

t1, t2, t3 = st.tabs(["👥 OPERAÇÃO & JURÍDICO", "🧠 DISCADOR & CAPACITY", "📡 TELEFONIA"])

with t1:
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("ALVO", alvo)
    c2.metric("RECUPERADO", f"R$ {d.get('VALOR'):,.2f}")
    c3.metric("PROJEÇÃO X (-50%)", f"R$ {d.get('PROJ', 0.0) * 0.5:,.2f}")
    c4.metric("PREJUÍZO OCIOSIDADE", f"R$ {d.get('PERDA'):,.2f}", delta="- PREJUÍZO", delta_color="inverse")

    st.divider()
    col_a, col_b = st.columns([2, 1])
    with col_a:
        st.subheader("🔎 Dossiê Forense")
        st.info(f"**Parecer Técnico:** {d.get('FOR')}")
        st.progress(d["CON"]/d["ALO"] if d["ALO"] > 0 else 0, text=f"Funil Alô -> Contato: {round((d['CON']/d['ALO']*100) if d['ALO']>0 else 0)}%")
        st.progress(d["CPC"]/d["CON"] if d["CON"] > 0 else 0, text=f"Funil Contato -> CPC: {round((d['CPC']/d['CON']*100) if d['CON']>0 else 0)}%")
    with col_b:
        st.subheader("⚖️ Blindagem Legal")
        st.error(f"**Base Legal:** {d.get('LEGAL')}")
        st.write(f"**Status de Operação:** {d.get('STATUS')}")

with t2:
    st.subheader("Inteligência de Mailing e Esteira SPC")
    if visao_ativa == "🧠 DISCADOR (ESTEIRA)":
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("QUALIDADE DO MEIO", d.get("MEIO"))
        c2.metric("ESTEIRA SPC", d.get("SPC"))
        c3.metric("AUTONOMIA", f"{d.get('AUTO')} Dias")
        c4.metric("PENETRAÇÃO", f"{d.get('PEN')}%")
    st.dataframe(st.session_state.historico[st.session_state.historico["VISAO"] == "🧠 DISCADOR (ESTEIRA)"], use_container_width=True)

with t3:
    st.subheader("Status de Rede (Trunk IP)")
    st.dataframe(st.session_state.historico[st.session_state.historico["VISAO"] == "📡 TELEFONIA"], use_container_width=True)

# --- 5. EXPORTAÇÃO ---
st.divider()
st.download_button("📊 GERAR RELATÓRIO PADRÃO OURO (CSV)", st.session_state.historico.to_csv(index=False).encode('utf-8-sig'), "SPA_INTEGRAL_FINAL.csv")
            
