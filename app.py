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
""", unsafe_allow_True=True)

# --- 2. BANCO DE DADOS INTEGRAL (QUANTUM MEMORY V37 - BLINDAGEM TOTAL) ---
if 'db' not in st.session_state:
    st.session_state.db = {
        "OPERAÇÃO": {
            "ANA (PERFORMANCE)": {
                "VALOR_REAL": 45800.0, "VALOR_PROMESSA": 62000.0, "PROJ": 91600.0, "STATUS": "85% LIBERADO", "LEGAL": "Art. 444 CLT",
                "LOG_TIME": "06:12:00", "PROD": 92, "MINUTOS_PAUSA": 40, "DISCADAS": 1200,
                "ALO": 450, "CPC": 120, "CPCA": 85, "PROMESSAS": 70,
                "P1": "00:10:00", "P2": "00:10:00", "LANCHE": "00:20:00", "BANHEIRO": "00:00:00"
            },
            "MARCOS (SABOTAGEM)": {
                "VALOR_REAL": 0.0, "VALOR_PROMESSA": 0.0, "PROJ": 0.0, "STATUS": "0% BLOQUEADO", "LEGAL": "Art. 482 CLT",
                "LOG_TIME": "04:30:00", "PROD": 0, "MINUTOS_PAUSA": 125, "DISCADAS": 800,
                "ALO": 12, "CPC": 0, "CPCA": 0, "PROMESSAS": 0,
                "P1": "00:25:00", "P2": "00:30:00", "LANCHE": "01:00:00", "BANHEIRO": "00:30:00"
            },
            "JULIA (VÁCUO)": {
                "VALOR_REAL": 800.0, "VALOR_PROMESSA": 2500.0, "PROJ": 1600.0, "STATUS": "12% OK", "LEGAL": "Art. 482 CLT",
                "LOG_TIME": "02:20:00", "PROD": 12, "MINUTOS_PAUSA": 55, "DISCADAS": 500,
                "ALO": 85, "CPC": 8, "CPCA": 2, "PROMESSAS": 1,
                "P1": "00:10:00", "P2": "00:10:00", "LANCHE": "00:20:00", "BANHEIRO": "00:15:00"
            }
        },
        "DISCADOR": {"PEN": 65, "SPC": 15, "MAILING": "Ativo 2026"},
        "TELEFONIA": {"LAT": 250, "STATUS": "CRÍTICO", "SERVER": "Vivo Cloud"}
    }

# Lógica de Auditoria V37 (Previne KeyError e ValueError)
df_list = []
for k, v in st.session_state.db["OPERAÇÃO"].items():
    discadas = v.get("DISCADAS", 1)
    alo = v.get("ALO", 0)
    df_list.append({
        "OPERADOR": k,
        "LOC %": round((alo / discadas) * 100, 1),
        "ALÔ": alo,
        "CPC": v.get("CPC", 0),
        "PROM QTD": v.get("PROMESSAS", 0),
        "VLR PROMESSA": v.get("VALOR_PROMESSA", 0.0),
        "VLR REAL": v.get("VALOR_REAL", 0.0),
        "PROJEÇÃO": v.get("PROJ", 0.0),
        "X (-50%)": v.get("PROJ", 0.0) * 0.5,
        "STATUS": v.get("STATUS", "PENDENTE"),
        "MINUTOS": v.get("MINUTOS_PAUSA", 0)
    })

df_audit = pd.DataFrame(df_list)
total_pausa_coletiva = df_audit["MINUTOS"].sum()

# --- 3. CABEÇALHO ---
st.markdown(f"""
    <div class="manifesto-container">
        <div class="quote-text">"Enquanto o mundo olha para o avião que sobe, eu governo o código que o faz voar."</div>
        <div class="signature">👊🚀📊⚖️🏁💎 — Frase autoral: Comandante S.A.</div>
    </div>
