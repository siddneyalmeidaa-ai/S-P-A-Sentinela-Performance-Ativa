import streamlit as st
import pandas as pd

# --- 1. SOBERANIA S.A. (ESTILO UNIFICADO) ---
st.set_page_config(page_title="S.A. SUPREMO - V111", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    .stApp {background-color: #0E1117; color: #FFFFFF;}
    .selo-sidney {
        text-align: center; color: #FFD700; font-size: 20px; font-weight: bold; 
        border-bottom: 2px solid #FFD700; padding: 10px; margin-bottom: 15px;
    }
    /* ESTILO DOS CARDS IGUALADOS */
    .card-sa {
        background-color: #1A1C23; padding: 20px; border-radius: 12px;
        border: 1px solid #333; margin-bottom: 15px; border-left: 6px solid #FFD700;
        text-align: center;
    }
    .titulo-card { color: #FFD700; font-size: 14px; font-weight: bold; text-transform: uppercase; margin-bottom: 8px; }
    .valor-card { font-size: 32px; font-weight: bold; color: #FFFFFF; }
    .sub-card { color: #AAAAAA; font-size: 12px; margin-top: 5px; }
    
    .card-operador {
        background-color: #1A1C23; padding: 15px; border-radius: 12px;
        border: 1px solid #333; margin-bottom: 10px; border-left: 6px solid #FFD700;
    }
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
    'PAUSA_MIN': [35, 55, 40],
    'LOGADO_MIN': [540, 555, 530]
})

# --- 3. ABAS ---
abas = st.tabs(["👑 Cockpit", "👥 Gestão Visual", "☎️ Discador", "📡 Telefonia"])

# --- ABA 01: COCKPIT (AGORA COM CARDS) ---
with abas[0]:
    total_v = df['VALOR'].sum()
    total_p = df['PROMESSA'].sum()
    total_c = df['CPC'].sum()
    conv_geral = (total_p / total_c) * 100 if total_c > 0 else 0
    
    # Grid de Cards no Cockpit
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""<div class="card-sa">
            <div class="titulo-card">💰 Valor Total</div>
            <div class="valor-card">R$ {total_v:,.2f}</div>
            <div class="sub-card">Meta Liberada: 50%</div>
        </div>""", unsafe_allow_html=True)
    with col2:
        st.markdown(f"""<div class="card-sa">
            <div class="titulo-card">📈 Conversão Geral</div>
            <div class="valor-card">{conv_geral:.1f}%</div>
            <div class="sub-card">Promessa / CPC</div>
        </div>""", unsafe_allow_html=True)

    col3, col4 = st.columns(2)
    with col3:
        st.markdown(f"""<div class="card-sa">
            <div class="titulo-card">🤝 Promessas</div>
            <div class="valor-card">{total_p}</div>
            <div class="sub-card">Volume de Prova</div>
        </div>""", unsafe_allow_html=True)
    with col4:
        st.markdown(f"""<div class="card-sa">
            <div class="titulo-card">⏱️ Média de Pausa</div>
            <div class="valor-card">{int(df['PAUSA_MIN'].mean())} min</div>
            <div class="sub-card">Teto: 45 min</div>
        </div>""", unsafe_allow_html=True)

# --- ABA 02: GESTÃO VISUAL (MANTIDA) ---
with abas[1]:
    st.subheader("👥 Performance dos Operadores")
    for _, row in df.iterrows():
        c_ind = (row['PROMESSA'] / row['CPC']) * 100 if row['CPC'] > 0 else 0
        status_h = f"<div style='color:#FF4B4B;'>⚠️ ALERTA ({row['PAUSA_MIN']}m)</div>" if row['PAUSA_MIN'] > 45 else f"<div style='color:#00FF00;'>✅ OK ({row['PAUSA_MIN']}m)</div>"
        
        st.markdown(f"""
        <div class="card-operador">
            <div style="color:#FFD700; font-weight:bold;">👤 {row['OPERADOR']}</div>
            <div style="display:flex; justify-content:space-between; margin-top:5px;">
                <span>R$ {row['VALOR']:,.2f}</span>
                <span>{c_ind:.1f}% Conv.</span>
                {status_h}
            </div>
        </div>
        """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown(f"--- \n **SISTEMA V111 ATIVO | STAKE: 1 REAL**")
    
