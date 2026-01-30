import streamlit as st
import pandas as pd

# --- 1. CONFIGURAÇÃO SOBERANIA S.A. ---
st.set_page_config(page_title="S.A. SUPREMO - V111", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    .stApp {background-color: #0E1117; color: #FFFFFF;}
    .selo-sidney {
        text-align: center; color: #FFD700; font-size: 20px; font-weight: bold; 
        border-bottom: 2px solid #FFD700; padding: 10px; margin-bottom: 15px;
    }
    /* ESTILO DOS CARDS SUPREMO */
    .card-sa {
        background-color: #1A1C23; padding: 20px; border-radius: 12px;
        border: 1px solid #333; margin-bottom: 15px; border-left: 6px solid #FFD700;
    }
    .titulo-card { color: #FFD700; font-size: 14px; font-weight: bold; text-transform: uppercase; margin-bottom: 8px; }
    .valor-card { font-size: 28px; font-weight: bold; color: #FFFFFF; }
    .detalhe-tecnico { font-size: 13px; color: #AAAAAA; margin-top: 5px; line-height: 1.4; }
    
    .card-operador {
        background-color: #1A1C23; padding: 18px; border-radius: 12px;
        border: 1px solid #333; margin-bottom: 12px; border-left: 6px solid #FFD700;
    }
    .nome-op { color: #FFD700; font-weight: bold; font-size: 18px; text-transform: uppercase; }
    .grid-metrics { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-top: 15px; font-size: 14px; }
    .m-label { color: #AAAAAA; }
    .m-val { color: #FFFFFF; font-weight: bold; }
    </style>
    <div class="selo-sidney">🔱 SIDNEY ALMEIDA - DASHBOARD SUPREMO V111 🔱</div>
    """, unsafe_allow_html=True)

# --- 2. DADOS (PADRÃO OURO) ---
df = pd.DataFrame({
    'OPERADOR': ['PAULO', 'MARCOS', 'JESSICA'],
    'ALÔ': [150, 162, 100],
    'CPC': [90, 40, 50],
    'CPCA': [85, 38, 45],
    'PROMESSA': [25, 5, 10],
    'VALOR': [2500.00, 500.00, 1200.00],
    'PAUSA_MIN': [35, 55, 40]
})

# --- 3. ABAS UNIFICADAS ---
abas = st.tabs(["👑 Cockpit", "👥 Gestão Visual", "☎️ Discador", "📡 Telefonia"])

# --- ABA 01: COCKPIT (RESTAURADO COM CARDS) ---
with abas[0]:
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"""<div class="card-sa">
            <div class="titulo-card">💰 VALOR TOTAL</div>
            <div class="valor-card">R$ {df['VALOR'].sum():,.2f}</div>
            <div class="detalhe-tecnico">Meta Liberada: 50%</div>
        </div>""", unsafe_allow_html=True)
    with c2:
        conv = (df['PROMESSA'].sum() / df['CPC'].sum()) * 100
        st.markdown(f"""<div class="card-sa">
            <div class="titulo-card">📈 CONVERSÃO GERAL</div>
            <div class="valor-card">{conv:.1f}%</div>
            <div class="detalhe-tecnico">CPCA / Promessa</div>
        </div>""", unsafe_allow_html=True)
    
    c3, c4 = st.columns(2)
    with c3:
        st.markdown(f"""<div class="card-sa">
            <div class="titulo-card">🤝 TOTAL PROMESSAS</div>
            <div class="valor-card">{df['PROMESSA'].sum()}</div>
            <div class="detalhe-tecnico">Volume de Prova</div>
        </div>""", unsafe_allow_html=True)
    with c4:
        st.markdown(f"""<div class="card-sa">
            <div class="titulo-card">⏱️ MÉDIA DE PAUSA</div>
            <div class="valor-card">{int(df['PAUSA_MIN'].mean())} min</div>
            <div class="detalhe-tecnico">Teto: 45 min</div>
        </div>""", unsafe_allow_html=True)

# --- ABA 02: GESTÃO VISUAL (PERFEITA) ---
with abas[1]:
    for _, row in df.iterrows():
        status = "✅ OK" if row['PAUSA_MIN'] <= 45 else "🚨 ALERTA"
        color = "#00FF00" if row['PAUSA_MIN'] <= 45 else "#FF4B4B"
        st.markdown(f"""
        <div class="card-operador">
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <div class="nome-op">👤 {row['OPERADOR']}</div>
                <div style="color:{color}; font-weight:bold;">{status}</div>
            </div>
            <div class="grid-metrics">
                <div>💰 <span class="m-label">VALOR:</span> <span class="m-val">R$ {row['VALOR']:,.2f}</span></div>
                <div>📞 <span class="m-label">ALÔ:</span> <span class="m-val">{row['ALÔ']}</span></div>
                <div>🎯 <span class="m-label">CPC:</span> <span class="m-val">{row['CPC']}</span></div>
                <div>💎 <span class="m-label">CPCA:</span> <span class="m-val">{row['CPCA']}</span></div>
                <div>🤝 <span class="m-label">PROMESSAS:</span> <span class="m-val">{row['PROMESSA']}</span></div>
                <div>⏱️ <span class="m-label">PAUSA:</span> <span class="m-val">{row['PAUSA_MIN']} min</span></div>
            </div>
        </div>""", unsafe_allow_html=True)

# --- ABA 03: DISCADOR (DETALHADO) ---
with abas[2]:
    st.markdown(f"""
    <div class="card-sa">
        <div class="titulo-card">🔍 IA-SENTINELA</div>
        <div class="valor-card">Vácuo (1.00x)</div>
        <div class="detalhe-tecnico">
            <b>Status:</b> Zonas Mortas Detectadas<br>
            <b>Ação:</b> Reciclar Mailing Imediatamente
        </div>
    </div>""", unsafe_allow_html=True)

# --- ABA 04: TELEFONIA (DETALHADA) ---
with abas[3]:
    st.markdown(f"""
    <div class="card-sa">
        <div class="titulo-card">📡 STATUS DA REDE</div>
        <div class="valor-card">45ms</div>
        <div class="detalhe-tecnico">
            <b>Estabilidade:</b> 98.5%<br>
            <b>Troncos:</b> 24 Canais Ativos
        </div>
    </div>""", unsafe_allow_html=True)

# --- FOOTER ---
st.markdown(f"--- \n **SISTEMA V111 ATIVO | STAKE: 1 Real**")
