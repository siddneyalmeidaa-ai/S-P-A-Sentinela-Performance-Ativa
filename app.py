import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. CONFIGURAÇÃO DE SEGURANÇA E INTERFACE ---
st.set_page_config(page_title="S.P.A. - Sidney Almeida", layout="wide", page_icon="🛰️")

# --- 2. QUANTUM MEMORY (BANCO DE DADOS EM SESSÃO) ---
if 'historico' not in st.session_state:
    # Dados mestre de inicialização
    st.session_state.historico = pd.DataFrame([
        {"DATA": "27/01/2026", "OPERADOR": "ANA", "ERRO": "NENHUM", "DETALHE": "PERFORMANCE IDEAL", "ESTORNO": 1250.40, "STATUS": "LIBERADO"},
        {"DATA": "27/01/2026", "OPERADOR": "MARCOS", "ERRO": "BLOCO 1", "DETALHE": "ERRO DE PROCESSO", "ESTORNO": 0.00, "STATUS": "PENDENTE"}
    ])

# --- 3. PAINEL DE COMANDO LATERAL (ONDE VOCÊ MEXE) ---
with st.sidebar:
    st.header("🎮 COMANDO S.P.A.")
    st.subheader("LANÇAR AUDITORIA")
    
    with st.form("form_auditoria"):
        nome = st.selectbox("OPERADOR", ["MARCOS", "ANA", "RICARDO", "JULIA"])
        categoria = st.selectbox("CATEGORIA MESTRE", ["NENHUM", "SABOTAGEM", "OMISSÃO", "BLOCO 1", "VÁCUO (1.00x)"])
        
        # Detalhamento dinâmico conforme sua regra de 'operator behavior'
        detalhe_texto = "N/A"
        if categoria == "SABOTAGEM":
            detalhe_texto = st.selectbox("TIPO DE SABOTAGEM", ["Desvio de Script", "Sabotagem de Dialer", "Desligamento Proposital", "Manipulação de Projeção"])
        elif categoria == "OMISSÃO":
            detalhe_texto = st.selectbox("TIPO DE OMISSÃO", ["Omissão de Valor", "Omissão de Histórico", "Falta de Registro"])
        elif categoria == "VÁCUO (1.00x)":
            detalhe_texto = "ZONA DE MORTE DETECTADA"

        valor = st.number_input("VALOR EXATO (R$)", min_value=0.0, step=0.10, format="%.2f")
        obs = st.text_input("OBSERVAÇÕES DO GESTOR")
        
        submit = st.form_submit_button("🚀 EXECUTAR E SINCRONIZAR")
        
        if submit:
            # Lógica Automática de Status e Projeção (-50% se Pendente)
            status_calc = "LIBERADO"
            if categoria == "VÁCUO (1.00x)": status_calc = "BLOQUEADO"
            elif categoria != "NENHUM": status_calc = "PENDENTE"
            
            novo_dado = pd.DataFrame([{
                "DATA": datetime.now().strftime("%d/%m/%Y"),
                "OPERADOR": nome,
                "ERRO": categoria,
                "DETAL
            
