import streamlit as st
import pandas as pd
import hashlib
from datetime import datetime
from docx import Document
import io

# --- 1. SOBERANIA & BLINDAGEM CSS ---
st.set_page_config(page_title="S.P.A. MASTER - V114 UNIFICADO", layout="wide")
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
            "DISCADOR": {"LIXO": "70.6%", "PROG": "ALERTA: Mailing saturado em 15 min. Risco de Vácuo."},
            "TELEFONIA": {"LAT": "380ms", "PROG": "ESTÁVEL: Monitorando latência Vivo Cloud."}
        },
        "IPI": "SINCRO_V114_UNIFICADO"
    }

# --- 3. MOTOR DE PROCESSAMENTO (CONVERSÃO & CONSOLIDAÇÃO) ---
df_list = []
for k, v in st.session_state.db["OPERAÇÃO"].items():
    conv_val = (v["PROMESSAS"] / v["CPCA"] * 100) if v["CPCA"] > 0 else 0
    df_list.append({
        "OPERADOR": k, "CPF": v["CPF"], "ALO": v["ALO"], "CPCA": v["CPCA"], 
        "PROMESSAS": v["PROMESSAS"], "CONVERSÃO": f"{round(conv_val, 1)}%", 
        "PAUSA": v["PAUSA"], "LOGIN": v["LOGIN"], "LOGOUT": v["LOGOUT"], "TEMPO LOGADO": v["LOGADO"],
        "X (-50%)": (v["PROMESSAS"] * 100) * 0.5 # Exemplo de Projeção
    })
df_audit = pd.DataFrame(df_list)

# --- 4. INTERFACE UNIFICADA ---
st.markdown(f'<div class="manifesto-container"><div class="quote-text">"S.P.A. MASTER - SIDNEY ALMEIDA | V114"</div><div class="signature">👊🚀 — COMANDANTE S.A. | {st.session_state.db["IPI"]}</div></div>', unsafe_allow_html=True)

tabs = st.tabs(["👑 01. COCKPIT", "👥 02. GESTÃO CPF", "☎️ 03. DISCADOR", "📡 04. TELEFONIA", "🐍 05. SABOTAGEM", "⚖️ 06. JURÍDICO", "📂 07. EXPORTAÇÃO"])

with tabs[0]: # COCKPIT (A CENTRAL)
    st.subheader("🚀 Saúde Técnica do Servidor")
    col_t1, col_t2 = st.columns(2)
    col_t1.info(f"☎️ VISÃO DISCADOR: {st.session_state.db['TECNICO']['DISCADOR']['LIXO']} Lixo | {st.session_state.db['TECNICO']['DISCADOR']['PROG']}")
    col_t2.success(f"📡 VISÃO TELEFONIA: Latência {st.session_state.db['TECNICO']['TELEFONIA']['LAT']} | {st.session_state.db['TECNICO']['TELEFONIA']['PROG']}")
    
    st.markdown("---")
    st.subheader("📊 Funil & Consolidação Operacional")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Total Alô", df_audit["ALO"].sum())
    m2.metric("Soma Pausas", f"{df_audit['PAUSA'].sum()} min")
    m3.metric("Conv. Média", f"{round(df_audit['PROMESSAS'].sum() / df_audit['CPCA'].sum() * 100, 1)}%")
    m4.metric("Total X (-50%)", f"R$ {df_audit['X (-50%)'].sum():,.2f}")
    
    st.dataframe(df_audit[["OPERADOR", "LOGIN", "LOGOUT", "TEMPO LOGADO", "PAUSA", "CONVERSÃO"]].style.applymap(lambda x: 'color: red' if isinstance(x, int) and x > 45 else '', subset=['PAUSA']), use_container_width=True)

with tabs[1]: # GESTÃO CPF (ESPELHO TÁTICO)
    op_sel = st.selectbox("Espelhar Terminal:", df_audit["OPERADOR"].tolist())
    res_op = df_audit[df_audit["OPERADOR"] == op_sel].iloc[0]
    st.subheader(f"👥 Espelho Tático: {op_sel}")
    st.radio("COMANDO IMEDIATO:", ["ENTRA", "PULA", "NÃO ENTRA"], horizontal=True, key=f"cmd_{op_sel}")
    st.table(res_op)

with tabs[6]: # EXPORTAÇÃO FORENSE (SEGMENTADA)
    st.header("📂 Exportação de Relatórios Ouro")
    
    st.subheader("1. Consolidado Operacional (Total Equipe)")
    st.write(f"Soma Total Logada: {df_audit['TEMPO LOGADO'].max()} | Soma Total Pausas: {df_audit['PAUSA'].sum()} min")
    st.download_button("Baixar Consolidado Excel", df_audit.to_csv().encode('utf-8-sig'), "Consolidado_S_A.xlsx")
    
    st.subheader("2. Relatório Individual (Forense)")
    op_ref = st.selectbox("Selecionar para PDF:", df_audit["OPERADOR"].tolist())
    st.download_button(f"Gerar PDF - {op_ref}", df_audit[df_audit["OPERADOR"] == op_ref].to_csv().encode('utf-8-sig'), f"Relatorio_{op_ref}.pdf")
    
