import streamlit as st
import pandas as pd
import hashlib
from datetime import datetime
import io

# --- 1. CONFIGURAÇÃO E BLINDAGEM S.A. (PADRÃO OURO) ---
st.set_page_config(page_title="S.P.A. MASTER - SIDNEY ALMEIDA", layout="wide", page_icon="🛰️")

# CSS Proprietário: Dark Mode, Ocultação de Menus e Alertas de Sabotagem
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
    .diag-box { background-color: #1a1a1a; border-left: 5px solid #FF4B4B; padding: 15px; margin: 10px 0; border-radius: 5px; }
    .prog-box { background-color: #1a1a1a; border-left: 5px solid #FFA500; padding: 15px; margin: 10px 0; border-radius: 5px; }
    .sol-box { background-color: #1a1a1a; border-left: 5px solid #00FF41; padding: 15px; margin: 10px 0; border-radius: 5px; }
    .ofensor-red { color: #FF0000; font-weight: bold; border: 2px solid #FF0000; padding: 10px; border-radius: 5px; text-align: center; }
    </style>
""", unsafe_allow_html=True)

# --- 2. BANCO DE DADOS INTEGRAL (QUANTUM MEMORY REPLICA) ---
if 'db' not in st.session_state:
    st.session_state.db = {
        "OPERAÇÃO": {
            "ANA (PERFORMANCE)": {"CPF": "123.456.789-01", "VALOR_REAL": 46600.0, "PROJ": 93200.0, "STATUS": "85% LIBERADO", "TEMPO_LOGADO": "08:00:00", "PAUSA": 40, "DISCADAS": 1200, "ALO": 450, "CPC": 120, "CPCA": 95, "PROMESSAS_N": 70, "SABOTAGEM_SCORE": 0},
            "MARCOS (SABOTAGEM)": {"CPF": "456.123.789-55", "VALOR_REAL": 0.0, "PROJ": 0.0, "STATUS": "0% PENDENTE", "TEMPO_LOGADO": "03:15:00", "PAUSA": 125, "DISCADAS": 800, "ALO": 12, "CPC": 2, "CPCA": 1, "PROMESSAS_N": 0, "SABOTAGEM_SCORE": 85}
        },
        "DISCADOR": {"IA_SENTINELA": "ATIVO", "MAILING": "MAILING_OURO_V1", "DESCONHECIDOS": 42.5, "INEXISTENTES": 28.1, "CAIXA_POSTAL": 15.4, "SUCESSO": 14.0},
        "TELEFONIA": {"LAT": 380, "SERVER": "Vivo Cloud", "SIP_CHANNELS": 200, "BUSY": 185, "JITTER": "15ms", "LOSS": "2.5%"}
    }

# --- 3. LÓGICA DE PROCESSAMENTO S.A. (CORREÇÃO DE CONVERSÃO V97) ---
LIMITE_PAUSA = 45
df_list = []
for k, v in st.session_state.db["OPERAÇÃO"].items():
    prom = v.get("PROMESSAS_N", 0)
    cpca = v.get("CPCA", 0)
    
    # REGRA ATUALIZADA: PROMESSA / CPCA [cite: 2026-01-29]
    conv = round((prom / cpca * 100), 1) if cpca > 0 else 0
    
    df_list.append({
        "OPERADOR": k, "CPF": v.get("CPF"), "ALÔ": v.get("ALO"), "CPC": v.get("CPC"), "CPCA": cpca, "PROMESSAS": prom,
        "CONV %": conv, "REAL": v.get("VALOR_REAL", 0.0), "X (-50%)": (v.get("PROJ", 0.0) * 0.5),
        "LOGADO": v.get("TEMPO_LOGADO", "00:00:00"), "PAUSA": v.get("PAUSA", 0),
        "SABOTAGEM": v.get("SABOTAGEM_SCORE", 0), "STATUS": v.get("STATUS")
    })
df_audit = pd.DataFrame(df_list)

# --- 4. FUNÇÕES DE RENDERIZAÇÃO (ESPELHAMENTO ABSOLUTO) ---
def render_placa_mestra(data, is_individual=False):
    st.markdown("### 📊 Bloco 01: Funil e Performance")
    c = st.columns(6)
    c[0].metric("Alô", int(data['ALÔ'].sum() if not is_individual else data['ALÔ']))
    c[1].metric("CPC", int(data['CPC'].sum() if not is_individual else data['CPC']))
    c[2].metric("CPCA", int(data['CPCA'].sum() if not is_individual else data['CPCA']))
    c[3].metric("Promessas", int(data['PROMESSAS'].sum() if not is_individual else data['PROMESSAS']))
    c[4].metric("Conv %", f"{data['CONV %'].mean() if not is_individual else data['CONV %']:.1f}%")
    c[5].metric("X (-50%)", f"R$ {data['X (-50%)'].sum() if not is_individual else data['X (-50%)']:,.2f}")
    
    st.divider()
    
    b1, b2, b3, b4 = st.columns(4)
    with b1:
        st.markdown("#### 🕒 Bloco 02: Tempo")
        st.write(f"**Logado:** {data['LOGADO'].max() if not is_individual else data['LOGADO']}")
        st.write(f"**Pausa:** {data['PAUSA'].sum() if not is_individual else data['PAUSA']} min")
    with b2:
        st.markdown("#### ☎️ Bloco 03: Discador")
        st.metric("IA-Sentinela", "ATIVO")
        st.write(f"Mailing: {st.session_state.db['DISCADOR']['MAILING']}")
    with b3:
        st.markdown("#### 📡 Bloco 04: Telefonia")
        st.metric("Latência", f"{st.session_state.db['TELEFONIA']['LAT']}ms")
        st.write(f"Server: {st.session_state.db['TELEFONIA']['SERVER']}")
    with b4:
        st.markdown("#### ⚠️ Ofensores")
        p_val = data["PAUSA"].sum() if not is_individual else data["PAUSA"]
        if p_val > LIMITE_PAUSA: st.markdown(f'<div class="ofensor-red">ALERTA: {p_val}m</div>', unsafe_allow_html=True)
        else: st.success("Normal")

# --- 5. INTERFACE DE COMANDO S.A. ---
st.markdown(f'<div class="manifesto-container"><div class="quote-text">"Enquanto o mundo olha para o avião que sobe, eu governo o código que o faz voar."</div><div class="signature">👊🚀📊⚖️🏁💎 — Comandante S.A.</div></div>', unsafe_allow_html=True)

# HIERARQUIA DE 7 ABAS (EXPORTAÇÃO POR ÚLTIMO)
tabs = st.tabs(["👑 01. COCKPIT", "👥 02. GESTÃO CPF", "☎️ 03. VISÃO DISCADOR", "📡 04. TELEFONIA TÁTICA", "🐍 05. SABOTAGEM", "⚖️ 06. JURÍDICO", "📂 07. EXPORTAÇÃO"])

# --- ABA 01: COCKPIT ---
with tabs[0]:
    render_placa_mestra(df_audit)
    st.subheader("🏁 Tabela da Favelinha")
    st.dataframe(df_audit.style.applymap(lambda x: 'color: red' if x > LIMITE_PAUSA else '', subset=['PAUSA']), use_container_width=True)

# --- ABA 02: GESTÃO CPF (ESPELHO) ---
with tabs[1]:
    st.header("👥 Espelhamento Individual")
    op_sel = st.selectbox("Auditar Operador:", df_audit["OPERADOR"].tolist())
    res_ind = df_audit[df_audit["OPERADOR"] == op_sel].iloc[0]
    st.info(f"AUDITANDO CPF: {res_ind['CPF']}")
    render_placa_mestra(res_ind, is_individual=True)
    st.radio("Comando Direto:", ["ENTRA", "PULA", "NÃO ENTRA"], horizontal=True)

# --- ABA 03: VISÃO DISCADOR ---
with tabs[2]:
    st.header("☎️ Inteligência de Mailing")
    d = st.session_state.db["DISCADOR"]
    st.error(f"Sintoma: {(d['DESCONHECIDOS'] + d['INEXISTENTES']):.1f}% de Lixo.")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="diag-box"><b>🔍 DIAGNÓSTICO:</b> Falha bureau/higienização.</div>', unsafe_allow_html=True)
        st.markdown('<div class="prog-box"><b>📈 PROGNÓSTICO:</b> Perda de 60% do CPCA.</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="sol-box"><b>✅ SOLUÇÃO S.A.:</b> Trocar Lote Imediatamente.</div>', unsafe_allow_html=True)

# --- ABA 04: TELEFONIA TÁTICA ---
with tabs[3]:
    st.header("📡 Inteligência de Rede")
    t = st.session_state.db["TELEFONIA"]
    st.error(f"Sintoma: Latência em {t['LAT']}ms.")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="diag-box"><b>🔍 DIAGNÓSTICO:</b> Congestionamento SIP Vivo.</div>', unsafe_allow_html=True)
        st.markdown('<div class="prog-box"><b>📈 PROGNÓSTICO:</b> Queda total em 15min.</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="sol-box"><b>✅ SOLUÇÃO S.A.:</b> Alternar para Tronco Reserva.</div>', unsafe_allow_html=True)

# --- ABA 05: SABOTAGEM E OMISSÃO ---
with tabs[4]:
    st.header("🐍 Módulo Anti-Sabotagem")
    op_sab = st.selectbox("Auditar Suspeita:", df_audit["OPERADOR"].tolist(), key="sab_sel")
    score = st.session_state.db["OPERAÇÃO"][op_sab].get("SABOTAGEM_SCORE", 0)
    st.warning(f"Score de Risco: {score}%")
    st.markdown('<div class="diag-box"><b>🔍 DIAGNÓSTICO:</b> Detecção de quedas propositais (Mudo).</div>', unsafe_allow_html=True)
    st.markdown('<div class="sol-box"><b>✅ SOLUÇÃO S.A.:</b> Bloqueio de terminal para acareação.</div>', unsafe_allow_html=True)

# --- ABA 06: JURÍDICO & COMPLIANCE ---
with tabs[5]:
    st.header("⚖️ Blindagem Legal")
    ofensores = df_audit[df_audit["PAUSA"] > LIMITE_PAUSA]
    for _, row in ofensores.iterrows():
        with st.expander(f"DOSSIÊ: {row['OPERADOR']}"):
            st.write(f"**Memorial:** Omissão detectada. {row['PAUSA']} min de pausa.")
            st.write(f"**Dano Patrimonial:** R$ {row['PAUSA'] * 0.92:.2f}")
            st.write("**Régua Disciplinar:** Sugestão de Advertência Escrita.")
            st.button(f"Emitir Termo - {row['CPF']}")

# --- ABA 07: EXPORTAÇÃO FORENSE ---
with tabs[6]:
    st.header("📂 Relatórios Ouro")
    csv_bytes = df_audit.to_csv(index=False).encode('utf-8-sig')
    hash_sha = hashlib.sha256(csv_bytes).hexdigest()
    st.info(f"**Hash Integridade (SHA-256):** {hash_sha}")
    st.write(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    st.download_button("EXTRAÇÃO BLINDADA", csv_bytes, "Relatorio_SA_V97.csv", "text/csv")
