import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. CONFIGURAÇÃO DE INTERFACE (PADRÃO OURO S.A.) ---
st.set_page_config(page_title="S.P.A. MASTER - SIDNEY ALMEIDA", layout="wide", page_icon="🛰️")

# Blindagem total de CSS e Markdown (Resolução definitiva do erro do print 04:07)
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

# --- 2. BANCO DE DADOS INTEGRAL (QUANTUM MEMORY V44) ---
# Resolvendo SyntaxError: '{' was never closed (Prints 04:11, 04:12, 04:13)
if 'db' not in st.session_state:
    st.session_state.db = {
        "OPERAÇÃO": {
            "ANA (PERFORMANCE)": {
                "VALOR_REAL": 45800.0, "PROJ": 91600.0, "STATUS": "85% LIBERADO",
                "MINUTOS_PAUSA": 40, "DISCADAS": 1200, "ALO": 450, "CPC": 120, "PROMESSAS_N": 70,
                "P1": "00:10:00", "P2": "00:10:00", "LANCHE": "00:20:00", "BANHEIRO": "00:00:00"
            },
            "MARCOS (SABOTAGEM)": {
                "VALOR_REAL": 0.0, "PROJ": 0.0, "STATUS": "0% BLOQUEADO",
                "MINUTOS_PAUSA": 125, "DISCADAS": 800, "ALO": 12, "CPC": 0, "PROMESSAS_N": 0,
                "P1": "00:25:00", "P2": "00:30:00", "LANCHE": "01:00:00", "BANHEIRO": "00:30:00"
            },
            "JULIA (VÁCUO)": {
                "VALOR_REAL": 800.0, "PROJ": 1600.0, "STATUS": "12% OK",
                "MINUTOS_PAUSA": 55, "DISCADAS": 500, "ALO": 85, "CPC": 8, "PROMESSAS_N": 1,
                "P1": "00:10:00", "P2": "00:10:00", "LANCHE": "00:20:00", "BANHEIRO": "00:15:00"
            }
        },
        "DISCADOR": {"PEN": 65, "MAILING": "Ativo 2026", "TOTAL_DISCADAS": 2500},
        "TELEFONIA": {"LAT": 250, "STATUS": "CRÍTICO", "SERVER": "Vivo Cloud"}
    }

# Processamento de Dados com Blindagem Anti-KeyError (Print 03:57)
df_list = []
for k, v in st.session_state.db["OPERAÇÃO"].items():
    alo = v.get("ALO", 0)
    disc = v.get("DISCADAS", 1)
    df_list.append({
        "OPERADOR": k,
        "LOC %": f"{(alo / disc * 100):.1f}%",
        "ALÔ": alo,
        "CPC": v.get("CPC", 0),
        "PROMESSAS (Nº)": int(v.get("PROMESSAS_N", 0)),
        "REAL": v.get("VALOR_REAL", 0.0),
        "PROJEÇÃO": v.get("PROJ", 0.0),
        "X (-50%)": v.get("PROJ", 0.0) * 0.5,
        "STATUS": v.get("STATUS", "PENDENTE"),
        "MINUTOS": v.get("MINUTOS_PAUSA", 0)
    })

df_audit = pd.DataFrame(df_list)
total_pausa_geral = df_audit["MINUTOS"].sum()

# --- 3. CABEÇALHO ---
st.markdown(f"""
    <div class="manifesto-container">
        <div class="quote-text">"Enquanto o mundo olha para o avião que sobe, eu governo o código que o faz voar."</div>
        <div class="signature">👊🚀📊⚖️🏁💎 — Frase autoral: Comandante S.A.</div>
    </div>
""", unsafe_allow_html=True)

st.title("🛰️ S.P.A. - SENTINELA DE PERFORMANCE ATIVA")
st.write(f"**ALINHAMENTO ORBITAL** | COCKPIT CONSOLIDADO | {datetime.now().strftime('%H:%M:%S')}")

