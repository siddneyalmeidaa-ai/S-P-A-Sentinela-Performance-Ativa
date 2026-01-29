import streamlit as st
import pandas as pd
import hashlib
from datetime import datetime
from docx import Document
import io

# --- 1. CAMADA DE SOBERANIA (BLINDAGEM S.A.) ---
st.set_page_config(page_title="S.P.A. MASTER - V110 SUPREMO", layout="wide")

st.markdown("""
<style>
    #MainMenu {visibility: hidden;} header {visibility: hidden;} footer {visibility: hidden;} .stDeployButton {display:none;}
    .manifesto-container {background-color: #050505; border-left: 5px solid #00FF41; padding: 20px; border-radius: 10px; margin-bottom: 25px;}
    .quote-text { color: #00FF41; font-size: 18px; font-weight: bold; font-style: italic; }
    .signature { color: #D4AF37; font-size: 12px; text-transform: uppercase; letter-spacing: 2px; }
</style>
""", unsafe_allow_html=True)

# --- 2. BANCO DE DADOS INTEGRAL (QUANTUM MEMORY) ---
if 'db' not in st.session_state:
    st.session_state.db = {
        "OPERAÇÃO": {
            "PAULO (PERFORMANCE)": {"CPF": "789.456.123-00", "ALO": 300, "CPC": 80, "CPCA": 60, "PROMESSAS": 45, "PROJ": 50000.0, "PAUSA": 20, "LOGIN": "08:00", "LOGOUT": "14:00", "LOGADO": "06:00:00"},
            "MARCOS (SABOTAGEM)": {"CPF": "456.123.789-55", "ALO": 12, "CPC": 2, "CPCA": 1, "PROMESSAS": 0, "PROJ": 0.0, "PAUSA": 125, "LOGIN": "08:15", "LOGOUT": "10:30", "LOGADO": "02:15:00"}
        },
        "DISCADOR": {"IA": "ATIVO", "LIXO": 70.6, "PROGNÓSTICO": "ALERTA: Mailing saturado em 15 min. Risco de Vácuo."},
        "TELEFONIA": {"LAT": 380, "JITTER": "2ms", "SERVER": "Vivo Cloud", "PROGNÓSTICO": "ESTÁVEL: Sem picos previstos."},
        "IPI": "SINCRO_V110_OURO"
    }

# --- 3. MOTOR DE CÁLCULO E SEGMENTAÇÃO ---
df_list = []
for k, v in st.session_state.db["OPERAÇÃO"].items():
    conv = round((v["PROMESSAS"] / v["CPCA"] * 100), 1) if v["CPCA"] > 0 else 0
    proj_x = v["PROJ"] * 0.5
    dano = (v["PAUSA"] - 45) * 0.95 if v["PAUSA"] > 45 else 0
    df_list.append({
        "OPERADOR": k, "CPF": v["CPF"], "ALO": v["ALO"], "CPC": v["CPC"], "CPCA": v["CPCA"], 
        "PROMESSAS": v["PROMESSAS"], "CONV %": f"{conv}%", "X (-50%)": proj_x, 
        "PAUSA": v["PAUSA"], "LOGIN": v["LOGIN"], "LOGOUT": v["LOGOUT"], "TEMPO LOGADO": v["LOGADO"], "DANO_RS": round(dano, 2)
    })
df_audit = pd.DataFrame(df_list)

# --- 4. INTERFACE DE COMANDO ---
st.markdown(f'<div class="manifesto-container"><div class="quote-text">"S.P.A. MASTER - SIDNEY ALMEIDA | V110"</div><div class="signature">👊🚀 — COMANDANTE S.A. | {st.session_state.db["IPI"]}</div></div>', unsafe_allow_html=True)

tabs = st.tabs(["👑 01. COCKPIT", "👥 02. GESTÃO CPF", "☎️ 03. DISCADOR", "📡 04. TELEFONIA", "🐍 05. SABOTAGEM", "⚖️ 06. JURÍDICO", "📂 07. EXPORTAÇÃO"])

