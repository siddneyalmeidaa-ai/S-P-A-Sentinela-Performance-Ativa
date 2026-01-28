import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. CONFIGURAÇÃO DE INTERFACE ---
st.set_page_config(page_title="S.P.A. - Sidney Almeida", layout="wide", page_icon="🛰️")

# --- 2. QUANTUM MEMORY (PERSISTÊNCIA DE DADOS) ---
if 'historico' not in st.session_state:
    st.session_state.historico = pd.DataFrame(columns=[
        "DATA", "OPERADOR", "VISAO", "MOTIVO", "ESTORNO", "STATUS", "LOG_TECNICO", "SCORE"
    ])

# --- 3. BARRA LATERAL: INPUT DE AUDITORIA ---
with st.sidebar:
    st.header("🎮 COMANDO S.P.A.")
    with st.form("input_form"):
        st.subheader("Sincronizar Servidor")
        op = st.selectbox("OPERADOR", ["ANA", "MARCOS", "RICARDO", "JULIA"])
        visao = st.radio("VISÃO", ["VISÃO BUSCADOR", "VISÃO OPERAÇÃO"])
        
        if visao == "VISÃO BUSCADOR":
            motivo = st.selectbox("MOTIVO TÉCNICO", [
                "Sabotagem de Dialer (Fila Presa)",
                "Desligamento Proposital (Servidor)",
                "Falsa Promessa (Sem Confirmação)",
                "Omissão de Histórico Técnico",
                "Manipulação de Projeção"
            ])
            impacto_score = -2  # Penalidade na confiança
        else:
            motivo = st.selectbox("MOTIVO OPERACIONAL", [
                "Cumprimento Bloco 1",
                "Cumprimento Bloco 2",
                "Vácuo de Operação (1.00x)",
                "Exposição de Valor (Omissão)",
                "Estorno Recuperado"
            ])
            impacto_score = 1 if "Cumprimento" in motivo or "Estorno" in motivo else -1
            
        valor = st.number_input("VALOR NEGOCIADO (R$)", min_value=0.0, format="%.2f")
        logs = st.text_area("LOGS DO DISCADOR/SISTEMA")
        
        if st.form_submit_button("🚀 EXECUTAR E BLINDAR"):
            # Lógica de Status Automática
            st_calc = "LIBERADO"
            if "Vácuo" in motivo or "Sabotagem" in motivo: st_calc = "BLOQUEADO"
            elif "Omissão" in motivo or "Falsa" in motivo: st_calc = "PENDENTE"
            
            novo_dado = pd.DataFrame([{
                "DATA": datetime.now().strftime("%d/%m/%Y"),
                "OPERADOR": op, "VISAO": visao, "MOTIVO": motivo,
                "ESTORNO": valor, "STATUS": st_calc, "LOG_TECNICO": logs,
                "SCORE": impacto_score
            }])
            st.session_state.historico = pd.concat([st.session_state.historico, novo_dado], ignore_index=True)
            st.success(f"DADOS SINCRONIZADOS: {op}")

# --- 4. CORPO PRINCIPAL - DASHBOARD ---
st.title("🛰️ S.P.A. - SENTINELA DE PERFORMANCE ATIVA")
st.markdown(f"**GESTOR GERAL:** SIDNEY ALMEIDA | **SINCRO:** ONLINE")

# --- 5. RAIO-X AUTOMATIZADO (DUPLA BUSCA) ---
st.divider()
col1, col2 = st.columns(2)

with col1:
    st.subheader("🔍 VISÃO BUSCADOR")
    st.caption("Filtro: Comportamento e Integridade")
    # Busca inteligente
    op_b = st.selectbox("PESQUISAR NO DISCADOR:", ["---"] + list(st.session_state.historico[st.session_state.historico["VISAO"]=="VISÃO BUSCADOR"]["OPERADOR"].unique()))
    
    if op_b != "---":
        dados_b = st.session_state.historico[(st.session_state.historico["OPERADOR"] == op_b) & (st.session_state.historico["VISAO"] == "VISÃO BUSCADOR")]
        st.error(f"Alertas de Conduta: {len(dados_b)}")
        st.table(dados_b[["MOTIVO", "LOG_TECNICO", "STATUS"]])

with col2:
    st.subheader("📈 VISÃO OPERAÇÃO")
    st.caption("Foco: Produção e Blocos")
    # Busca inteligente
    op_o = st.selectbox("PESQUISAR NA OPERAÇÃO:", ["---"] + list(st.session_state.historico[st.session_state.historico["VISAO"]=="VISÃO OPERAÇÃO"]["OPERADOR"].unique()))
    
    if op_o != "---":
        dados_o = st.session_state.historico[(st.session_state.historico["OPERADOR"] == op_o) & (st.session_state.historico["VISAO"] == "VISÃO OPERAÇÃO")]
        # Cálculo de Índice de Confiabilidade (Score base 10)
        score_total = max(0, min(10, 5 + st.session_state.historico[st.session_state.historico["OPERADOR"] == op_o]["SCORE"].sum()))
        
        st.metric("TOTAL EM NEGOCIAÇÃO", f"R$ {dados_o['ESTORNO'].sum():,.2f}")
        st.metric("ÍNDICE DE CONFIABILIDADE", f"{score_total}/10")
        st.table(dados_o[["MOTIVO", "ESTORNO", "STATUS"]])

# --- 6. TABELA DA FAVELINHA E RELATÓRIO ---
st.divider()
st.subheader("📋 TABELA DA FAVELINHA - CONSOLIDADO")
st.dataframe(st.session_state.historico, use_container_width=True)

# BOTÃO DE DOWNLOAD (UTF-8-SIG para Excel celular)
csv = st.session_state.historico.to_csv(index=False).encode('utf-8-sig')
st.download_button("📥 GERAR RELATÓRIO MENSAL (EXCEL)", csv, f"Relatorio_SPA_{datetime.now().strftime('%d_%m')}.csv", "text/csv")
