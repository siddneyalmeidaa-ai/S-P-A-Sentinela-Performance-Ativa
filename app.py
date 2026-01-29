import streamlit as st
import pandas as pd
from datetime import datetime
from docx import Document
import io

# --- 1. SOBERANIA E BLINDAGEM (ESTILO S.A.) ---
st.set_page_config(page_title="SPA MASTER V119", layout="wide")
st.markdown("""
<style>
    #MainMenu {visibility: hidden;} header {visibility: hidden;} footer {visibility: hidden;}
    .manifesto {background-color: #050505; border-left: 5px solid #00FF41; padding: 20px; border-radius: 10px; margin-bottom: 25px;}
    .titulo { color: #00FF41; font-size: 18px; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# --- 2. BANCO DE DADOS INTEGRAL ---
if 'db' not in st.session_state:
    st.session_state.db = {
        "OPERACAO": {
            "PAULO": {"CPF": "789.456.123-00", "ALO": 300, "CPCA": 60, "PROM": 45, "PAUSA": 20, "LOGIN": "08:00", "LOGOUT": "14:00", "LOGADO": "06:00:00"},
            "MARCOS": {"CPF": "456.123.789-55", "ALO": 12, "CPCA": 1, "PROM": 0, "PAUSA": 125, "LOGIN": "08:15", "LOGOUT": "10:30", "LOGADO": "02:15:00"}
        },
        "TECNICO": {
            "DISCADOR": {"LIXO": "70.6%", "STATUS": "IA-SENTINELA ATIVA", "PROG": "Mailing saturado. Risco de Vacuo."},
            "TELEFONIA": {"LAT": "380ms", "SERVER": "Vivo Cloud", "PROG": "Estabilidade confirmada."}
        },
        "IPI": "SINCRO_V119_NO_EMOJI"
    }

# --- 3. MOTOR DE CALCULO (CONVERSAO E CONSOLIDACAO) ---
df_list = []
for k, v in st.session_state.db["OPERACAO"].items():
    conv = (v["PROM"] / v["CPCA"] * 100) if v["CPCA"] > 0 else 0
    df_list.append({
        "OPERADOR": k, "CPF": v["CPF"], "ALO": v["ALO"], "CPCA": v["CPCA"], 
        "PROMESSAS": v["PROM"], "CONVERSAO": f"{round(conv, 1)}%", 
        "PAUSA": v["PAUSA"], "LOGIN": v["LOGIN"], "LOGOUT": v["LOGOUT"], "TEMPO LOGADO": v["LOGADO"],
        "X (-50%)": (v["PROM"] * 100) * 0.5 
    })
df_audit = pd.DataFrame(df_list)

# --- 4. INTERFACE DE COMANDO ---
st.markdown('<div class="manifesto"><div class="titulo">S.P.A. MASTER - SIDNEY ALMEIDA | V119</div></div>', unsafe_allow_html=True)

tabs = st.tabs(["01. COCKPIT", "02. GESTAO CPF", "03. DISCADOR", "04. TELEFONIA", "05. SABOTAGEM", "06. JURIDICO", "07. EXPORTACAO"])

with tabs[0]: # COCKPIT
    st.subheader("Saude do Servidor e Funil Macro")
    c_t1, c_t2 = st.columns(2)
    c_t1.info(f"DISCADOR: {st.session_state.db['TECNICO']['DISCADOR']['LIXO']} | {st.session_state.db['TECNICO']['DISCADOR']['STATUS']}")
    c_t2.success(f"TELEFONIA: Latencia {st.session_state.db['TECNICO']['TELEFONIA']['LAT']} | {st.session_state.db['TECNICO']['TELEFONIA']['SERVER']}")
    
    st.markdown("---")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Total Alo", df_audit["ALO"].sum())
    m2.metric("Soma Pausas", f"{df_audit['PAUSA'].sum()} min")
    m3.metric("Conv. Media", f"{round(df_audit['PROMESSAS'].sum() / df_audit['CPCA'].sum() * 100, 1)}%")
    m4.metric("Total X (-50%)", f"R$ {df_audit['X (-50%)'].sum():,.2f}")
    
    st.subheader("Tabela da Favelinha (Consolidado)")
    st.dataframe(df_audit[["OPERADOR", "LOGIN", "LOGOUT", "TEMPO LOGADO", "PAUSA", "CONVERSAO"]].style.applymap(lambda x: 'color: red' if isinstance(x, int) and x > 45 else '', subset=['PAUSA']), use_container_width=True)

with tabs[1]: # GESTAO CPF
    op_sel = st.selectbox("Espelhar Terminal:", df_audit["OPERADOR"].tolist())
    res_op = df_audit[df_audit["OPERADOR"] == op_sel].iloc[0]
    st.radio("COMANDO:", ["ENTRA", "PULA", "NAO ENTRA"], horizontal=True, key=f"cmd_{op_sel}")
    st.table(res_op)

with tabs[2]: # DISCADOR
    st.subheader("Inteligencia IA-Sentinela")
    st.write(f"Diagnostico: {st.session_state.db['TECNICO']['DISCADOR']['PROG']}")

with tabs[3]: # TELEFONIA
    st.subheader("Status Vivo Cloud")
    st.write(f"Latencia: {st.session_state.db['TECNICO']['TELEFONIA']['LAT']}")
    st.success(f"Prognostico: {st.session_state.db['TECNICO']['TELEFONIA']['PROG']}")

with tabs[4]: # SABOTAGEM
    st.subheader("O Sentinela: Deteccao de Omissao")
    ofensores = df_audit[df_audit["PAUSA"] > 45]
    if not ofensores.empty:
        st.error("Infratores detectados!")
        st.table(ofensores[["OPERADOR", "PAUSA", "TEMPO LOGADO"]])
    else: st.success("Operacao Limpa.")

with tabs[5]: # JURIDICO
    st.subheader("Compliance Art. 482 CLT")
    st.write("Auditoria Juridica ativa por CPF.")

with tabs[6]: # EXPORTACAO
    st.subheader("Relatorios Ouro")
    csv = df_audit.to_csv(index=False).encode('utf-8-sig')
    st.download_button("Baixar Relatorio Geral", csv, "Relatorio_S_A.csv")
