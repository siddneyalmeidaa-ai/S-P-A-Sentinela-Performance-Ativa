import streamlit as st
import pandas as pd

# --- 1. SOBERANIA S.A. (ESTILO SUPREMO) ---
st.set_page_config(page_title="S.A. SUPREMO - V111", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    .stApp {background-color: #0E1117; color: #FFFFFF;}
    .selo-sidney {
        text-align: center; color: #FFD700; font-size: 20px; font-weight: bold; 
        border-bottom: 2px solid #FFD700; padding: 10px; margin-bottom: 15px;
    }
    .card-operador {
        background-color: #1A1C23; padding: 18px; border-radius: 12px;
        border: 1px solid #333; margin-bottom: 12px; border-left: 6px solid #FFD700;
    }
    .nome-op { color: #FFD700; font-weight: bold; font-size: 18px; text-transform: uppercase; }
    .grid-metrics { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-top: 15px; font-size: 14px; }
    .m-label { color: #AAAAAA; font-weight: normal; }
    .m-val { color: #FFFFFF; font-weight: bold; }
    </style>
    <div class="selo-sidney">🔱 SIDNEY ALMEIDA - DASHBOARD SUPREMO V111 🔱</div>
    """, unsafe_allow_html=True)

# --- 2. DADOS (PADRÃO OURO) ---
# Adicionado campo CPCA conforme solicitado
df = pd.DataFrame({
    'OPERADOR': ['PAULO', 'MARCOS', 'JESSICA'],
    'ALÔ': [150, 162, 100],
    'CPC': [90, 40, 50],
    'CPCA': [85, 38, 45], # Exemplo de dado CPCA
    'PROMESSA': [25, 5, 10],
    'VALOR': [2500.00, 500.00, 1200.00],
    'PAUSA_MIN': [35, 55, 40]
})

# --- 3. SISTEMA DE ABAS ---
abas = st.tabs(["👑 Cockpit", "👥 Gestão Visual", "☎️ Discador", "📡 Telefonia"])

# --- ABA 01: COCKPIT ---
with abas[0]:
    st.write("**Resumo Geral de Operação Ativo.**")

# --- ABA 02: GESTÃO VISUAL (FOCO TOTAL AQUI) ---
with abas[1]:
    st.subheader("👥 Performance Detalhada dos Operadores")
    
    for _, row in df.iterrows():
        # Lógica de Alerta
        status_icon = "✅ OK" if row['PAUSA_MIN'] <= 45 else "🚨 ALERTA"
        status_color = "#00FF00" if row['PAUSA_MIN'] <= 45 else "#FF4B4B"
        
        st.markdown(f"""
        <div class="card-operador">
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <div class="nome-op">👤 {row['OPERADOR']}</div>
                <div style="color:{status_color}; font-weight:bold;">{status_icon}</div>
            </div>
            <div class="grid-metrics">
                <div><span class="m-label">💰 VALOR:</span> <span class="m-val">R$ {row['VALOR']:,.2f}</span></div>
                <div><span class="m-label">📞 ALÔ:</span> <span class="m-val">{row['ALÔ']}</span></div>
                <div><span class="m-label">🎯 CPC:</span> <span class="m-val">{row['CPC']}</span></div>
                <div><span class="m-label">💎 CPCA:</span> <span class="m-val">{row['CPCA']}</span></div>
                <div><span class="m-label">🤝 PROMESSAS:</span> <span class="m-val">{row['PROMESSA']}</span></div>
                <div><span class="m-label">⏱️ PAUSA:</span> <span class="m-val">{row['PAUSA_MIN']} min</span></div>
            </div>
        </div>""", unsafe_allow_html=True)

# --- ABA 03: DISCADOR (SEM ALTERAÇÃO) ---
with abas[2]:
    st.info("Monitoramento de Discador mantido conforme padrão anterior.")

# --- ABA 04: TELEFONIA (SEM ALTERAÇÃO) ---
with abas[3]:
    st.info("Monitoramento de Telefonia mantido conforme padrão anterior.")

# --- FOOTER ---
st.markdown(f"--- \n **SISTEMA V111 ATIVO | STAKE: 1 Real**")
