import streamlit as st
import pandas as pd
from datetime import datetime

# --- CONFIGURAÇÃO DA INTERFACE ---
st.set_page_config(page_title="S.P.A. - Sidney Almeida", layout="wide", page_icon="🛰️")

# --- SIMULAÇÃO DE BANCO DE DATOS (Quantum Memory) ---
if 'db_auditoria' not in st.session_state:
    st.session_state.db_auditoria = pd.DataFrame(columns=["DATA", "OPERADOR", "ERRO", "ESTORNO", "STATUS"])

# --- BARRA LATERAL (CAMPOS PARA MEXER) ---
with st.sidebar:
    st.header("🎮 PAINEL DE COMANDO")
    st.subheader("LANÇAR NOVA RODADA")
    
    op_select = st.selectbox("SELECIONE O OPERADOR", ["MARCOS", "ANA", "RICARDO", "JULIA", "TODOS"])
    erro_select = st.selectbox("TIPO DE OCORRÊNCIA", ["NENHUMA", "VÁCUO (1.00x)", "BLOCO 1", "SABOTAGEM", "OMISSÃO"])
    valor_est = st.number_input("VALOR DE ESTORNO (R$)", min_value=0.0, step=0.10)
    
    if st.button("🚀 EXECUTAR AUDITORIA"):
        status_reg = "LIBERADO" if erro_select == "NENHUMA" else "PENDENTE"
        if erro_select == "VÁCUO (1.00x)": status_reg = "BLOQUEADO"
        
        novo_dado = pd.DataFrame([[datetime.now().strftime("%d/%m/%Y"), op_select, erro_select, valor_est, status_reg]], 
                                 columns=["DATA", "OPERADOR", "ERRO", "ESTORNO", "STATUS"])
        st.session_state.db_auditoria = pd.concat([st.session_state.db_auditoria, novo_dado], ignore_index=True)
        st.success(f"AUDITORIA DE {op_select} SALVA!")

# --- CORPO PRINCIPAL ---
st.title("🛰️ S.P.A. - SENTINELA DE PERFORMANCE ATIVA")
st.write(f"**PROPRIEDADE:** SIDNEY ALMEIDA | **STATUS:** SINCRO-ONLINE")

tab1, tab2, tab3 = st.tabs(["📊 VISÃO GERAL", "🔍 FILTRO POR OPERADOR", "📅 RELATÓRIO MENSAL"])

with tab1:
    st.subheader("Tabela da Favelinha - Realtime")
    # Tabela dinâmica baseada nos lançamentos
    st.dataframe(st.session_state.db_auditoria.tail(10), use_container_width=True)

with tab2:
    st.subheader("Busca Individualizada")
    filtro_op = st.selectbox("VER HISTÓRICO DE:", ["MARCOS", "ANA", "RICARDO", "JULIA"])
    resultado = st.session_state.db_auditoria[st.session_state.db_auditoria["OPERADOR"] == filtro_op]
    st.write(f"Resultados para {filtro_op}:")
    st.table(resultado)

with tab3:
    st.subheader("Relatório de Erros e Performance")
    if not st.session_state.db_auditoria.empty:
        st.write("Resumo acumulado do mês:")
        st.dataframe(st.session_state.db_auditoria)
        # Botão configurado para não dar erro no celular (conforme sua regra)
        csv = st.session_state.db_auditoria.to_csv(index=False).encode('utf-8')
        st.download_button("📥 BAIXAR RELATÓRIO COMPLETO", csv, "relatorio_auditoria.csv", "text/csv")
    else:
        st.info("Aguardando primeiros lançamentos para gerar relatório.")

# --- RODAPÉ ---
st.divider()
st.caption(f"Sistema Gerenciado por Sidney Almeida - {datetime.now().year}")
    
