import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. CONFIGURAÇÃO ---
st.set_page_config(page_title="S.P.A. - Sidney Almeida", layout="wide", page_icon="🛰️")

# --- 2. BANCO DE DADOS (MEMÓRIA) ---
if 'historico' not in st.session_state:
    st.session_state.historico = pd.DataFrame(columns=["DATA", "OPERADOR", "CATEGORIA", "DETALHE", "ESTORNO", "STATUS", "OBS"])

# --- 3. BARRA LATERAL (PAINEL DE LANÇAMENTO) ---
with st.sidebar:
    st.header("🎮 COMANDO S.P.A.")
    with st.form("auditoria_form"):
        st.subheader("Nova Auditoria")
        nome = st.selectbox("OPERADOR", ["ANA", "MARCOS", "RICARDO", "JULIA"])
        cat = st.selectbox("CATEGORIA", ["NENHUM", "SABOTAGEM", "OMISSÃO", "BLOCO 1", "VÁCUO (1.00x)"])
        
        # Detalhamento dinâmico
        det = "PERFORMANCE IDEAL"
        if cat == "SABOTAGEM":
            det = st.selectbox("TIPO DE SABOTAGEM", ["Desvio de Script", "Sabotagem de Dialer", "Desligamento Proposital", "Manipulação de Projeção"])
        elif cat == "OMISSÃO":
            det = st.selectbox("TIPO DE OMISSÃO", ["Omissão de Valor", "Omissão de Histórico", "Falta de Registro"])
        elif cat == "VÁCUO (1.00x)":
            det = "VÁCUO DE OPERAÇÃO"

        valor_est = st.number_input("ESTORNO RECUPERADO (R$)", min_value=0.0, step=0.10)
        comentario = st.text_input("OBSERVAÇÃO")
        
        if st.form_submit_button("🚀 SALVAR E SINCRONIZAR"):
            # Lógica de Status
            st_calc = "LIBERADO"
            if cat == "VÁCUO (1.00x)": st_calc = "BLOQUEADO"
            elif cat != "NENHUM": st_calc = "PENDENTE"
            
            novo = pd.DataFrame([{
                "DATA": datetime.now().strftime("%d/%m/%Y"),
                "OPERADOR": nome,
                "CATEGORIA": cat,
                "DETALHE": det,
                "ESTORNO": valor_est,
                "STATUS": st_calc,
                "OBS": comentario
            }])
            st.session_state.historico = pd.concat([st.session_state.historico, novo], ignore_index=True)
            st.success(f"REGISTRO DE {nome} ENVIADO!")

# --- 4. DASHBOARD PRINCIPAL ---
st.title("🛰️ S.P.A. - SENTINELA DE PERFORMANCE ATIVA")
st.write(f"PROPRIEDADE: **SIDNEY ALMEIDA** | STATUS: **SINCRO-ONLINE**")

t1, t2, t3 = st.tabs(["📊 VISÃO GERAL", "🔍 FILTRO OPERADOR", "📥 RELATÓRIO MENSAL"])

with t1:
    st.subheader("Tabela da Favelinha - Tempo Real")
    st.dataframe(st.session_state.historico, use_container_width=True)

with t2:
    st.subheader("Auditoria por Nome")
    sel_op = st.selectbox("ESCOLHA O ALVO:", ["ANA", "MARCOS", "RICARDO", "JULIA"])
    st.table(st.session_state.historico[st.session_state.historico["OPERADOR"] == sel_op])

with t3:
    st.subheader("Exportação de Dados")
    st.write("Histórico completo do mês:")
    st.dataframe(st.session_state.historico)
    
    # BOTÃO DE RELATÓRIO (Correção para celular)
    csv_data = st.session_state.historico.to_csv(index=False).encode('utf-8-sig')
    st.download_button(
        label="📥 GERAR RELATÓRIO (EXCEL/CSV)",
        data=csv_data,
        file_name=f"Relatorio_SPA_{datetime.now().strftime('%m_%Y')}.csv",
        mime="text/csv"
)
    
