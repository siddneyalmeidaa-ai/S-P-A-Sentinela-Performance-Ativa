import streamlit as st
import pandas as pd
import hashlib
from datetime import datetime
from docx import Document
import io

# --- 1. CAMADA DE SOBERANIA (CONFIGURAÇÃO & BLINDAGEM) ---
st.set_page_config(page_title="S.P.A. MASTER - V96 SUPREMO", layout="wide")

# CSS PROPRIETÁRIO S.A.
st.markdown("""
<style>
    #MainMenu {visibility: hidden;} header {visibility: hidden;} footer {visibility: hidden;}
    .manifesto-container {background-color: #050505; border-left: 5px solid #00FF41; padding: 20px; border-radius: 10px; margin-bottom: 25px;}
    .quote-text { color: #00FF41; font-size: 18px; font-weight: bold; font-style: italic; }
    .signature { color: #D4AF37; font-size: 12px; text-transform: uppercase; letter-spacing: 2px; }
    .ofensor-red { color: #FF0000; font-weight: bold; background-color: rgba(255,0,0,0.1); padding: 5px; border-radius: 3px; }
</style>
""", unsafe_allow_html=True)

# --- 2. BANCO DE DADOS INTEGRAL (PADRÃO OURO) ---
if 'db' not in st.session_state:
    st.session_state.db = {
        "OPERAÇÃO": {
            "ANA (PERFORMANCE)": {"CPF": "123.456.789-01", "VALOR_REAL": 46600.0, "PROJ": 93200.0, "PAUSA": 40, "ALO": 450, "CPCA": 95, "PROMESSAS": 70, "SABOTAGEM": 0},
            "MARCOS (SABOTAGEM)": {"CPF": "456.123.789-55", "VALOR_REAL": 0.0, "PROJ": 0.0, "PAUSA": 125, "ALO": 12, "CPCA": 1, "PROMESSAS": 0, "SABOTAGEM": 85}
        },
        "DISCADOR": {"IA_SENTINELA": "ATIVO", "LIXO_TOTAL": 70.6, "DESCONHECIDOS": 42.5, "INEXISTENTES": 28.1},
        "TELEFONIA": {"LAT": 380, "SERVER": "Vivo Cloud", "JITTER": "2ms"},
        "IPI": "S.A.-V96-2026"
    }

# --- 3. MOTOR DE CÁLCULO & LÓGICA DE GUERRA ---
df_list = []
for k, v in st.session_state.db["OPERAÇÃO"].items():
    conv = round((v["PROMESSAS"] / v["CPCA"] * 100), 1) if v["CPCA"] > 0 else 0
    proj_x = v["PROJ"] * 0.5 # REGRA X -50%
    dano = (v["PAUSA"] - 45) * 0.95 if v["PAUSA"] > 45 else 0
    df_list.append({
        "OPERADOR": k, "CPF": v["CPF"], "CPCA": v["CPCA"], "PROMESSAS": v["PROMESSAS"],
        "CONV %": conv, "X (-50%)": proj_x, "PAUSA": v["PAUSA"], "DANO R$": round(dano, 2),
        "STATUS": "85% LIBERADO" if conv > 50 else "0% PENDENTE"
    })
df_audit = pd.DataFrame(df_list)

# --- 4. INTERFACE S.A. SUPREMO ---
st.markdown('<div class="manifesto-container"><div class="quote-text">"S.P.A. MASTER - SIDNEY ALMEIDA | V96"</div><div class="signature">👊🚀 — COMANDANTE S.A. | IPI: SINCRO_S.A.</div></div>', unsafe_allow_html=True)

tabs = st.tabs(["👑 01. COCKPIT", "👥 02. GESTÃO CPF", "☎️ 03. DISCADOR", "📡 04. TELEFONIA", "🐍 05. SABOTAGEM", "⚖️ 06. JURÍDICO", "📂 07. EXPORTAÇÃO"])

with tabs[0]: # COCKPIT
    st.subheader("🏁 Tabela da Favelinha")
    # Alerta Vermelho Automático
    def highlight_pausa(val):
        color = 'red' if val > 45 else 'white'
        return f'color: {color}'
    st.dataframe(df_audit.style.applymap(highlight_pausa, subset=['PAUSA']), use_container_width=True)
    st.metric("Total X do Servidor", f"R$ {df_audit['X (-50%)'].sum():,.2f}")

with tabs[1]: # GESTÃO CPF
    op_sel = st.selectbox("Espelhar Terminal (CPF):", df_audit["OPERADOR"].tolist())
    res = df_audit[df_audit["OPERADOR"] == op_sel].iloc[0]
    st.info(f"Visualizando terminal de {op_sel} | CPF: {res['CPF']}")
    st.metric("Meta X Rodada", f"R$ {res['X (-50%)']:,.2f}")
    st.radio("COMANDO IMEDIATO:", ["ENTRA", "PULA", "NÃO ENTRA"], horizontal=True)

with tabs[2]: # DISCADOR
    st.header("☎️ Inteligência de Mailing")
    st.error(f"Lixo Detectado: {st.session_state.db['DISCADOR']['LIXO_TOTAL']}%")
    st.write(f"Desconhecidos: {st.session_state.db['DISCADOR']['DESCONHECIDOS']}% | Inexistentes: {st.session_state.db['DISCADOR']['INEXISTENTES']}%")

with tabs[3]: # TELEFONIA
    st.header("📡 Infraestrutura Cloud")
    st.warning(f"Latência Vivo Cloud: {st.session_state.db['TELEFONIA']['LAT']}ms")
    st.write(f"Servidor: {st.session_state.db['TELEFONIA']['SERVER']} | Jitter: {st.session_state.db['TELEFONIA']['JITTER']}")

with tabs[4]: # SABOTAGEM
    st.header("🐍 O Sentinela")
    st.table(df_audit[df_audit["PAUSA"] > 45][["OPERADOR", "PAUSA", "DANO R$"]])

with tabs[5]: # JURÍDICO
    st.header("⚖️ Blindagem Legal")
    ofensor = st.selectbox("Selecionar Infrator:", df_audit[df_audit["PAUSA"] > 45]["OPERADOR"].tolist())
    if ofensor:
        dados_o = df_audit[df_audit["OPERADOR"] == ofensor].iloc[0]
        st.text_area("Memorial Descritivo:", f"Detectada sabotagem por pausa excessiva de {dados_o['PAUSA']} minutos, gerando dano patrimonial de R$ {dados_o['DANO R$']}.")
        st.write("Punição Sugerida: Advertência Formal + Suspensão.")

with tabs[6]: # EXPORTAÇÃO
    st.header("📂 Relatórios Ouro")
    csv_data = df_audit.to_csv(index=False).encode('utf-8-sig')
    hash_sa = hashlib.sha256(csv_data).hexdigest()
    st.write(f"Hash de Integridade (SHA-256): `{hash_sa}`")
    st.download_button("EXPORTAR RELATÓRIO FORENSE", csv_data, f"S_A_V96_{datetime.now().strftime('%Y%m%d')}.csv")
    
