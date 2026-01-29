import streamlit as st
import pandas as pd
from datetime import datetime
import io

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

# --- 2. BANCO DE DADOS INTEGRAL (PADRÃO OURO) ---
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
        "DISCADOR": {"PEN": 65, "MAILING": "Ativo 2026", "VÁCUO": 0},
        "TELEFONIA": {"LAT": 250, "STATUS": "ESTÁVEL", "SERVER": "Vivo Cloud"}
    }

# --- 3. PROCESSAMENTO S.A. (REGRA X = -50%) ---
df_list = []
for k, v in st.session_state.db["OPERAÇÃO"].items():
    alo = v.get("ALO", 0)
    prom = v.get("PROMESSAS_N", 0)
    proj = v.get("PROJ", 0.0)
    df_list.append({
        "OPERADOR": k,
        "LOC %": (alo / v.get("DISCADAS", 1) * 100),
        "ALÔ": alo,
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

# --- 4. CABEÇALHO ---
st.markdown(f"""
    <div class="manifesto-container">
        <div class="quote-text">"Enquanto o mundo olha para o avião que sobe, eu governo o código que o faz voar."</div>
        <div class="signature">👊🚀📊⚖️🏁💎 — Comandante S.A.</div>
    </div>
""", unsafe_allow_html=True)

st.title("🛰️ S.P.A. - SENTINELA DE PERFORMANCE ATIVA")
st.write(f"**CONSOLIDE V69** | {datetime.now().strftime('%H:%M:%S')}")

# --- 5. ESTRUTURA DE 6 ABAS (CONSOLIDADA) ---
aba1, aba2, aba3, aba4, aba5, aba6 = st.tabs([
    "👑 01. COCKPIT", 
    "👥 02. GESTÃO", 
    "🧠 03. DISCADOR", 
    "📡 04. TELEFONIA", 
    "📂 05. RELATÓRIOS", 
    "⚖️ 06. JURÍDICO"
])

# --- ABA 01: COCKPIT ---
with aba1:
    st.header("📊 Visão 360º")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Localização", f"{df_audit['LOC %'].mean():.1f}%")
    c2.metric("Promessas", int(df_audit['PROMESSAS'].sum()))
    c3.metric("Recuperado", f"R$ {df_audit['REAL'].sum():,.2f}")
    c4.metric("Pausas", f"{df_audit['MINUTOS'].sum()} min")
    st.divider()
    st.subheader("🏁 Tabela da Favelinha")
    st.dataframe(df_audit, use_container_width=True)

# --- ABA 02: GESTÃO ---
with aba2:
    op_sel = st.selectbox("Operador:", df_audit["OPERADOR"].tolist())
    res = df_audit[df_audit["OPERADOR"] == op_sel].iloc[0]
    st.metric("X (-50%)", f"R$ {res['X (-50%)']:,.2f}")
    st.warning(f"Ação: {'ENTRA' if res['CONV %'] > 15 else 'PULA'}")

# --- ABA 03: DISCADOR ---
with aba3:
    st.subheader("IA-SENTINELA: Monitoramento de Vácuo")
    st.json(st.session_state.db["DISCADOR"])

# --- ABA 04: TELEFONIA ---
with aba4:
    st.subheader("Status de Conectividade")
    st.json(st.session_state.db["TELEFONIA"])

# --- ABA 05: RELATÓRIOS (MULTIFORMATO) ---
with aba5:
    st.header("📥 Exportação")
    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
        df_audit.to_excel(writer, index=False)
    st.download_button("📗 Excel", buffer.getvalue(), "S_A_AUDIT.xlsx")
    st.download_button("📊 CSV", df_audit.to_csv().encode('utf-8-sig'), "S_A_AUDIT.csv")

# --- ABA 06: JURÍDICO (STATUS) ---
with aba6:
    st.header("⚖️ Auditoria de Status")
    st.table(df_audit[["OPERADOR", "STATUS"]])
    
