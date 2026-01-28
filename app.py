import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. CONFIGURAÇÃO DE AMBIENTE ---
st.set_page_config(page_title="S.P.A. MASTER - SIDNEY ALMEIDA", layout="wide", page_icon="🛡️")

# --- 2. QUANTUM MEMORY: CENÁRIOS INTEGRADOS (ESTANQUES POR ABA) ---
if 'db' not in st.session_state:
    st.session_state.db = {
        "OPERAÇÃO": {
            "ANA (PERFORMANCE)": {"ALO": 1200, "CON": 950, "CPC": 450, "VALOR": 45800.00, "PROJ": 91600.0, "LEGAL": "Art. 444 CLT (Conformidade)", "FOR": "Script nível 5. Alta conversão de mailing classe A."},
            "MARCOS (SABOTAGEM)": {"ALO": 2500, "CON": 50, "CPC": 5, "VALOR": 0.00, "PROJ": 0.0, "LEGAL": "Art. 482, 'e' CLT (Desídia)", "FOR": "Cabo Desconectado para forçar ociosidade."},
            "RICARDO (OMISSÃO)": {"ALO": 800, "CON": 780, "CPC": 700, "VALOR": 150.00, "PROJ": 300.0, "LEGAL": "Art. 482, 'h' CLT (Insubordinação)", "FOR": "Mudo Proposital/Retenção de linha."}
        },
        "DISCADOR": {
            "MAILING_VIVO_JANEIRO": {"TOTAL_LEADS": 150000, "PENETRACAO": 65, "AUTONOMIA": 12.5, "SPC_STATUS": "HIGIENIZADO", "QUALIDADE": "QUENTE", "TICKET_MEDIO": 185.0},
            "BASE_RECOVERY_ESTEIRA": {"TOTAL_LEADS": 300000, "PENETRACAO": 15, "AUTONOMIA": 2.1, "SPC_STATUS": "PENDENTE", "QUALIDADE": "FRIO", "TICKET_MEDIO": 420.0}
        },
        "TELEFONIA": {
            "VIVO (TRUNK PRINCIPAL)": {"STATUS": "BLOQUEADO", "LATENCIA": "250ms", "FOR": "Queda de Link SIP / Instabilidade de Jitter."},
            "SIPvox (CONTINGÊNCIA)": {"STATUS": "LIBERADO", "LATENCIA": "25ms", "FOR": "Rota Premium Ativa - Estável."}
        }
    }

# --- 3. INTERFACE DE NAVEGAÇÃO POR DEPARTAMENTOS ---
st.title("🛰️ S.P.A. - SENTINELA DE PERFORMANCE ATIVA")
st.write(f"**Servidor Operacional** | 📅 {datetime.now().strftime('%d/%m/%Y')} | 👤 Comandante S.A.")

aba_op, aba_disc, aba_tel, aba_fav = st.tabs([
    "👥 GESTÃO DE OPERADORES", 
    "🧠 ESTRATÉGIA DE DISCADOR", 
    "📡 INFRA TELEFONIA", 
    "📊 TABELA DA FAVELINHA"
])

# --- ABA 1: OPERAÇÃO (CADA UM NO SEU QUADRADO) ---
with aba_op:
    st.header("📈 Dashboard de Performance e Blindagem Jurídica")
    col1, col2 = st.columns([1, 2])
    
    with col1:
        op_sel = st.selectbox("Selecione o Operador para Auditoria:", list(st.session_state.db["OPERAÇÃO"].keys()), key="op_key")
        d_op = st.session_state.db["OPERAÇÃO"][op_sel]
        
        # Regra do X: Projeção - 50%
        x_calc = d_op["PROJ"] * 0.50
        
        st.divider()
        st.subheader("🛠️ Ação Imediata")
        st.write(f"**Status:** {'🔴 BLOQUEADO' if d_op['VALOR'] == 0 else '🟢 LIBERADO'}")
        st.write(f"**Enquadramento:** {d_op['LEGAL']}")
        
    with col2:
        st.subheader("📊 Métricas de Esteira (Alô/Contato/CPC)")
        m1, m2, m3 = st.columns(3)
        m1.metric("ALÔ (SISTEMA)", d_op["ALO"])
        m2.metric("CONTATO (HUMANO)", d_op["CON"])
        m3.metric("CPC (EFETIVO)", d_op["CPC"])
        
        m4, m5 = st.columns(2)
        m4.metric("VALOR RECUPERADO", f"R$ {d_op['VALOR']:,.2f}")
        m5.metric("PROJEÇÃO X (-50%)", f"R$ {x_calc:,.2f}")
        
        st.info(f"**Dossiê Forense:** {d_op['FOR']}")

# --- ABA 2: DISCADOR (TERMINOLOGIA TÉCNICA) ---
with aba_disc:
    st.header("🧠 Inteligência de Malha e Capacity")
    disc_sel = st.selectbox("Selecione a Carga/Mailing:", list(st.session_state.db["DISCADOR"].keys()), key="disc_key")
    d_d = st.session_state.db["DISCADOR"][disc_sel]
    
    d1, d2, d3, d4 = st.columns(4)
    d1.metric("QUALIDADE DO MEIO", d_d["QUALIDADE"])
    d2.metric("AUTONOMIA (DIAS)", d_d["AUTONOMIA"])
    d3.metric("STATUS SPC/SERASA", d_d["SPC_STATUS"])
    d4.metric("PENETRAÇÃO DE BASE", f"{d_d['PENETRACAO']}%")
    
    st.divider()
    st.write(f"**Ticket Médio da Carga:** R$ {d_d['TICKET_MEDIO']:,.2f}")
    st.write(f"**Leads Ativos na Esteira:** {d_d['TOTAL_LEADS']}")

# --- ABA 3: TELEFONIA (INFRAESTRUTURA) ---
with aba_tel:
    st.header("📡 Monitoramento de Conectividade e Trunks")
    tel_sel = st.selectbox("Selecione o Trunk IP:", list(st.session_state.db["TELEFONIA"].keys()), key="tel_key")
    d_t = st.session_state.db["TELEFONIA"][tel_sel]
    
    t1, t2 = st.columns(2)
    t1.metric("STATUS DO LINK", d_t["STATUS"])
    t2.metric("LATÊNCIA DE ROTA", d_t["LATENCIA"])
    
    st.divider()
    st.warning(f"**Análise Forense de Telefonia:** {d_t['FOR']}")

# --- ABA 4: FAVELINHA (O RESUMO DE TUDO) ---
with aba_fav:
    st.header("📊 Tabela da Favelinha - Resumo Executivo")
    st.write("Abaixo o consolidado dos operadores auditados nesta sessão.")
    # Exemplo de como a tabela apareceria acumulada
    data_fav = {
        "Operador": ["ANA", "MARCOS", "RICARDO"],
        "Alô": [1200, 2500, 800],
        "CPC": [450, 5, 700],
        "Valor": [45800.0, 0.0, 150.0],
        "Projeção X": [45800.0, 0.0, 150.0],
        "Status Jurídico": ["LIBERADO", "BLOQUEADO (Art. 482)", "BLOQUEADO (Art. 482)"]
    }
    st.table(data_fav)
    
