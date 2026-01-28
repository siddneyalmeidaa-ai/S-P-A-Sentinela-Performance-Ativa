import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. CONFIGURAÇÃO ---
st.set_page_config(page_title="S.P.A. - Sidney Almeida", layout="wide", page_icon="🛰️")

# --- 2. QUANTUM MEMORY ---
if 'historico' not in st.session_state:
    st.session_state.historico = pd.DataFrame(columns=[
        "DATA", "ALVO", "VISAO", "MOTIVO", "VALOR", "STATUS", "LOG_TECNICO"
    ])

# --- 3. BARRA LATERAL (CORREÇÃO DE SINCRONISMO) ---
with st.sidebar:
    st.header("🎮 LANÇAMENTO CENTRAL")
    # O segredo está em não usar o 'form' para a seleção da visão, para que ele atualize na hora
    visao_selecionada = st.radio("DESTINO DO REGISTRO", ["VISÃO TELEFONIA", "VISÃO DISCADOR", "VISÃO OPERAÇÃO"])
    
    with st.form("executar_registro"):
        # MUDANÇA DINÂMICA DE CAMPOS CONFORME A VISÃO
        if visao_selecionada == "VISÃO TELEFONIA":
            alvo = st.selectbox("EMPRESA DE TELEFONIA", ["VIVO", "CLARO", "TIM", "OI", "SIPvox", "TRUNK_01"])
            motivo = st.selectbox("MOTIVO TÉCNICO", ["Entrega OK", "Queda de Sinal", "Congestionamento", "Fila Presa", "Bloqueio de Bina"])
            label_valor = "IMPACTO FINANCEIRO (R$)"
        
        elif visao_selecionada == "VISÃO DISCADOR":
            alvo = st.selectbox("OPERADOR (LOGS)", ["ANA", "MARCOS", "RICARDO", "JULIA"])
            motivo = st.selectbox("MOTIVO NO DISCADOR", ["Sabotagem de Dialer", "Desligamento Proposital", "Falsa Promessa", "Omissão de Histórico"])
            label_valor = "VALOR ESTIMADO (R$)"
            
        else: # VISÃO OPERAÇÃO
            alvo = st.selectbox("OPERADOR (PERFORMANCE)", ["ANA", "MARCOS", "RICARDO", "JULIA"])
            motivo = st.selectbox("MOTIVO OPERACIONAL", ["Cumprimento Bloco 1", "Cumprimento Bloco 2", "Vácuo (1.00x)", "Estorno Real"])
            label_valor = "VALOR NEGOCIADO (R$)"
            
        valor_input = st.number_input(label_valor, min_value=0.0, format="%.2f")
        detalhes = st.text_area("DETALHES DO SERVIDOR / LOGS")
        
        btn_enviar = st.form_submit_button("🚀 SINCRONIZAR")
        
        if btn_enviar:
            # Regra de Status Sidney
            st_calc = "LIBERADO"
            if any(x in motivo for x in ["Vácuo", "Sabotagem", "Queda", "Falsa"]): st_calc = "BLOQUEADO"
            
            novo_log = pd.DataFrame([{
                "DATA": datetime.now().strftime("%d/%m/%Y"),
                "ALVO": alvo, "VISAO": visao_selecionada, "MOTIVO": motivo,
                "VALOR": valor_input, "STATUS": st_calc, "LOG_TECNICO": detalhes
            }])
            st.session_state.historico = pd.concat([st.session_state.historico, novo_log], ignore_index=True)
            st.success(f"REGISTRO EM {visao_selecionada} REALIZADO!")

# --- 4. RELATÓRIOS EM ABAS ---
st.title("🛰️ S.P.A. - SENTINELA DE PERFORMANCE ATIVA")
st.write(f"PROPRIEDADE: **SIDNEY ALMEIDA** | **SINCRO-ONLINE**")

t_tel, t_dis, t_ope = st.tabs(["📡 TELEFONIA", "🔍 DISCADOR", "📈 OPERAÇÃO"])

with t_tel:
    st.subheader("Relatório de Empresas de Telefonia")
    df_t = st.session_state.historico[st.session_state.historico["VISAO"] == "VISÃO TELEFONIA"]
    st.dataframe(df_t, use_container_width=True)

with t_dis:
    st.subheader("Relatório de Logs do Discador")
    df_d = st.session_state.historico[st.session_state.historico["VISAO"] == "VISÃO DISCADOR"]
    st.dataframe(df_d, use_container_width=True)

with t_ope:
    st.subheader("Relatório de Performance Operacional")
    df_o = st.session_state.historico[st.session_state.historico["VISAO"] == "VISÃO OPERAÇÃO"]
    st.dataframe(df_o, use_container_width=True)
    if not df_o.empty:
        st.metric("TOTAL PRODUZIDO", f"R$ {df_o['VALOR'].sum():,.2f}")

# BOTÃO DE DOWNLOAD SEM ERRO DE ACENTO
csv = st.session_state.historico.to_csv(index=False).encode('utf-8-sig')
st.download_button("📥 BAIXAR RELATÓRIO MENSAL", csv, "Relatorio_SPA.csv", "text/csv")
            
