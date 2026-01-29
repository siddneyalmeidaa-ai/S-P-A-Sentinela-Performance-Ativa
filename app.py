import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. CONFIGURAÇÃO DE INTERFACE (PADRÃO OURO S.A.) ---
st.set_page_config(page_title="S.P.A. MASTER - SIDNEY ALMEIDA", layout="wide", page_icon="🛰️")

# CORREÇÃO CRÍTICA: unsafe_allow_html=True (conforme erro no print 04:07)
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

# --- 2. BANCO DE DADOS INTEGRAL (QUANTUM MEMORY V38) ---
if 'db' not in st.session_state:
    st.session_state.db = {
        "OPERAÇÃO": {
            "ANA (PERFORMANCE)": {
                "VALOR_REAL": 45800.0, "VALOR_PROMESSA": 62000.0, "PROJ": 91600.0, "STATUS": "85% LIBERADO",
                "LOG_TIME": "06:12:00", "MINUTOS_PAUSA": 40, "DISCADAS": 1200,
                "ALO": 450, "CPC": 120, "CPCA": 85, "PROMESSAS": 70,
                "P1": "00:10:00", "P2": "00:10:00", "LANCHE": "00:20:00", "BANHEIRO": "00:00:00"
            },
            "MARCOS (SABOTAGEM)": {
                "VALOR_REAL": 0.0, "VALOR_PROMESSA": 0.0, "PROJ": 0.0, "STATUS": "0% BLOQUEADO",
                "LOG_TIME": "04:30:00", "MINUTOS_PAUSA": 125, "DISCADAS": 800,
                "ALO": 12, "CPC": 0, "CPCA": 0, "PROMESSAS": 0,
                "P1": "00:25:00", "P2": "00:30:00", "LANCHE": "01:00:00", "BANHEIRO": "00:30:00"
            },
            "JULIA (VÁCUO)": {
                "VALOR_REAL": 800.0, "VALOR_PROMESSA": 2500.0, "PROJ": 1600.0, "STATUS": "12% OK",
                "LOG_TIME": "02:20:00", "MINUTOS_PAUSA": 55, "DISCADAS": 500,
                "ALO": 85, "CPC": 8, "CPCA": 2, "PROMESSAS": 1,
                "P1": "00:10:00", "P2": "00:10:00", "LANCHE": "00:20:00", "BANHEIRO": "00:15:00"
            }
        },
        "DISCADOR": {"PEN": 65, "MAILING": "Ativo 2026", "TOTAL_DISCADAS_GERAL": 2500},
        "TELEFONIA": {"LAT": 250, "STATUS": "CRÍTICO", "SERVER": "Vivo Cloud"}
    }

# Lógica de Auditoria V38 (Calculando Taxa de Localização do Mailing)
df_data = []
for k, v in st.session_state.db["OPERAÇÃO"].items():
    # Regra: X = Projeção - 50%
    proj = v.get("PROJ", 0.0)
    x_calculado = proj * 0.5
    
    # Taxa de Localização Individual
    loc_ind = (v.get("ALO", 0) / v.get("DISCADAS", 1)) * 100
    
    df_data.append({
        "OPERADOR": k,
        "LOC %": f"{loc_ind:.1f}%",
        "ALÔ": v.get("ALO", 0),
        "CPC": v.get("CPC", 0),
        "PROMESSA (R$)": v.get("VALOR_PROMESSA", 0.0),
        "REAL (R$)": v.get("VALOR_REAL", 0.0),
        "PROJEÇÃO": proj,
        "X (-50%)": x_calculado,
        "STATUS": v.get("STATUS", "PENDENTE"),
        "PAUSA": v.get("MINUTOS_PAUSA", 0)
    })

df_audit = pd.DataFrame(df_data)
total_pausa = df_audit["PAUSA"].sum()

# --- 3. CABEÇALHO ---
st.markdown(f"""
    <div class="manifesto-container">
        <div class="quote-text">"Enquanto o mundo olha para o avião que sobe, eu governo o código que o faz voar."</div>
        <div class="signature">👊🚀📊⚖️🏁💎 — Frase autoral: Comandante S.A.</div>
    </div>
""", unsafe_allow_html=True)

