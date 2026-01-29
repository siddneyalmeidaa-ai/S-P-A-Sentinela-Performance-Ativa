import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. CONFIGURAÇÃO E BLINDAGEM DE INTERFACE ---
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

# --- 2. BANCO DE DADOS INTEGRAL (S.A. PADRÃO OURO) ---
if 'db' not in st.session_state:
    st.session_state.db = {
        "OPERAÇÃO": {
            "ANA (PERFORMANCE)": {
                "VALOR_REAL": 46600.0, "PROJ": 93200.0, "STATUS": "85% LIBERADO", 
                "MINUTOS_PAUSA": 40, "DISCADAS": 1200, "ALO": 450, "CPC": 120, 
                "CPCA": 95, "PROMESSAS_N": 70, "P1": "00:10:00", "P2": "00:10:00", 
                "LANCHE": "00:20:00", "BANHEIRO": "00:00:00"
            },
            "JULIA (VÁCUO)": {
                "VALOR_REAL": 800.0, "PROJ": 1600.0, "STATUS": "12% PENDENTE", 
                "MINUTOS_PAUSA": 55, "DISCADAS": 500, "ALO": 85, "CPC": 8, 
                "CPCA": 4, "PROMESSAS_N": 1, "P1": "00:10:00", "P2": "00:10:00", 
                "LANCHE": "00:20:00", "BANHEIRO": "00:15:00"
            },
            "MARCOS (SABOTAGEM)": {
                "VALOR_REAL": 0.0, "PROJ": 0.0, "STATUS": "0% PENDENTE", 
                "MINUTOS_PAUSA": 125, "DISCADAS": 800, "ALO": 12, "CPC": 0, 
                "CPCA": 0, "PROMESSAS_N": 0, "P1": "00:25:00", "P2": "00:30:00", 
                "LANCHE": "01:00:00", "BANHEIRO": "00:30:00"
            }
        },
        "DISCADOR": {"PEN": 65, "MAILING": "Ativo 2026", "TOTAL_DISCADAS": 2500},
        "TELEFONIA": {"LAT": 250, "STATUS": "CRÍTICO", "SERVER": "Vivo Cloud"}
    }

# --- 3. PROCESSAMENTO (REGRA X = -50%) ---
df_list = []
for k, v in st.session_state.db["OPERAÇÃO"].items():
    alo = v.get("ALO", 0)
    prom = v.get("PROMESSAS_N", 0)
    proj = v.get("PROJ", 0.0)
    df_list.append({
        "OPERADOR": k,
        "LOC %": (alo / v.get("DISCADAS", 1) * 100),
        "ALÔ": alo,
        "CPC": v.get("CPC", 0),
        "CPCA": v.get("CPCA", 0),
        "PROMESSAS": prom,
        "CONV %": (prom / alo * 100) if alo > 0 else 0,
        "REAL": v.get("VALOR_REAL", 0.0),
        "PROJEÇÃO": proj,
        "X (-50%)": proj * 0.5,
        "STATUS": v.get("STATUS", "PENDENTE"),
        "MINUTOS": v.get("MINUTOS_PAUSA", 0)
    })
df_audit = pd.DataFrame(df_list)

# --- 4. CABEÇALHO MANIFESTO ---
st.markdown(f"""
    <div class="manifesto-container">
        <div class="quote-text">"Enquanto o mundo olha para o avião que sobe, eu governo o código que o faz voar."</div>
        <div class="signature">👊🚀📊⚖️🏁💎 — Comandante S.A.</div>
    </div>
""", unsafe_allow_html=True)

st.title("🛰️ S.P.A. - SENTINELA DE PERFORMANCE ATIVA")
st.write(f"**CONSOLIDE V64** | COCKPIT ATUALIZADO | {datetime.now().strftime('%H:%M:%S')}")

aba1, aba2, aba3, aba4, aba5 = st.tabs([
    "👑 01. COCKPIT", "👥 02. GESTÃO", "🧠 03. DISCADOR", 
    "📡 04. TELEFONIA", "📂 05. RELATÓRIOS"
])

# --- ABA 01: COCKPIT (VOLUME DE PROMESSAS INTEGRADO) ---
with aba1:
    st.header("📊 Cockpit Consolidado (Tudo Aqui)")
    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("Localização", f"{df_audit['LOC %'].mean():.1f}%")
    c2.metric("Contatos (CPCA)", int(df_audit['CPCA'].sum()))
    c3.metric("Volume Promessas", int(df_audit['PROMESSAS'].sum())) # <--- ATUALIZADO
    c4.metric("Recuperado Real", f"R$ {df_audit['REAL'].sum():,.2f}")
    c5.metric("Pausa Equipe", f"{df_audit['MINUTOS'].sum()} min")

    st.divider()
    st.subheader("🏁 Tabela da Favelinha")
    st.dataframe(df_audit, use_container_width=True)

# --- ABA 02: GESTÃO (ANATOMIA DO FUNIL) ---
with aba2:
    st.header("👥 Anatomia do Funil Individual")
    op_sel = st.selectbox("Selecione para análise profunda:", df_audit["OPERADOR"].tolist())
    res = df_audit[df_audit["OPERADOR"] == op_sel].iloc[0]
    p_raw = st.session_state.db["OPERAÇÃO"][op_sel]
    
    f1, f2, f3, f4 = st.columns(4)
    f1.metric("Alô", int(res["ALÔ"]))
    f2.metric("CPC", int(res["CPC"]))
    f3.metric("CPCA", int(res["CPCA"]))
    f4.metric("Promessas", int(res["PROMESSAS"]))
    
    st.divider()
    st.warning(f"Ação Imediata: {'ENTRA' if res['CONV %'] > 15 else 'PULA'}")
    st.write(f"**Pausas Detalhadas:** P1: {p_raw['P1']} | P2: {p_raw['P2']} | Lanche: {p_raw['LANCHE']} | Banheiro: {p_raw['BANHEIRO']}")

with aba3: st.json(st.session_state.db["DISCADOR"])
with aba4: st.json(st.session_state.db["TELEFONIA"])
with aba5: st.download_button("📥 DOWNLOAD V64", df_audit.to_csv().encode('utf-8-sig'), "S_A_SPA_V64.csv")
            
