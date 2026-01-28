import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. CONFIGURAÇÃO DE INTERFACE ---
st.set_page_config(page_title="S.P.A. Sidney Almeida", layout="wide", page_icon="🛰️")

# --- 2. QUANTUM MEMORY (LIMPA PARA PRODUÇÃO) ---
if 'historico' not in st.session_state:
    st.session_state.historico = pd.DataFrame(columns=[
        "DATA", "ALVO", "VISAO", "MOTIVO_TECNICO", "VALOR", 
        "ALO", "CPC", "STATUS", "DETALHE_FORENSE", "MODO_SABOTAGEM"
    ])

# --- 3. BARRA LATERAL: COMANDO DE ALIMENTAÇÃO ---
with st.sidebar:
    st.header("🕵️ COMANDO CENTRAL")
    visao_ativa = st.radio("DESTINO DO REGISTRO", ["VISÃO TELEFONIA", "VISÃO DISCADOR", "VISÃO OPERAÇÃO"])
    
    with st.form("input_master"):
        # DINAMISMO POR TERMINOLOGIA DE ABA
        if visao_ativa == "VISÃO TELEFONIA":
            alvo = st.selectbox("OPERADORA/TRUNK", ["VIVO", "CLARO", "TIM", "OI", "SIPvox", "TRUNK_IP"])
            motivo = st.selectbox("STATUS DA CONECTIVIDADE", ["Sinal OK", "Queda de Trunk", "Latência Alta", "Saturado"])
            label_valor = "PREJUÍZO TÉCNICO (R$)"
            label_detalhe = "DETALHAMENTO DA QUEDA (MENTE DO SISTEMA):"
        
        elif visao_ativa == "VISÃO DISCADOR":
            alvo = st.selectbox("OPERADOR (AUDITORIA)", ["ANA", "MARCOS", "RICARDO", "JULIA"])
            motivo = st.selectbox("COMPORTAMENTO DISCADOR", ["Desconexão Cabo", "Mudo Proposital", "Shadow Log", "Falsa Confirmação"])
            label_valor = "VALOR EM RISCO (R$)"
            label_detalhe = "DETALHAMENTO DA SABOTAGEM (MENTE DO OPERADOR):"
            
        else: # VISÃO OPERAÇÃO
            alvo = st.selectbox("OPERADOR (PRODUÇÃO)", ["ANA", "MARCOS", "RICARDO", "JULIA"])
            motivo = st.selectbox("ESTÁGIO OPERACIONAL", ["Fase 1: Abordagem", "Fase 2: Oferta", "Fase 3: Fechamento", "Vácuo"])
            label_valor = "VALOR NEGOCIADO (R$)"
            label_detalhe = "DETALHAMENTO DA CONVERSA (MENTE DA NEGOCIAÇÃO):"

        st.divider()
        col_alo, col_cpc = st.columns(2)
        v_alo = col_alo.number_input("VOL. ALÔ (ATENDIDAS)", min_value=0, step=1)
        v_cpc = col_cpc.number_input("VOL. CPC (CONTATO REAL)", min_value=0, step=1)
        v_valor = st.number_input(label_valor, min_value=0.0, format="%.2f")
        
        # CAMPO FORENSE SEMPRE PRESENTE
        detalhe_forense = st.text_area(label_detalhe)
        
        if st.form_submit_button("🚀 ALIMENTAR SERVIDOR"):
            st_calc = "LIBERADO"
            if any(x in motivo for x in ["Vácuo", "Desconexão", "Mudo", "Queda", "Shadow"]):
                st_calc = "BLOQUEADO"
            
            novo_dado = pd.DataFrame([{
                "DATA": datetime.now().strftime("%d/%m/%Y %H:%M"),
                "ALVO": alvo, "VISAO": visao_ativa, "MOTIVO_TECNICO": motivo,
                "VALOR": v_valor, "ALO": v_alo, "CPC": v_cpc, "STATUS": st_calc,
                "DETALHE_FORENSE": detalhe_forense
            }])
            st.session_state.historico = pd.concat([st.session_state.historico, novo_dado], ignore_index=True)
            st.success(f"REGISTRO EM {visao_ativa} SINCRONIZADO!")

# --- 4. RELATÓRIOS POR ABA (INTERFACES ALIMENTADAS) ---
st.title("🛰️ S.P.A. - SENTINELA DE PERFORMANCE ATIVA")

t_tel, t_dis, t_ope = st.tabs(["📡 RELATÓRIO TELEFONIA", "🔍 RELATÓRIO DISCADOR", "📈 RELATÓRIO OPERAÇÃO"])

with t_tel:
    st.subheader("Auditoria de Trunks e Sinal")
    df_t = st.session_state.historico[st.session_state.historico["VISAO"] == "VISÃO TELEFONIA"]
    st.dataframe(df_t, use_container_width=True)

with t_dis:
    st.subheader("Auditoria de Comportamento e Logs")
    df_d = st.session_state.historico[st.session_state.historico["VISAO"] == "VISÃO DISCADOR"]
    st.dataframe(df_d, use_container_width=True)

with t_ope:
    st.subheader("Métricas de Performance e Funil")
    df_o = st.session_state.historico[st.session_state.historico["VISAO"] == "VISÃO OPERAÇÃO"]
    st.dataframe(df_o, use_container_width=True)
    if not df_o.empty:
        total_rec = df_o["VALOR"].sum()
        st.metric("TOTAL RECUPERADO", f"R$ {total_rec:,.2f}")

# DOWNLOAD
csv = st.session_state.historico.to_csv(index=False).encode('utf-8-sig')
st.download_button("📥 BAIXAR RELATÓRIO MESTRE", csv, "Relatorio_SPA.csv", "text/csv")