st.title("🛰️ S.P.A. - SENTINELA DE PERFORMANCE ATIVA")
st.write(f"**CONSOLIDE 01-06** | SISTEMA SINCRONIZADO | {datetime.now().strftime('%H:%M:%S')}")

# --- 4. AS 6 ABAS (REGRA ACUMULATIVA) ---
aba1, aba2, aba3, aba4, aba5, aba6 = st.tabs([
    "👑 01. VISÃO ESTRATÉGICA", "👥 02. GESTÃO DE OPERADORES", "🧠 03. ESTRATÉGIA DE DISCADOR", 
    "📡 04. INFRA TELEFONIA", "📂 05. CENTRAL DE RELATÓRIOS", "⚖️ 06. VISÃO JURÍDICA"
])

# --- ABA 01: COCKPIT CONSOLIDADO ---
with aba1:
    st.header("📊 Cockpit: Localização, Promessas e Valor")
    
    c1, c2, c3, c4, c5 = st.columns(5)
    
    # Taxa de Localização do Mailing (Total Alô / Total Discadas)
    total_alo = df_audit["ALÔ"].sum()
    total_disc = st.session_state.db["DISCADOR"]["TOTAL_DISCADAS_GERAL"]
    taxa_loc_geral = (total_alo / total_disc) * 100
    c1.metric("Taxa Localização", f"{taxa_loc_geral:.1f}%", "EFIC. MAILING")
    
    c2.metric("Promessas Total", f"R$ {df_audit['PROMESSA (R$)'].sum():,.2f}")
    c3.metric("Financeiro Real", f"R$ {df_audit['REAL (R$)'].sum():,.2f}", "TOTAL RECUPERADO")
    
    # Conversão de CPC Geral
    conv_cpc = (df_audit["CPC"].sum() / total_alo) * 100 if total_alo > 0 else 0
    c4.metric("Conversão CPC", f"{conv_cpc:.1f}%")
    
    # Alerta de Pausa (Vermelho se > 45)
    pausa_color = "inverse" if total_pausa > 45 else "normal"
    c5.metric("Pausa Coletiva", f"{total_pausa} min", f"{total_pausa-45}m excesso" if total_pausa > 45 else "OK", delta_color=pausa_color)

    st.divider()
    st.subheader("🏁 Tabela da Favelinha - Auditoria de X (-50%)")
    st.dataframe(df_audit.style.format({
        "PROMESSA (R$)": "R$ {:,.2f}", "REAL (R$)": "R$ {:,.2f}", 
        "PROJEÇÃO": "R$ {:,.2f}", "X (-50%)": "R$ {:,.2f}"
    }), use_container_width=True)

# --- ABA 02: GESTÃO DE OPERADORES ---
with aba2:
    st.header("👥 Anatomia do Funil Individual")
    op = st.selectbox("Selecione o Alvo:", list(st.session_state.db["OPERAÇÃO"].keys()))
    data = st.session_state.db["OPERAÇÃO"][op]
    
    f1, f2, f3, f4 = st.columns(4)
    f1.metric("Alô (Localização)", data["ALO"])
    f2.metric("CPC (Conversão)", data["CPC"])
    f3.metric("Promessa Valor", f"R$ {data['VALOR_PROMESSA']:,.2f}")
    f4.metric("Pausa Individual", f"{data['MINUTOS_PAUSA']} min")
    
    st.divider()
    st.subheader("🛰️ Monitoramento de Pausas")
    p1, p2, p3, p4 = st.columns(4)
    p1.info(f"P1: {data['P1']}")
    p2.info(f"P2: {data['P2']}")
    p3.success(f"Lanche: {data['LANCHE']}")
    p4.warning(f"Banheiro: {data['BANHEIRO']}")

# --- ABAS DE INFRA (RESTURADAS) ---
with aba3: st.header("🧠 Estratégia de Discador"); st.metric("IPI (Penetração)", f"{st.session_state.db['DISCADOR']['PEN']}%")
with aba4: st.header("📡 Infra Telefonia"); st.error(f"Latência: {st.session_state.db['TELEFONIA']['LAT']}ms")
with aba5: st.header("📂 Relatórios"); st.download_button("Baixar Dossiê", df_audit.to_html(), "S_A_V38.html", "text/html")
with aba6: st.header("⚖️ Visão Jurídica"); st.table(df_audit[["OPERADOR", "STATUS"]])
    
