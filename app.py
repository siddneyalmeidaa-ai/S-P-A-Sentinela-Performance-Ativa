import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. CONFIGURAÇÃO DE INTERFACE (PADRÃO OURO S.A.) ---
st.set_page_config(page_title="S.P.A. MASTER - SIDNEY ALMEIDA", layout="wide", page_icon="🛰️")

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

# --- 2. BANCO DE DADOS INTEGRAL (QUANTUM MEMORY V35) ---
if 'db' not in st.session_state:
    st.session_state.db = {
        "OPERAÇÃO": {
            "ANA (PERFORMANCE)": {
                "VALOR": 45800.0, "PROJ": 91600.0, "STATUS": "85% LIBERADO", "LEGAL": "Art. 444 CLT",
                "LOG_TIME": "06:12:00", "PROD": 92, "MINUTOS_PAUSA": 40,
                "ALO": 450, "CONTATOS": 380, "CPC": 120, "CPCA": 85, "PROMESSAS": 70,
                "P1": "00:10:00", "P2": "00:10:00", "LANCHE": "00:20:00", "BANHEIRO": "00:00:00"
            },
            "MARCOS (SABOTAGEM)": {
                "VALOR": 0.0, "PROJ": 0.0, "STATUS": "0% BLOQUEADO", "LEGAL": "Art. 482 CLT",
                "LOG_TIME": "04:30:00", "PROD": 0, "MINUTOS_PAUSA": 125,
                "ALO": 12, "CONTATOS": 2, "CPC": 0, "CPCA": 0, "PROMESSAS": 0,
                "P1": "00:25:00", "P2": "00:30:00", "LANCHE": "01:00:00", "BANHEIRO": "00:30:00"
            },
            "JULIA (VÁCUO)": {
                "VALOR": 800.0, "PROJ": 1600.0, "STATUS": "12% OK", "LEGAL": "Art. 482 CLT",
                "LOG_TIME": "02:20:00", "PROD": 12, "MINUTOS_PAUSA": 55,
                "ALO": 85, "CONTATOS": 40, "CPC": 8, "CPCA": 2, "PROMESSAS": 1,
                "P1": "00:10:00", "P2": "00:10:00", "LANCHE": "00:20:00", "BANHEIRO": "00:15:00"
            }
        },
        "DISCADOR": {"PEN": 65, "SPC": 15, "MAILING": "Ativo 2026"},
        "TELEFONIA": {"LAT": 250, "STATUS": "CRÍTICO", "SERVER": "Vivo Cloud"}
    }

# Cálculos Consolidado V35
df_audit = pd.DataFrame([
    {
        "OPERADOR": k, 
        "ALÔ": v.get("ALO", 0),
        "CPC": v.get("CPC", 0),
        "CPCA": v.get("CPCA", 0),
        "PROMESSAS": v.get("PROMESSAS", 0),
        "VALOR": v['VALOR'],
        "STATUS": v["STATUS"],
        "MINUTOS": v.get("MINUTOS_PAUSA", 0)
    }
    for k, v in st.session_state.db["OPERAÇÃO"].items()
])

total_min_pausa = df_audit["MINUTOS"].sum()
limite_alerta = 45

# --- 3. CABEÇALHO ---
st.markdown(f"""
    <div class="manifesto-container">
        <div class="quote-text">"Enquanto o mundo olha para o avião que sobe, eu governo o código que o faz voar."</div>
        <div class="signature">👊🚀📊⚖️🏁💎 — Frase autoral: Comandante S.A.</div>
    </div>
""", unsafe_allow_html=True)

st.title("🛰️ S.P.A. - SENTINELA DE PERFORMANCE ATIVA")
st.write(f"**CONSOLIDE 01-06** | SISTEMA INTEGRAL | {datetime.now().strftime('%H:%M:%S')}")

# --- 4. INTERFACE DE 6 ABAS ---
aba1, aba2, aba3, aba4, aba5, aba6 = st.tabs([
    "👑 01. VISÃO ESTRATÉGICA", "👥 02. GESTÃO DE OPERADORES", "🧠 03. ESTRATÉGIA DE DISCADOR", 
    "📡 04. INFRA TELEFONIA", "📂 05. CENTRAL DE RELATÓRIOS", "⚖️ 06. VISÃO JURÍDICA"
])

# --- ABA 01: VISÃO GERAL (O CONSOLIDADO) ---
with aba1:
    st.header("📊 Cockpit: Conversão, Promessas e Localização")
    
    # Quadrante de Ouro
    q1, q2, q3, q4, q5 = st.columns(5)
    q1.metric("Localização (Alô)", f"{df_audit['ALÔ'].sum()}")
    q2.metric("Conversão (CPC)", f"{df_audit['CPC'].sum()}")
    q3.metric("Promessas Total", f"{df_audit['PROMESSAS'].sum()}", delta="ALVO JURÍDICO")
    q4.metric("Financeiro", f"R$ {df_audit['VALOR'].sum():,.2f}")
    
    status_cor = "inverse" if total_min_pausa > limite_alerta else "normal"
    q5.metric("Pausa Coletiva", f"{total_min_pausa} min", 
              f"{total_min_pausa - limite_alerta}m excesso" if total_min_pausa > limite_alerta else "OK", 
              delta_color=status_cor)

    st.divider()
    st.subheader("🏁 Tabela da Favelinha - Auditoria de Resultado")
    st.dataframe(df_audit[["OPERADOR", "ALÔ", "CPC", "CPCA", "PROMESSAS", "VALOR", "STATUS"]], use_container_width=True)

# --- ABA 02: GESTÃO DE OPERADORES ---
with aba2:
    st.header("👥 Anatomia do Funil Individual")
    op = st.selectbox("Selecione o Alvo:", list(st.session_state.db["OPERAÇÃO"].keys()), key="v35_op")
    data = st.session_state.db["OPERAÇÃO"][op]
    
    # Detalhe do quadrante
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Alô (Localização)", data["ALO"])
    c2.metric("CPC (Conversão)", data["CPC"])
    c3.metric("Promessas (Resultado)", data["PROMESSAS"], delta=f"{int((data['PROMESSAS']/data['ALO'])*100) if data['ALO']>0 else 0}% Efic.")
    c4.metric("Pausa Individual", f"{data['MINUTOS_PAUSA']} min")
    
    st.divider()
    st.subheader("🛰️ Monitoramento de Pausas Detalhado")
    p1, p2, p3, p4 = st.columns(4)
    p1.info(f"P1: {data['P1']}")
    p2.info(f"P2: {data['P2']}")
    p3.success(f"Lanche: {data['LANCHE']}")
    p4.warning(f"Banheiro: {data['BANHEIRO']}")

# --- ABAS DE APOIO ---
with aba3: st.header("🧠 Mailing e Penetração"); st.progress(st.session_state.db['DISCADOR']['PEN'])
with aba4: st.header("📡 Status de Rede"); st.error(f"Latência: {st.session_state.db['TELEFONIA']['LAT']}ms")
with aba5: st.header("📂 Exportação Blindada"); st.download_button("Baixar Dossiê", df_audit.to_html(), "S_A_AUDIT_V35.html", "text/html")
with aba6: st.header("⚖️ Auditoria Jurídica"); st.table(df_audit[["OPERADOR", "STATUS"]])
