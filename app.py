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
    .metric-card {
        background-color: #1A1C23; padding: 12px; border-radius: 8px;
        border-left: 4px solid #FFD700; margin: 5px 0;
    }
    .metric-card h3 { font-size: 13px; color: #FFD700; text-transform: uppercase; margin: 0; }
    .metric-card h2 { font-size: 24px; font-weight: bold; margin: 5px 0; }
    </style>
    <div class="selo-sidney">🔱 SIDNEY ALMEIDA - DASHBOARD SUPREMO V111 🔱</div>
    """, unsafe_allow_html=True)

# --- 2. DADOS (MEMÓRIA QUÂNTICA) ---
if 'dados_v111' not in st.session_state:
    st.session_state.dados_v111 = pd.DataFrame({
        'OPERADOR': ['PAULO', 'MARCOS', 'JESSICA'],
        'ALÔ': [150, 162, 100],
        'CPC': [90, 40, 50],
        'PROMESSA': [25, 5, 10],
        'VALOR': [2500.00, 500.00, 1200.00],
        'PAUSA_MIN': [35, 55, 40],
        'LOGADO_MIN': [540, 555, 530]
    })

df = st.session_state.dados_v111

# --- 3. INTERFACE DE ABAS ---
abas = st.tabs(["👑 Cockpit", "👥 Gestão", "☎️ Discador", "📡 Telefonia", "🐍 Sabotagem", "📂 Exportação"])

# --- ABA 01: COCKPIT (SUMÁRIO) ---
with abas[0]:
    total_valor = df['VALOR'].sum()
    total_promessas = df['PROMESSA'].sum()
    total_cpc = df['CPC'].sum()
    conversao = (total_promessas / total_cpc) * 100 if total_cpc > 0 else 0

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f"<div class='metric-card'><h3>VALOR TOTAL</h3><h2>R$ {total_valor:,.2f}</h2></div>", unsafe_allow_html=True)
    with c2:
        st.markdown(f"<div class='metric-card'><h3>PRODUTIVIDADE</h3><h2>{total_promessas}</h2></div>", unsafe_allow_html=True)
    with c3:
        st.markdown(f"<div class='metric-card'><h3>CONVERSÃO</h3><h2>{conversao:.1f}%</h2></div>", unsafe_allow_html=True)
    
    st.divider()
    st.write(f"**Média de Pausa:** {int(df['PAUSA_MIN'].mean())} min")

# --- ABA 02: GESTÃO (COM FILTRO POR OPERADOR) ---
with abas[1]:
    st.subheader("👥 Gestão de Operadores")
    
    # CRIAÇÃO DO FILTRO
    lista_operadores = ["TODOS"] + sorted(df['OPERADOR'].unique().tolist())
    operador_selecionado = st.selectbox("🔍 Buscar por Operador:", lista_operadores)
    
    # APLICAÇÃO DO FILTRO
    if operador_selecionado == "TODOS":
        df_filtrado = df
    else:
        df_filtrado = df[df['OPERADOR'] == operador_selecionado]
    
    # EXIBIÇÃO DA TABELA FILTRADA
    st.table(df_filtrado)
    
    # Alerta de Pausa específico para o selecionado
    if operador_selecionado != "TODOS":
        pausa = df_filtrado['PAUSA_MIN'].values[0]
        if pausa > 45:
            st.error(f"🚨 {operador_selecionado} está acima da meta de pausa ({pausa} min)!")
        else:
            st.success(f"✅ {operador_selecionado} está dentro da meta ({pausa} min).")

# --- ABAS TÉCNICAS ---
with abas[2]: # Discador
    st.table(pd.DataFrame({'DIAGNÓSTICO': ['Vácuo 1.00x'], 'SOLUÇÃO': ['Reset IA-Sentinela']}))

with abas[3]: # Telefonia
    st.table(pd.DataFrame({'DIAGNÓSTICO': ['Latência Alta'], 'SOLUÇÃO': ['Reset Rota SIP']}))

# --- FOOTER ---
st.markdown(f"--- \n **SISTEMA V111 ATIVO** | STAKE: **1 Real**")