""", unsafe_allow_html=True)

st.title("🛰️ S.P.A. - SENTINELA DE PERFORMANCE ATIVA")
st.write(f"**CONSOLIDE 01-06** | SISTEMA INTEGRAL RESTAURADO | {datetime.now().strftime('%H:%M:%S')}")

# --- 4. INTERFACE DE 6 ABAS (REGRA ACUMULATIVA) ---
aba1, aba2, aba3, aba4, aba5, aba6 = st.tabs([
    "👑 01. VISÃO ESTRATÉGICA", "👥 02. GESTÃO DE OPERADORES", "🧠 03. ESTRATÉGIA DE DISCADOR", 
    "📡 04. INFRA TELEFONIA", "📂 05. CENTRAL DE RELATÓRIOS", "⚖️ 06. VISÃO JURÍDICA"
])

# --- ABA 01: COCKPIT CONSOLIDADO ---
with aba1:
    st.header("📊 Cockpit: Localização, Conversão e Valor")
    
    m1, m2, m3, m4, m5 = st.columns(5)
    
    # Métrica de Localização (Mailing)
    total_discadas = sum(v.get("DISCADAS", 0) for v in st.session_state.db["OPERAÇÃO"].values())
    loc_operacao = round((df_audit["ALÔ"].sum() / total_discadas) * 100, 1) if total_discadas > 0 else 0
    m1.metric("Localização", f"{loc_operacao}%", "EFIC. MAILING")
    
    # Métrica de Valor Acordado (Promessas)
    m2.metric("Vlr Promessas", f"R$ {df_audit['VLR PROMESSA'].sum():,.2f}", "ACORDADO")
    
    # Métrica de Financeiro Real
    m3.metric("Financeiro Real", f"R$ {df_audit['VLR REAL'].sum():,.2f}", "EM CAIXA")
    
    # Métrica de Conversão CPC
    conv_cpc = round((df_audit["CPC"].sum() / df_audit["ALÔ"].sum()) * 100, 1) if df_audit["ALÔ"].sum() > 0 else 0
    m4.metric("Conversão CPC", f"{conv_cpc}%")
    
    # Alerta de Pausa Coletiva (Regra 45 min)
    status_pausa = "inverse" if total_pausa_coletiva > 45 else "normal"
    m5.metric("Pausa Coletiva", f"{total_pausa_coletiva} min", 
              f"{total_pausa_coletiva - 45}m excesso" if total_pausa_coletiva > 45 else "DENTRO DO LIMITE", 
              delta_color=status_pausa)

    st.divider()
    st.subheader("🏁 Tabela da Favelinha - Auditoria de Resultado e X")
    st.dataframe(df_audit.drop(columns=['MINUTOS']).style.format({
        "VLR PROMESSA": "R$ {:,.2f}", "VLR REAL": "R$ {:,.2f}", 
        "PROJEÇÃO": "R$ {:,.2f}", "X (-50%)": "R$ {:,.2f}", "LOC %": "{:.1f}%"
    }), use_container_width=True)

# --- ABA 02: GESTÃO DETALHADA ---
with aba2:
    st.header("👥 Anatomia do Funil e Comportamento")
    op = st.selectbox("Selecione o Operador para Auditoria:", list(st.session_state.db["OPERAÇÃO"].keys()))
    data = st.session_state.db["OPERAÇÃO"][op]
    
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Localização Individual", f"{round((data.get('ALO',0)/data.get('DISCADAS',1))*100, 1)}%")
    c2.metric("Vlr Promessa", f"R$ {data.get('VALOR_PROMESSA',0):,.2f}")
    c3.metric("Conversão (CPC)", data.get("CPC", 0))
    c4.metric("Pausa Total", f"{data.get('MINUTOS_PAUSA', 0)} min")
    
    st.divider()
    st.subheader("🛰️ Monitoramento de Pausas")
    p1, p2, p3, p4 = st.columns(4)
    p1.info(f"P1: {data.get('P1','00:00:00')}")
    p2.info(f"P2: {data.get('P2','00:00:00')}")
    p3.success(f"Lanche: {data.get('LANCHE','00:00:00')}")
    p4.warning(f"Banheiro: {data.get('BANHEIRO','00:00:00')}")

# --- RESTANTE DAS ABAS (PADRÃO ACUMULATIVO) ---
with aba3:
    st.header("🧠 Estratégia de Discador")
    st.metric("IPI (Penetração)", f"{st.session_state.db['DISCADOR']['PEN']}%")
    st.write(f"Mailing: {st.session_state.db['DISCADOR']['MAILING']}")

with aba4:
    st.header("📡 Infra Telefonia")
    st.error(f"Latência: {st.session_state.db['TELEFONIA']['LAT']}ms no {st.session_state.db['TELEFONIA']['SERVER']}")

with aba5:
    st.header("📂 Central de Relatórios")
    st.download_button("📥 BAIXAR DOSSIÊ COMPLETO", df_audit.to_html().encode('utf-8-sig'), "S_A_V37_AUDIT.html", "text/html")

with aba6:
    st.header("⚖️ Visão Jurídica (CLT)")
    st.table(df_audit[["OPERADOR", "STATUS"]])
    
