import streamlit as st
import pandas as pd
from datetime import datetime

# --- CONFIGURAÇÃO ---
st.set_page_config(page_title="S.P.A. - Sidney Almeida", layout="wide", page_icon="🛰️")

# --- QUANTUM MEMORY ---
if 'historico' not in st.session_state:
    st.session_state.historico = pd.DataFrame(columns=[
        "DATA", "ALVO", "VISAO", "MOTIVO", "VALOR", "STATUS", "LOG_TECNICO"
    ])

# --- BARRA LATERAL: COMANDO S.P.A. ---
with st.sidebar:
    st.header("🎮 LANÇAMENTO CENTRAL")
    with st.form("form_sincro"):
        visao = st.radio("DESTINO DO REGISTRO", ["VISÃO TELEFONIA", "VISÃO DISCADOR", "VISÃO OPERAÇÃO"])
        
        # Lógica de seleção baseada na visão
        if visao == "VISÃO TELEFONIA":
            alvo = st.selectbox("OPERADORA/EMPRESA", ["VIVO", "CLARO", "TIM", "OI", "SIPvox", "TRUNK_IP"])
            motivo = st.selectbox("MOTIVO TÉCNICO", ["Entrega OK", "Queda de Sinal", "Congestionamento", "Fila Presa", "Bloqueio de Bina"])
        elif visao == "VISÃO DISCADOR":
            alvo = st.selectbox("OPERADOR", ["ANA", "MARCOS", "RICARDO", "JULIA"])
            motivo = st.selectbox("MOTIVO LOGS", ["Sabotagem de Dialer", "Desligamento Proposital", "Falsa Promessa", "Omissão de Histórico"])
        else:
            alvo = st.selectbox("OPERADOR ", ["ANA", "MARCOS", "RICARDO", "JULIA"])
            motivo = st.selectbox("MOTIVO PERFORMANCE", ["Bloco 1", "Bloco 2", "Vácuo (1.00x)", "Estorno Real"])
            
        valor = st.number_input("VALOR DE IMPACTO (R$)", min_value=0.0, format="%.2f")
        logs = st.text_area("DETALHES DO SERVIDOR")
        
        if st.form_submit_button("🚀 SINCRONIZAR"):
            # Regra Sidney: Vácuo e Sabotagem bloqueiam na hora
            st_calc = "LIBERADO"
            if any(x in motivo for x in ["Vácuo", "Sabotagem", "Queda", "Falsa"]): st_calc = "BLOQUEADO"
            
            novo = pd.DataFrame([{
                "DATA": datetime.now().strftime("%d/%m/%Y"),
                "ALVO": alvo, "VISAO": visao, "MOTIVO": motivo,
                "VALOR": valor, "STATUS": st_calc, "LOG_TECNICO": logs
            }])
            st.session_state.historico = pd.concat([st.session_state.historico, novo], ignore_index=True)
            st.success("SINCRO COMPLETA!")

# --- CORPO PRINCIPAL: AS 3 ABAS DE RELATÓRIO ---
st.title("🛰️ S.P.A. - SENTINELA DE PERFORMANCE ATIVA")
st.write(f"PROPRIEDADE: **SIDNEY ALMEIDA** | STATUS: **SINCRO-ONLINE**")

tab_tel, tab_disc, tab_oper = st.tabs(["📡 RELATÓRIO TELEFONIA", "🔍 RELATÓRIO DISCADOR", "📈 RELATÓRIO OPERAÇÃO"])

with tab_tel:
    st.subheader("Auditoria de Operadoras e Trunks")
    df_tel = st.session_state.historico[st.session_state.historico["VISAO"] == "VISÃO TELEFONIA"]
    st.dataframe(df_tel, use_container_width=True)
    if not df_tel.empty:
        st.metric("PERDA POR INSTABILIDADE", f"R$ {df_tel['VALOR'].sum():,.2f}")

with tab_disc:
    st.subheader("Auditoria de Comportamento e Logs")
    df_disc = st.session_state.historico[st.session_state.historico["VISAO"] == "VISÃO DISCADOR"]
    # Busca automática dentro da aba
    op_busca = st.selectbox("FILTRAR OPERADOR NO DISCADOR:", ["TODOS"] + list(df_disc["ALVO"].unique()))
    if op_busca != "TODOS":
        df_disc = df_disc[df_disc["ALVO"] == op_busca]
    st.table(df_disc[["DATA", "ALVO", "MOTIVO", "STATUS", "LOG_TECNICO"]])

with tab_oper:
    st.subheader("Auditoria de Performance e Blocos")
    df_oper = st.session_state.historico[st.session_state.historico["VISAO"] == "VISÃO OPERAÇÃO"]
    # Busca automática dentro da aba
    op_oper = st.selectbox("FILTRAR OPERADOR NA OPERAÇÃO:", ["TODOS"] + list(df_oper["ALVO"].unique()))
    if op_oper != "TODOS":
        df_oper = df_oper[df_oper["ALVO"] == op_oper]
    st.dataframe(df_oper, use_container_width=True)
    st.metric("RECUPERAÇÃO LÍQUIDA", f"R$ {df_oper['VALOR'].sum():,.2f}")

# --- BOTÃO DE DOWNLOAD GLOBAL ---
st.divider()
csv = st.session_state.historico.to_csv(index=False).encode('utf-8-sig')
st.download_button("📥 BAIXAR RELATÓRIO CONSOLIDADO (EXCEL)", csv, "relatorio_geral_spa.csv", "text/csv")
