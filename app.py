import streamlit as st
import pandas as pd
from datetime import datetime
import hashlib

# --- 1. CAMADA DE SOBERANIA (BLINDAGEM S.A.) ---
st.set_page_config(page_title="S.A. SUPREMO - V111", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp {background-color: #0E1117; color: #FFFFFF;}
    .selo-sidney {
        text-align: center; 
        color: #FFD700; 
        font-size: 26px; 
        font-weight: bold; 
        border-bottom: 2px solid #FFD700; 
        padding: 10px; 
        margin-bottom: 20px;
    }
    .metric-card {
        background-color: #1A1C23;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #FFD700;
        margin: 10px 0;
    }
    </style>
    <div class="selo-sidney">🔱 SIDNEY ALMEIDA - SUMÁRIO EXECUTIVO INTEGRAL V111 🔱</div>
    """, unsafe_allow_html=True)

# --- MEMÓRIA QUÂNTICA: DADOS INTEGRADOS ---
if 'dados' not in st.session_state:
    st.session_state.dados = {
        'OPERADOR': ['PAULO', 'MARCOS', 'TOTAL'],
        'ALÔ': [150, 162, 312],
        'CPC': [90, 40, 130],
        'CPCA': [90, 40, 130],
        'PROMESSA': [25, 5, 30],
        'VALOR': [2500.00, 500.00, 3000.00],
        'CONVERSÃO': ['27.7%', '12.3%', '23.0%'],
        'LOGIN': ['08:00', '08:15', '-'],
        'LOGOUT': ['17:00', '17:30', '-'],
        'TEMPO LOGADO': ['09:00', '09:15', '-'],
        'PAUSA 45': ['35m', '55m', '-'],
        'SCORE': [95, 42, 68]
    }

df = pd.DataFrame(st.session_state.dados)

# --- ARQUITETURA DE ABAS ---
abas = st.tabs([
    "👑 Cockpit", "👥 Gestão", "☎️ Discador", 
    "📡 Telefonia", "🐍 Sabotagem", "⚖️ Jurídico", "📂 Exportação"
])

# --- ABA 01: COCKPIT (IMUTÁVEL) ---
with abas[0]:
    st.subheader("👑 Cockpit - Central Macro")
    st.table(df[['OPERADOR', 'ALÔ', 'CPC', 'CPCA', 'PROMESSA', 'VALOR', 'CONVERSÃO']])
    
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("⏱️ Gestão de Tempo")
        st.dataframe(df[['OPERADOR', 'LOGIN', 'LOGOUT', 'TEMPO LOGADO', 'PAUSA 45']])
    with c2:
        st.subheader("🔥 Mapa de Calor de Pausas")
        for i, row in df.iterrows():
            if row['OPERADOR'] != 'TOTAL':
                tempo = int(row['PAUSA 45'].replace('m', ''))
                if tempo > 45:
                    st.error(f"ALERTA: {row['OPERADOR']} excedeu a Trava 45 ({tempo}min)")
                else:
                    st.success(f"{row['OPERADOR']}: {tempo}min (Dentro da meta)")

# --- ABA 02: GESTÃO OPERADOR (TRAVA -50%) ---
with abas[1]:
    st.subheader("👥 Gestão por CPF")
    op_ref = st.selectbox("Selecione para Auditoria:", df['OPERADOR'][:-1])
    dados_op = df[df['OPERADOR'] == op_ref].iloc[0]
    
    v_bruto = dados_op['VALOR']
    v_liberado = v_bruto * 0.50 # Regra de Ouro: -50%
    
    st.markdown(f"""
    <div class='metric-card'>
        <h3>PROJEÇÃO META X</h3>
        <p>VALOR PENDENTE: R$ {v_bruto}</p>
        <h2 style='color: #00FF00;'>VALOR LIBERADO: R$ {v_liberado}</h2>
        <p><small>Trava de Segurança S.A. aplicada: -50%</small></p>
    </div>
    """, unsafe_allow_html=True)
    
    col_btn1, col_btn2, col_btn3 = st.columns(3)
    with col_btn1: st.button("🟢 ENTRA", key="e1", use_container_width=True)
    with col_btn2: st.button("🟡 PULA", key="p1", use_container_width=True)
    with col_btn3: st.button("🔴 NÃO ENTRA", key="n1", use_container_width=True)

# --- ABA 03: VISÃO DISCADOR (MAILING) ---
with abas[2]:
    st.subheader("☎️ Inteligência de Mailing")
    audit_m = pd.DataFrame({
        'DIAGNÓSTICO': ['Desconhecidos (Massa)', 'Vácuo (1.00x)', 'CPC Fantasma'],
        'SOLUÇÃO': ['Higienizar Base', 'Trocar Mailing', 'IA-Sentinela Ativa'],
        'IMPACTO': ['- R$ 300,00', '- R$ 850,00', '- R$ 150,00']
    })
    st.table(audit_m)

# --- ABA 04: VISÃO TELEFONIA (LINK) ---
with abas[3]:
    st.subheader("📡 Auditoria de Link e Rede")
    audit_t = pd.DataFrame({
        'MÉTRICA': ['Latência', 'Jitter', 'Sincronia SIP'],
        'STATUS': ['12ms (Verde)', '0.8ms (Estável)', 'Sincronizado'],
        'SAÚDE': ['100%', '100%', 'OK']
    })
    st.table(audit_t)

# --- ABA 05: SABOTAGEM (O SENTINELA) ---
with abas[4]:
    st.subheader("🐍 Perfilamento Comportamental")
    st.write("Cruzamento de Dados: Operador vs. Sistema")
    
    for i, row in df.iterrows():
        if row['OPERADOR'] != 'TOTAL':
            score = row['SCORE']
            status = "🔴 SABOTADOR" if score < 50 else "🟢 CONFIÁVEL"
            st.write(f"**{row['OPERADOR']}** | Score: {score}% | Status: {status}")
            st.progress(score / 100)

# --- ABA 06: JURÍDICO (ART. 482) ---
with abas[5]:
    st.subheader("⚖️ Blindagem Jurídica")
    st.warning("AUDITORIA: Se Link (Aba 04) está OK e Produção está Baixa = DESÍDIA.")
    
    with st.expander("Gerar Advertência"):
        op_jur = st.selectbox("Operador Infrator:", df['OPERADOR'][:-1], key="jur")
        st.text_area("Enquadramento:", f"Art. 482 CLT alínea (e) - Desídia comprovada por ociosidade deliberada e Pausas Fantasmas.")
        st.button("Gerar PDF de Advertência")

# --- ABA 07: EXPORTAÇÃO FORENSE (SEM ERRO DE ACENTO) ---
with abas[6]:
    st.subheader("📂 Exportação de Dossiê 360º")
    
    # Gerando Hash SHA-256 para o relatório
    hash_obj = hashlib.sha256(str(datetime.now()).encode())
    hash_res = hash_obj.hexdigest()[:12].upper()
    
    st.write(f"Assinatura Digital da Rodada: **{hash_res}**")
    
    # Preparando CSV com codificação para celular (UTF-8-SIG)
    csv = df.to_csv(index=False).encode('utf-16')
    
    st.download_button(
        label="📥 Baixar Relatório Completo (Saneado)",
        data=csv,
        file_name=f"SA_SUPREMO_V111_{datetime.now().strftime('%d_%m_%Y')}.csv",
        mime="text/csv"
    )

# --- FOOTER ---
st.markdown(f"--- \n **SISTEMA V111 ATIVO** | {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} | STAKE: **1 Real**")
                     