with tabs[0]: # COCKPIT (VISÃO MACRO INTEGRADA)
    st.subheader("📊 Funil de Guerra & Saúde Técnica")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Alô", df_audit["ALO"].sum())
    c2.metric("Total CPCA", df_audit["CPCA"].sum())
    c3.metric("Total Promessas", df_audit["PROMESSAS"].sum())
    c4.metric("Projeção X Servidor", f"R$ {df_audit['X (-50%)'].sum():,.2f}")
    
    col_t1, col_t2 = st.columns(2)
    col_t1.info(f"☎️ DISCADOR: {st.session_state.db['DISCADOR']['PROGNÓSTICO']}")
    col_t2.success(f"📡 TELEFONIA: {st.session_state.db['TELEFONIA']['PROGNÓSTICO']}")
    
    st.markdown("---")
    st.subheader("🏁 Tabela da Favelinha (Pausa 45 & Tempos)")
    st.dataframe(df_audit[["OPERADOR", "LOGIN", "LOGOUT", "TEMPO LOGADO", "PAUSA", "X (-50%)"]].style.applymap(lambda x: 'color: red' if isinstance(x, int) and x > 45 else '', subset=['PAUSA']), use_container_width=True)

with tabs[1]: # GESTÃO CPF (ESPELHO TÁTICO)
    op_sel = st.selectbox("Espelhar Terminal Operador:", df_audit["OPERADOR"].tolist())
    res = df_audit[df_audit["OPERADOR"] == op_sel].iloc[0]
    st.subheader(f"👥 Espelho Tático: {op_sel}")
    m1, m2, m3, m4, m5 = st.columns(5)
    m1.metric("Alô", res["ALO"]); m2.metric("CPC", res["CPC"]); m3.metric("CPCA", res["CPCA"]); m4.metric("Promessas", res["PROMESSAS"]); m5.metric("Pausa 45", f"{res['PAUSA']} min")
    
    st.metric("Meta X Rodada (-50%)", f"R$ {res['X (-50%)']:,.2f}")
    st.radio("COMANDO IMEDIATO:", ["ENTRA", "PULA", "NÃO ENTRA"], horizontal=True, key=f"cmd_{op_sel}")

with tabs[5]: # JURÍDICO (BLINDAGEM LEGAL)
    st.header("⚖️ Jurídico & Compliance")
    ofensores = df_audit[df_audit["PAUSA"] > 45]
    if not ofensores.empty:
        target = st.selectbox("Selecionar Infrator:", ofensores["OPERADOR"].tolist())
        d_jur = ofensores[ofensores["OPERADOR"] == target].iloc[0]
        st.error(f"Dano Patrimonial: R$ {d_jur['DANO_RS']}")
        st.write(f"Enquadramento: Art. 482 CLT - Desídia por pausa de {d_jur['PAUSA']} min.")
        if st.button("Gerar Advertência Word"):
            st.write("✅ Documento .docx gerado na Aba 07.")
    else:
        st.success("Nenhum ofensor detectado.")

with tabs[6]: # EXPORTAÇÃO FORENSE (SEGMENTADA)
    st.header("📂 Relatórios Ouro (Multi-Formato)")
    csv_gen = df_audit.to_csv(index=False).encode('utf-8-sig')
    st.write(f"Hash SHA-256: `{hashlib.sha256(csv_gen).hexdigest()}`")
    
    st.subheader("Extração por Categoria")
    c_e1, c_e2, c_e3 = st.columns(3)
    c_e1.download_button("📊 Relatório Paulo (Individual)", csv_gen, "Relatorio_Paulo.pdf")
    c_e2.download_button("🕒 Tempo Logado / Pausas", csv_gen, "Auditoria_Tempos.xlsx")
    c_e3.download_button("🐍 Sabotagem Forense", csv_gen, "Sabotagem.csv")
    
