import streamlit as st
import pandas as pd

# --- 1. SOBERANIA S.A. (ESTILO INTEGRAL) ---
st.set_page_config(page_title="S.A. SUPREMO - V111", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    .stApp {background-color: #0E1117; color: #FFFFFF;}
    .selo-sidney {
        text-align: center; color: #FFD700; font-size: 20px; font-weight: bold; 
        border-bottom: 2px solid #FFD700; padding: 10px; margin-bottom: 15px;
    }
    /* PADRÃO DE CARDS SUPREMO */
    .card-sa {
        background-color: #1A1C23; padding: 20px; border-radius: 12px;
        border: 1px solid #333; margin-bottom: 15px; border-left: 6px solid #FFD700;
        text-align: center;
    }
    .titulo-card { color: #FFD700; font-size: 14px; font-weight: bold; text-transform: uppercase; margin-bottom: 8px; }
    .valor-card { font-size: 28px; font-weight: bold; color: #FFFFFF; }
    .sub-card { color: #AAAAAA; font-size: 12px; margin-top: 5px; }
    
    .card-operador {
        background-color: #1A1C23; padding: 15px; border-radius: 12px;
        border: 1px solid #333; margin-bottom: 10px; border-left: 6px solid #FFD700;
    }
    </style>
    <div class="selo-sidney">🔱 SIDNEY ALMEIDA - DASHBOARD SUPREMO V111 🔱</div>
    """, unsafe_allow_html=True)

# --- 2. DADOS (PADRÃO OURO) ---
df = pd.DataFrame({
    'OPERADOR': ['PAULO', 'MARCOS', 'JESSICA'],
    'ALÔ': [150, 162, 100],
    'CPC': [90, 40, 50],
    'PROMESSA': [25, 5, 10],
    'VALOR': [2500.00, 500.00, 1200.00],
    'PAUSA_MIN': [35, 55, 40],
    'LOGADO_MIN': [540, 555, 530]
})

# --- 3. ABAS UNIFICADAS ---
abas = st.tabs(["👑 Cockpit", "👥 Gestão Visual", "☎️ Discador", "📡 Telefonia"])

# --- ABA 01: COCKPIT ---
with abas[0]:
    total_v = df['VALOR'].sum()
    total_p = df['PROMESSA'].sum()
    total_c = df['CPC'].sum()
    conv_geral = (total_p / total_c) * 100 if total_c > 0 else 0
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f'<div class="card-sa"><div class="titulo-card">💰 Valor Total</div><div class="valor-card">R$ {total_v:,.2f}</div><div class="sub-card">Meta Liberada: 50%</div></div>', unsafe_allow_html=True)
    with c2:
        st.markdown(f'<div class="card-sa"><div class="titulo-card">📈 Conversão</div><div class="valor-card">{conv_geral:.1f}%</div><div class="sub-card">Média do Time</div></div>', unsafe_allow_html=True)

# --- ABA 02: GESTÃO VISUAL ---
with abas[1]:
    for _, row in df.iterrows():
        c_ind = (row['PROMESSA'] / row['CPC']) * 100 if row['CPC'] > 0 else 0
        status = f"<span style='color:#FF4B4B;'>🚨 ALERTA</span>" if row['PAUSA_MIN'] > 45 else f"<span style='color:#00FF00;'>✅ OK</span>"
        st.markdown(f"""
        <div class="card-operador">
            <div style="color:#FFD700; font-weight:bold;">👤 {row['OPERADOR']}</div>
            <div style="display:flex; justify-content:space-between; margin-top:5px;
    