# --- 4. AS 6 ABAS (REGRA: NADA SE EXCLUI) ---
aba1, aba2, aba3, aba4, aba5, aba6 = st.tabs([
    "👑 01. COCKPIT CONSOLIDADO", "👥 02. GESTÃO DE OPERADORES", "🧠 03. ESTRATÉGIA DE DISCADOR", 
    "📡 04. INFRA TELEFONIA", "📂 05. CENTRAL DE RELATÓRIOS", "⚖️ 06. VISÃO JURÍDICA"
])

# --- ABA 01: COCKPIT VISÃO CONSOLIDADA ---
with aba1:
    st.header("📊 Cockpit de Visão Estratégica")
    
    m1, m2, m3, m4, m5 = st.columns(5)
    
    # 1. Taxa de Localização (Indicador Mestre de Mailing)
    t_disc = st.session_state.db["DISCADOR"]["TOTAL_DISCADAS"]
    loc_geral = (df_audit["ALÔ"].sum() / t_disc * 100) if t_disc > 0 else 0
    m1.metric("Taxa Localização", f"{loc_geral:.1f}%", "MAILING")
    
    # 2. Promessas em NÚMERO (Como ordenado)
    m2.metric("Promessas (Nº)", f"{int(df_audit['PROMESSAS (Nº)'].sum())}", "VOLUME")
    
    # 3. Financeiro
    m3.metric("Recuperado Real", f"R$ {df_audit['REAL'].sum():,.2f}")
    
    # 4. Telefonia (Infra)
    m4.metric("Latência Rede", f"{st.session_state.db['TELEFONIA']['LAT']}ms", st.session_state.db['TELEFONIA']['STATUS'], delta_color="inverse")
    
    # 5. Pausa Coletiva (Gestão)
    p_color = "inverse" if total_pausa_geral > 45 else "normal"
    m5.metric("Pausa Coletiva", f"{total_pausa_geral} min", f"{total_pausa_geral-45}m excesso" if total_pausa_geral > 45 else "DENTRO DO LIMITE", delta_color=p_color)

    st.divider()
    st.subheader("🏁 Tabela da Favelinha - Auditoria de X (-50%)")
    st.dataframe(df_audit.style.format({
        "REAL": "R$ {:,.2f}", "PROJEÇÃO": "R$ {:,.2f}", "X (-50%)": "R$ {:,.2f}"
    }), use_container_width=True)

# --- ABA 02: GESTÃO DE OPERADORES ---
with aba2:
    st.header("👥 Anatomia do Funil Individual")
    op_sel = st.selectbox("Selecione para análise profunda:", df_audit["OPERADOR"].tolist())
    res_op = st.session_state.db["OPERAÇÃO"][op_sel]
    
    f1, f2, f3, f4 = st.columns(4)
    f1.metric("Alô", res_op.get("ALO", 0))
    f2.metric("CPC", res_op.get("CPC", 0))
    f3.metric("Promessas (Nº)", int(res_op.get("PROMESSAS_N", 0)))
    f4.metric("Pausa Individual", f"{res_op.get('MINUTOS_PAUSA', 0)} min")
    
    st.divider()
    st.info(f"Monitor de Pausas Detalhado: P1: {res_op['P1']} | P2: {res_op['P2']} | Lanche: {res_op['LANCHE']} | Banheiro: {res_op['BANHEIRO']}")

# --- ABAS TÉCNICAS E JURÍDICAS ---
with aba3:
    st.header("🧠 Discador")
    st.metric("IPI (Penetração)", f"{st.session_state.db['DISCADOR']['PEN']}%")

with aba4:
    st.header("📡 Telefonia")
    st.error(f"Status do Servidor: {st.session_state.db['TELEFONIA']['SERVER']}")

with aba5:
    st.header("📂 Relatórios")
    # Resolução definitiva do SyntaxError: unterminated string literal (Print 04:10)
    csv = df_audit.to_csv(index=False).encode('utf-8-sig')
    st.download_button("📥 BAIXAR AUDITORIA V44", csv, "AUDIT_S_A_V44.csv", "text/csv")

with aba6:
    st.header("⚖️ Visão Jurídica")
    st.table(df_audit[["OPERADOR", "STATUS"]])
    
