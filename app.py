import streamlit as st
import pandas as pd
import hashlib
from datetime import datetime
import io

# --- 1. CONFIGURAÇÃO E BLINDAGEM S.A. ---
st.set_page_config(page_title="S.P.A. MASTER - SIDNEY ALMEIDA", layout="wide", page_icon="🛰️")

# CSS para Dark Mode S.A. e Ocultação de Menus Nativos
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

# --- 3. LÓGICA DE PROCESSAMENTO S.A. ---
LIMITE_PAUSA = 45
df_list = []
for k, v in st.session_state.db["OPERAÇÃO"].items():
    prom, cpca = v.get("PROMESSAS_N", 0), v.get("CPCA", 0)
    df_list.append({
        "OPERADOR": k, "CPF": v.get("CPF"), "ALÔ": v.get("ALO"), "CPC": v.get("CPC"), "CPCA": cpca, "PROMESSAS": prom,
        "CONV %": round((cpca / prom * 100), 1) if prom > 0 else 0,
        "REAL": v.get("VALOR_REAL", 0.0), "X (-50%)": v.get("PROJ", 0.0) * 0.5,
        "LOGADO": v.get("TEMPO_LOGADO", "00:00:00"), "PAUSA": v.get("PAUSA", 0),
        "SABOTAGEM": v.get("SABOTAGEM_SCORE", 0), "STATUS": v.get("STATUS")
    })
df_audit = pd.DataFrame(df_list)

# --- 4. FUNÇÕES DE INTERFACE ESPELHADA ---
def render_placa_mestra(data, is_individual=False):
    # BLOCO 01: FUNIL
    st.markdown("### 📊 Bloco 01: Funil e Performance")
    c = st.columns(6)
    c[0].metric("Alô", int(data['ALÔ'].sum() if not is_individual else data['ALÔ']))
    c[1].metric("CPC", int(data['CPC'].sum() if not is_individual else data['CPC']))
    c[2].metric("CPCA", int(data['CPCA'].sum() if not is_individual else data['CPCA']))
    c[3].metric("Promessas", int(data['PROMESSAS'].sum() if not is_individual else data['PROMESSAS']))
    c[4].metric("Conv %", f"{data['CONV %'].mean() if not is_individual else data['CONV %']:.1f}%")
    c[5].metric("X (-50%)", f"R$ {data['X (-50%)'].sum() if not is_individual else data['X (-50%)']:,.2f}")
    
    st.divider()
    # BLOCO 02, 03, 04 (O TELEFONINHO E O DISCADOR)
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
        else: st.success("Operação Limpa")

# --- 5. INTERFACE DE COMANDO ---
st.markdown(f'<div class="manifesto-container"><div class="quote-text">"Enquanto o mundo olha para o avião que sobe, eu governo o código que o faz voar."</div><div class="signature">👊🚀📊⚖️🏁💎 — Comandante S.A.</div></div>', unsafe_allow_html=True)

tabs = st.tabs(["👑 01. COCKPIT", "👥 02. GESTÃO CPF", "☎️ 03. VISÃO DISCADOR", "📡 04. TELEFONIA TÁTICA", "🐍 05. SABOTAGEM", "⚖️ 06. JURÍDICO", "📂 07. EXPORTAÇÃO"])

# ABA 01: COCKPIT MACRO
with tabs[0]:
    render_placa_mestra(df_audit)
    st.subheader("🏁 Tabela da Favelinha")
    st.dataframe(df_audit, use_container_width=True)

# ABA 02: GESTÃO CPF (O ESPELHO)
with tabs[1]:
    op_sel = st.selectbox("Selecione Operador para Auditoria:", df_audit["OPERADOR"].tolist())
    res_ind = df_audit[df_audit["OPERADOR"] == op_sel].iloc[0]
    st.info(f"AUDITANDO TERMINAL: {res_ind['CPF']}")
    render_placa_mestra(res_ind, is_individual=True)
    st.radio("Comando Direto:", ["ENTRA", "PULA", "NÃO ENTRA"], horizontal=True)

# ABA 03: VISÃO DISCADOR
with tabs[2]:
    st.header("☎️ Inteligência de Mailing")
    d = st.session_state.db["DISCADOR"]
    st.error(f"Sintoma: {(d['DESCONHECIDOS'] + d['INEXISTENTES']):.1f}% de Lixo Detectado.")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f'<div class="diag-box"><b>🔍 DIAGNÓSTICO:</b> Mailing corrompido ou bureau antigo.</div>', unsafe_allow_html=True)
    with c2:
        st.markdown(f'<div class="sol-box"><b>✅ SOLUÇÃO S.A.:</b> Trocar para Lote Reserva Imediatamente.</div>', unsafe_allow_html=True)

# ABA 04: TELEFONIA TÁTICA
with tabs[3]:
    st.header("📡 Inteligência de Rede")
    t = st.session_state.db["TELEFONIA"]
    st.error(f"Sintoma: Latência Crítica {t['LAT']}ms.")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f'<div class="diag-box"><b>🔍 DIAGNÓSTICO:</b> Saturação no Gateway Vivo Cloud.</div>', unsafe_allow_html=True)
    with c2:
        st.markdown(f'<div class="sol-box"><b>✅ SOLUÇÃO S.A.:</b> Migrar para Tronco SIP de Contingência.</div>', unsafe_allow_html=True)

# ABA 05: SABOTAGEM E OMISSÃO
with tabs[4]:
    st.header("🐍 Módulo Anti-Sabotagem")
    op_sab = st.selectbox("Auditar Sabotagem:", df_audit["OPERADOR"].tolist(), key="sab")
    score = st.session_state.db["OPERAÇÃO"][op_sab].get("SABOTAGEM_SCORE", 0)
    if score > 50:
        st.error(f"⚠️ Alerta de Sabotagem: Score {score}%")
        st.markdown(f'<div class="diag-box"><b>🔍 DIAGNÓSTICO:</b> Operador forçando quedas e desligando em mudo.</div>', unsafe_allow_html=True)
    else: st.success("Nenhuma anomalia detectada.")

# ABA 06: JURÍDICO E COMPLIANCE
with tabs[5]:
    st.header("⚖️ Blindagem Jurídica")
    ofensores = df_audit[df_audit["PAUSA"] > LIMITE_PAUSA]
    for _, row in ofensores.iterrows():
        st.warning(f"Dossiê: {row['OPERADOR']}")
        st.write(f"**Memorial Descritivo:** Operador ausente por {row['PAUSA']} minutos. Conduta gera ociosidade forçada.")
        st.write(f"**Dano Patrimonial:** R$ {row['PAUSA'] * 0.85:.2f} (Tempo Logado Ocioso)")
        st.button(f"Gerar Advertência - {row['OPERADOR']}")

# ABA 07: EXPORTAÇÃO FORENSE (SEMPRE A ÚLTIMA)
with tabs[6]:
    st.header("📂 Relatórios Ouro")
    csv_data = df_audit.to_csv(index=False).encode('utf-8-sig')
    hash_val = hashlib.sha256(csv_data).hexdigest()
    
    st.info(f"**Hash de Integridade (SHA-256):** {hash_val}")
    st.write(f"Log de Extração: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} | IP: 187.xx.xx.xx")
    st.download_button("BAIXAR RELATÓRIO BLINDADO", csv_data, f"S_A_V96_{datetime.now().strftime('%d%m%Y')}.csv", "text/csv")
