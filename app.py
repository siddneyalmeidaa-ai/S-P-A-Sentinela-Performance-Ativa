import streamlit as st
import pandas as pd

# --- 1. SOBERANIA S.A. (ESTILO) ---
st.set_page_config(page_title="S.A. SUPREMO - V111", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    .stApp {background-color: #0E1117; color: #FFFFFF;}
    .selo-sidney {
        text-align: center; color: #FFD700; font-size: 20px; font-weight: bold; 
        border-bottom: 2px solid #FFD700; padding: 10px; margin-bottom: 15px;
    }
    .card-sa {
        background-color: #1A1C23; padding: 20px; border-radius: 12px;
        border: 1px solid #333; margin-bottom: 15px; border-left: 6px solid #FFD700;
    }
    .titulo-card { color: #FFD700; font-size: 14px; font-weight: bold; text-transform: uppercase; margin-bottom: 8px; }
    .valor-card { font-size: 28px; font-weight: bold; color: #FFFFFF; }
    .detalhe-tecnico { font-size: 13px; color: #AAAAAA; margin-top: 5px; line-height: 1.4; }
    
    .card-operador {
        background-color: #1A1C23; padding: 15px; border-radius: 12px;
        border: 1px solid #333; margin-bottom: 10px; border-left: 6px solid #FFD700;
    }
    .grid-metrics { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-top: 10px; font-size: 12px; }
    </style>
    <div class="selo-sidney">🔱 SIDNEY ALMEIDA - DASHBOARD SUPREMO V111 🔱</div>
    """, unsafe_allow_html=True)

# --- 2. DADOS ---
df = pd.DataFrame({
    'OPERADOR': ['PAULO', 'MARCOS', 'JESSICA'],
    'ALÔ': [150, 162, 100],
    'CPC': [90, 40, 50],
    'PROMESSA': [25, 5, 10],
    'VALOR': [2500.00, 500.00, 1200.00],
    'PAUSA_MIN': [35, 55, 40]
})

# --- 3. ABAS ---
abas = st.tabs(["👑 Cockpit", "👥 Gestão Visual", "☎️ Discador", "📡 Telefonia"])

# --- ABA 01: COCKPIT ---
with abas[0]:
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f'<div class="card-sa"><div class="titulo-card">💰 Faturamento</div><div class="valor-card">R$ {df["VALOR"].sum():,.2f}</div></div>', unsafe_allow_html=True)
    with c2:
        conv = (df['PROMESSA'].sum() / df['CPC'].sum()) * 100
        st.markdown(f'<div class="card-sa"><div class="titulo-card">📈 Conversão</div><div class="valor-card">{conv:.1f}%</div></div>', unsafe_allow_html=True)

# --- ABA 02: GESTÃO VISUAL ---
with abas[1]:
    for _, row in df.iterrows():
        status = "🚨 ALERTA" if row['PAUSA_MIN'] > 45 else "✅ OK"
        st.markdown(f"""
        <div class="card-operador">
            <div style="color:#FFD700; font-weight:bold;">👤 {row['OPERADOR']} | {status}</div>
            <div class="grid-metrics">
                <div>VALOR: R$ {row['VALOR']:,.2f}</div>
                <div>ALÔ: {row['ALÔ']}</div>
                <div>CPC: {row['CPC']}</div>
                <div>PROMESSAS: {row['PROMESSA']}</div>
                <div>PAUSA: {row['PAUSA_MIN']} min</div>
            </div>
        </div>""", unsafe_allow_html=True)

# --- ABA 03: DISCADOR (DETALHAMENTO PESADO) ---
with abas[2]:
    st.markdown(f"""
    <div class="card-sa">
        <div class="titulo-card">🔍 IA-SENTINELA: Diagnóstico de Vácuo</div>
        <div class="valor-card" style="color:#FF4B4B;">Vácuo Detectado (1.00x)</div>
        <div class="detalhe-tecnico">
            • <b>Causa Provável:</b> Mailing Saturado (Tentativas > 5)<br>
            • <b>Efeito:</b> Ocupação de linha sem conversão em ALÔ<br>
            • <b>Sugestão:</b> Reciclar base de dados ou aumentar o Ratio para 1:5
        </div>
    </div>
    <div class="card-sa">
        <div class="titulo-card">📊 Saúde do Mailing</div>
        <div class="valor-card">32%</div>
        <div class="detalhe-tecnico">
            • <b>Total Carregado:</b> 5.400 leads<br>
            • <b>Leads Virgens:</b> 120<br>
            • <b>Taxa de Atendimento:</b> 12% (Abaixo da média)
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- ABA 04: TELEFONIA (DETALHAMENTO TÉCNICO) ---
with abas[3]:
    st.markdown(f"""
    <div class="card-sa">
        <div class="titulo-card">📡 Estabilidade da Rota SIP</div>
        <div class="valor-card">Instável</div>
        <div class="detalhe-tecnico">
            • <b>Jitter:</b> 15ms (Oscilação detectada)<br>
            • <b>Perda de Pacotes:</b> 0.5%<br>
            • <b>Latência:</b> 85ms (Risco de voz robotizada)
        </div>
    </div>
    <div class="card-sa">
        <div class="titulo-card">📞 Troncos Ativos</div>
        <div class="valor-card">24 / 30</div>
        <div class="detalhe-tecnico">
            • <b>Canais em Uso:</b> 24 canais<br>
            • <b>Canais com Erro:</b> 6 canais (Timeout)
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown(f"--- \n **SISTEMA V111 ATIVO | STAKE: 1 Real**")
        
