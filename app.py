import streamlit as st
import pandas as pd
import hashlib
from datetime import datetime
from docx import Document
import io

# --- 1. SOBERANIA & BLINDAGEM CSS ---
st.set_page_config(page_title="S.P.A. MASTER - V116 SUPREMO", layout="wide")
st.markdown("""
<style>
    #MainMenu {visibility: hidden;} header {visibility: hidden;} footer {visibility: hidden;}
    .manifesto-container {background-color: #050505; border-left: 5px solid #00FF41; padding: 20px; border-radius: 10px; margin-bottom: 25px;}
    .quote-text { color: #00FF41; font-size: 18px; font-weight: bold; font-style: italic; }
    .signature { color: #D4AF37; font-size: 12px; text-transform: uppercase; letter-spacing: 2px; }
</style>
""", unsafe_allow_html=True)

# --- 2. QUANTUM MEMORY (BANCO DE DADOS INTEGRAL) ---
if 'db' not in st.session_state:
    st.session_state.db = {
        "OPERAÇÃO": {
            "PAULO": {"CPF": "789.456.123-00", "ALO": 300, "CPCA": 60, "PROMESSAS": 45, "PAUSA": 20, "LOGIN": "08:00", "LOGOUT": "14:00", "LOGADO": "06:00:00"},
            "MARCOS": {"CPF": "456.123.789-55", "ALO": 12, "CPCA": 1, "PROMESSAS": 0, "PAUSA": 125, "LOGIN": "08:15", "LOGOUT": "10:30", "LOGADO": "02:15:00"}
        },
        "TECNICO": {
            "DISCADOR": {"LIXO": "70.6%", "STATUS": "IA-SENTINELA ATIVA", "DETALHE": "Mailing com alto índice de vácuo detectado."},
            "TELEFONIA": {"LAT": "380ms", "SIP": "Canais 100% ativos", "SERVER": "Vivo Cloud"}
        },
        "IPI": "SINCRO_V116_OURO"
    }

# --- 3. MOTOR DE PROCESSAMENTO (CONVERSÃO & CONSOLIDAÇÃO) ---
df_list = []
for k, v in st.session_state.db["OPERAÇÃO"].items():
    conv_val = (v["PROMESSAS"] / v["CPCA"] * 100) if v["CPCA"] > 0 else 0
    df_list.append({
        "OPERADOR": k, "CPF": v["CPF"], "ALO": v["ALO"], "CPCA": v["CPCA"], 
        "PROMESSAS": v["PROMESSAS"], "CONVERSÃO": f"{round(conv_val, 1)}%", 
        "PAUSA": v["PAUSA"], "LOGIN": v["LOGIN"], "LOGOUT": v["LOGOUT"], "TEMPO LOGADO": v["LOGADO"],
        "X (-50%)": (v["PROMESSAS"] * 100) * 0.5 
    })
df_audit = pd.DataFrame(df_list)

# --- 4. INTERFACE DE COMANDO UNIFICADA ---
st.markdown(f'<div class="manifesto-container"><div class="quote-text">"S.P.A. MASTER - SIDNEY ALMEIDA | V116"</div><div class="signature">👊🚀 — COMANDANTE S.A. | {st.session_state.db["IPI"]}</div></div>', unsafe_allow_html=True)

tabs = st.tabs(["👑 01. COCKPIT", "👥 02. GESTÃO CPF", "☎️ 03. DISCADOR", "📡 04. TELEFONIA", "🐍 05. SABOTAGEM", "⚖️ 06. JURÍDICO", "📂 07. EXPORTAÇÃO"])

with tabs[0]: # 01. COCKPIT
    st.subheader("🚀 Saúde do Servidor & Funil Macro")
    c_t1, c_t2 = st.columns(2)
    c_t1.info(f"☎️ DISCADOR: {st.session_state.db['TECNICO']['DISCADOR']['LIXO']} Lixo | {st.session_state.db['TECNICO']['DISCADOR']['STATUS']}")
    c_t2.success(f"📡 TELEFONIA: Latência {st.session_state.db['TECNICO']['TELEFONIA']['LAT']} | {st.session_state.db['TECNICO']['TELEFONIA']['SERVER']}")
    
    st.markdown("---")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Total Alô", df_audit["ALO"].sum())
    m2.metric("Soma Pausas", f"{df_audit['PAUSA'].sum()} min")
    m3.metric("Conv. Média", f"{round(df_audit['PROMESSAS'].sum() / df_audit['CPCA'].sum() * 100, 1)}%")
    m4.metric("Total X (-50%)", f"R$ {df_audit['X (-50%)'].sum():,.2f}")
    
    st.subheader("🏁 Tabela da Favelinha (Consolidado)")
    st.dataframe(df_audit[["OPERADOR", "LOGIN", "LOGOUT", "TEMPO LOGADO", "PAUSA", "CONVERSÃO"]].style.applymap(lambda x: 'color: red' if isinstance(x, int) and x > 45 else '', subset=['PAUSA']), use_container_width=True)

with tabs[1]: # 02. GESTÃO CPF (ESPELHO)
    op_sel = st.selectbox("Espelhar Terminal Operador:", df_audit["OPERADOR"].tolist())
    res_op = df_audit[df_audit["OPERADOR"] == op_sel].iloc[0]
    st.subheader(f"👥 Espelho Tático: {op_sel}")
    st.radio("COMANDO IMEDIATO:", ["ENTRA", "PULA", "NÃO ENTRA"], horizontal=True, key=f"cmd_{op_sel}")
    st.table(res_op)

with tabs[2]: # 03. DISCADOR
    st.subheader("☎️ Inteligência IA-Sentinela")
    st.write(f"Diagnóstico de Mailing: {st.session_state.db['TECNICO']['DISCADOR']['DETALHE']}")
    st.progress(0.7) # Exemplo de saturação de lixo

with tabs[3]: # 04. TELEFONIA
    st.subheader("📡 Status Vivo
                 
