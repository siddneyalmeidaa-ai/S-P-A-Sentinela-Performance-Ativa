import streamlit as st
import pandas as pd

# --- 1. SOBERANIA S.A. (CONFIGURAÇÃO) ---
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
        background-color: #1A1C23; padding: 15px; border-radius: 12px;
        border: 1px solid #333; margin-bottom: 15px; border-left: 6px solid #FFD700;
    }
    .nome-operador { color: #FFD700; font-size: 18px; font-weight: bold; margin-bottom: 10px; }
    .metrica-valor { font-size: 14px; color: #FFFFFF; }
    .label-metrica { color: #AAAAAA; font-size: 12px; }
    .status-alerta { color: #FF4B4B; font-weight: bold; font-size: 12px; margin-top: 5px; }
    .status-ok { color: #00FF00; font-weight: bold; font-size: 12px; margin-top: 5px; }
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

# --- ABA 01: COCKPIT ---
with abas[0]:
    total_v = df['VALOR'].sum()
    conv = (df['PROMESSA'].sum() / df['CPC'].sum()) * 100
    st.metric("VALOR TOTAL", f"R$ {total_v:,.2f}")
    st.metric("CONVERSÃO GERAL", f"{conv:.1f}%")
    st.divider()
    st.write(f"**Stake:** 1 Real")

# --- ABA 02: GESTÃO VISUAL (SEM TABELA) ---
with abas[1]:
    st.subheader("👥 Performance dos Operadores")
    
    # Filtro de Busca
    busca = st.text_input("🔍 Filtrar por nome:", "").upper()
    
    for _, row in df.iterrows():
        if busca in row['OPERADOR']:
            # Cálculo de conversão individual: Promessa / CPC
            conv_ind = (row['PROMESSA'] / row['CPC']) * 100 if row['CPC'] > 0 else 0
            
            # Card do Operador
            with st.container():
                alerta_status = ""
                if row['PAUSA_MIN'] > 45:
                    alerta_status = f"<div class='status-alerta'>⚠️ ALERTA: PAUSA EXCEDIDA ({row['PAUSA_MIN']} min)</div>"
                else:
                    alerta_status = f"<div class='status-ok'>✅ PAUSA OK ({row['PAUSA_MIN']} min)</div>"

                st.markdown(f"""
                <div class="card-operador">
                    <div class="nome-operador">👤 {row['OPERADOR']}</div>
                    <div style="display: flex; justify-content: space-between;">
                        <div>
                            <span class="label-metrica">VALOR</span><br>
                            <span class="metrica-valor">R$ {row['VALOR']:,.2f}</span>
                        </div>
                        <div>
                            <span class="label-metrica">CONVERSÃO</span><br>
                            <span class="metrica-valor">{conv_ind:.1f}%</span>
                        </div>
                        <div>
                            <span class="label-metrica">PROMESSAS</span><br>
                            <span class="metrica-valor">{row['PROMESSA']}</span>
                        </div>
                    </div>
                    {alerta_status}
                </div>
                """, unsafe_allow_html=True)

# --- ABA TÉCNICA ---
with abas[2]: # Discador
    st.info("Diagnóstico: Vácuo 1.00x | Solução: Reset IA-Sentinela")

# --- FOOTER ---
st.markdown(f"--- \n **SISTEMA V111 ATIVO**")
