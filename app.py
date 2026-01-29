import streamlit as st
import pandas as pd
from datetime import datetime
import io

# --- 1. CONFIGURAÇÃO E BLINDAGEM DE INTERFACE (S.A. SOVEREIGN) ---
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

# --- 2. BANCO DE DADOS INTEGRAL (PADRÃO OURO ACUMULATIVO) ---
if 'db' not in st.session_state:
    st.session_state.db = {
        "OPERAÇÃO": {
            "ANA (PERFORMANCE)": {
                "VALOR_REAL": 46600.0, "PROJ": 93200.0, "VALOR_NEGOCIADO": 125400.0,
                "STATUS": "85% LIBERADO", "MINUTOS_PAUSA": 40, "DISCADAS": 1200, 
                "ALO": 450, "CPC": 120, "CPCA": 95, "PROMESSAS_N": 70,
                "P1": "00:10:00", "P2": "00:10:00", "LANCHE": "00:20:00", "BANHEIRO": "00:00:00"
            },
            "MARCOS (SABOTAGEM)": {
                "VALOR_REAL": 0.0, "PROJ": 0.0, "VALOR_NEGOCIADO": 0.0,
                "STATUS": "0% PENDENTE", "MINUTOS_PAUSA": 125, "DISCADAS": 800, 
                "ALO": 12, "CPC": 0, "CPCA": 0, "PROMESSAS_N": 0,
                "P1": "00:25:00", "P2": "00:30:00", "LANCHE": "01:00:00", "BANHEIRO": "00:30:00"
            },
            "JULIA (VÁCUO)": {
                "VALOR_REAL": 800.0, "PROJ": 1600.0, "VALOR_NEGOCIADO": 2500.0,
                "STATUS": "12% PENDENTE", "MINUTOS_PAUSA": 55, "DISCADAS": 500, 
                "ALO": 85, "CPC": 8, "CPCA": 4, "PROMESSAS_N": 1,
                "P1": "00:10:00", "P2": "00:10:00", "LANCHE": "00:20:00", "BANHEIRO": "00:15:00"
            }
        },
        "DISCADOR": {"PEN": 65, "MAILING": "Ativo 2026", "TOTAL_DISCADAS": 2500},
        "TELEFONIA": {"LAT": 250, "STATUS": "CRÍTICO", "SERVER": "Vivo Cloud"}
    }

# --- 3. PROCESSAMENTO (REGRA X = PROJEÇÃO - 50%) ---
df_list = []
for k, v in st.session_state.db["OPERAÇÃO"].items():
    alo = v.get("ALO", 0)
    disc = v.get("DISCADAS", 1)
    prom = v.get("PROMESSAS_N", 0)
    proj = v.get("PROJ", 0.0)
    df_list.append({
        "OPERADOR": k,
        "LOC %": (alo / disc * 100),
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
st.write(f"**CONSOLIDE V67** | SISTEMA INTEGRAL | {datetime.now().strftime('%H:%M:%S')}")

aba1, aba2, aba3, aba4, aba5 = st.tabs([
    "👑 01. COCKPIT", "👥 02. GESTÃO", "🧠 03. DISCADOR", 
    "📡 04. TELEFONIA", "📂 05. RELATÓRIOS"
])

# --- ABA 01: COCKPIT (VISÃO 360º COM VOLUME DE PROMESSAS) ---
with aba1:
    st.header("📊 Cockpit Consolidado")
    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("Localização", f"{df_audit['LOC %'].mean():.1f}%")
    c2.metric("Contatos (CPCA)", int(df_audit['CPCA'].sum()))
    c3.metric("Volume Promessas", int(df_audit['PROMESSAS'].sum()))
    c4.metric("Recuperado Real", f"R$ {df_audit['REAL'].sum():,.2f}")
    c5.metric("Pausa Equipe", f"{df_audit['MINUTOS'].sum()} min")

    st.divider()
    st.subheader("🏁 Tabela da Favelinha")
    st.dataframe(df_audit, use_container_width=True)

# --- ABA 02: GESTÃO (ANATOMIA DO FUNIL E SABOTAGEM) ---
with aba2:
    st.header("👥 Anatomia do Funil Individual")
    op_sel = st.selectbox("Selecione para análise profunda:", df_audit["OPERADOR"].tolist())
    res = df_audit[df_audit["OPERADOR"] == op_sel].iloc[0]
    p_raw = st.session_state.db["OPERAÇÃO"][op_sel]
    
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        st.subheader("📞 Funil de Chamadas")
        st.metric("Alô (Atendidas)", int(res["ALÔ"]))
        st.metric("CPC (Contatos)", int(res["CPC"]))
        st.metric("CPCA (Efetivos)", int(res["CPCA"]))
        st.metric("Promessas (Nº)", int(res["PROMESSAS"]))
    
    with col_f2:
        st.subheader("📈 Eficiência e Alvos")
        st.metric("Taxa Localização", f"{res['LOC %']:.1f}%")
        st.metric("Conversão (Prom/Alô)", f"{res['CONV %']:.1f}%")
        st.metric("Valor Real", f"R$ {res['REAL']:,.2f}")
        st.metric("Meta X (-50%)", f"R$ {res['X (-50%)']:,.2f}")

    st.divider()
    st.subheader("⚖️ Monitoramento de Sabotagem")
    st.write(f"**Pausas Detalhadas:** P1: {p_raw['P1']} | P2: {p_raw['P2']} | Lanche: {p_raw['LANCHE']} | Banheiro: {p_raw['BANHEIRO']}")
    st.warning(f"Ação Imediata: {'ENTRA' if res['CONV %'] > 15 else 'PULA'}")

# --- ABA 03/04: INFRAESTRUTURA ---
with aba3: st.json(st.session_state.db["DISCADOR"])
with aba4: st.json(st.session_state.db["TELEFONIA"])

# --- ABA 05: RELATÓRIOS MULTIFORMATO (ACUMULATIVO) ---
with aba5:
    st.header("📥 Central de Exportação S.A.")
    st.write("Baixe a auditoria completa nos formatos abaixo:")
    
    col_exp1, col_exp2 = st.columns(2)
    
    with col_exp1:
        # EXCEL
        buffer_xlsx = io.BytesIO()
        with pd.ExcelWriter(buffer_xlsx, engine='xlsxwriter') as writer:
            df_audit.to_excel(writer, index=False, sheet_name='Performance_SA')
        st.download_button("📗 Baixar EXCEL (XLSX)", buffer_xlsx.getvalue(), "S_A_AUDIT.xlsx")

        # CSV
        csv_data = df_audit.to_csv(index=False).encode('utf-8-sig')
        st.download_button("📊 Baixar CSV", csv_data, "S_A_AUDIT.csv", "text/csv")

    with col_exp2:
        # PDF (HTML Format)
        pdf_data = df_audit.to_html().encode('utf-8-sig')
        st.download_button("📕 Baixar PDF (Visual)", pdf_data, "S_A_AUDIT.pdf", "application/pdf")
        
        # WORD (DOC Format)
        word_content = f"RELATÓRIO DE AUDITORIA S.A.\nGERADO EM: {datetime.now()}\n\n" + df_audit.to_string()
        st.download_button("📘 Baixar WORD (DOC)", word_content.encode('utf-8-sig'), "S_A_AUDIT.doc", "application/msword")
    
