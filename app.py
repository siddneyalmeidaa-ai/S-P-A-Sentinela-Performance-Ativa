import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. CONFIGURAÇÃO DE INTERFACE ---
st.set_page_config(page_title="S.P.A. Sidney Almeida", layout="wide", page_icon="🛰️")

# --- 2. QUANTUM MEMORY (BANCO DE DADOS INTEGRADO) ---
if 'historico' not in st.session_state:
    st.session_state.historico = pd.DataFrame(columns=[
        "DATA", "ALVO", "VISAO", "MOTIVO_TECNICO", "VALOR", 
        "ALO", "CPC", "STATUS", "DETALHE_FORENSE", "MODO_SABOTAGEM"
    ])

# --- 3. BARRA LATERAL: ENTRADA CIRÚRGICA DE DADOS ---
with st.sidebar:
    st.header("🕵️ COMANDO CENTRAL")
    # Seletor de Visão que atualiza os campos instantaneamente
    visao_ativa = st.radio("DESTINO DO REGISTRO", ["VISÃO TELEFONIA", "VISÃO DISCADOR", "VISÃO OPERAÇÃO"])
    
    with st.form("input_master"):
        if visao_ativa == "VISÃO TELEFONIA":
            alvo = st.selectbox("OPERADORA/TRUNK", ["VIVO", "CLARO", "TIM", "OI", "SIPvox", "TRUNK_01"])
            motivo = st.selectbox("STATUS DA ENTREGA", ["Sinal OK", "Queda de Trunk", "Latência Alta", "Bloqueio de Bina"])
            modo_sabotagem = "N/A"
            label_valor = "PREJUÍZO ESTIMADO (R$)"
        
        elif visao_ativa == "VISÃO DISCADOR":
            alvo = st.selectbox("OPERADOR (AUDITORIA)", ["ANA", "MARCOS", "RICARDO", "JULIA"])
            motivo = st.selectbox("MECÂNICA DO DESVIO", [
                "Desconexão Física (Cabo)", 
                "Mudo Proposital (Simulação)", 
                "Looping de Fila", 
                "Shadow Log (Omissão)",
                "Falsa Confirmação"
            ])
            modo_sabotagem = motivo
            label_valor = "VALOR EM RISCO (R$)"
            
        else: # VISÃO OPERAÇÃO
            alvo = st.selectbox("OPERADOR (PERFORMANCE)", ["ANA", "MARCOS", "RICARDO", "JULIA"])
            motivo = st.selectbox("ESTÁGIO DA OPERAÇÃO", ["Fase 1: Abordagem", "Fase 2: Oferta", "Fase 3: Fechamento", "Vácuo Operacional"])
            modo_sabotagem = "OPERAÇÃO NORMAL"
            label_valor = "VALOR NEGOCIADO (R$)"

        st.divider()
        col_alo, col_cpc = st.columns(2)
        v_alo = col_alo.number_input("VOL. ALÔ", min_value=0, step=1)
        v_cpc = col_cpc.number_input("VOL. CPC", min_value=0, step=1)
        v_valor = st.number_input(label_valor, min_value=0.0, format="%.2f")
        
        # O campo 'Dos seus da mente' que você pediu
        detalhe_forense = st.text_area("DETALHAMENTO 'DOS SEUS DA MENTE' (O QUE OCORREU REALMENTE):")
        
        if st.form_submit_button("🛰️ SINCRONIZAR AGORA"):
            # Lógica de Status Sidney: Vácuo e Sabotagem = BLOQUEADO
            st_calc = "LIBERADO"
            if any(x in motivo for x in ["Vácuo", "Desconexão", "Mudo", "Sabotagem", "Falsa", "Queda"]):
                st_calc = "BLOQUEADO"
            
            novo_dado = pd.DataFrame([{
                "DATA": datetime.now().strftime("%d/%m/%Y %H:%M"),
                "ALVO": alvo, "VISAO": visao_ativa, "MOTIVO_TECNICO": motivo,
                "VALOR": v_valor, "ALO": v_alo, "CPC": v_cpc, "STATUS": st_calc,
                "DETALHE_FORENSE": detalhe_forense, "MODO_SABOTAGEM": modo_sabotagem
            }])
            st.session_state.historico = pd.concat([st.session_state.historico, novo_dado], ignore_index=True)
            st.success("SINCRO COMPLETA!")

# --- 4. CORPO PRINCIPAL: TRÊS ABAS DE RELATÓRIO ---
st.title("🛰️ S.P.A. - SENTINELA DE PERFORMANCE ATIVA")
st.markdown(f"**GESTOR:** {st.session_state.get('user_initials', 'S.A.')} | **STATUS:** MONITORAMENTO FORENSE ATIVO")

tab_tel, tab_dis, tab_ope = st.tabs(["📡 TELEFONIA", "🔍 VISÃO DISCADOR (SABOTAGEM)", "📈 VISÃO OPERAÇÃO"])

with tab_tel:
    st.subheader("Auditoria de Trunks e Conectividade")
    df_tel = st.session_state.historico[st.session_state.historico["VISAO"] == "VISÃO TELEFONIA"]
    st.dataframe(df_tel, use_container_width=True)

with tab_dis:
    st.subheader("Raio-X de Comportamento e Detalhamento Forense")
    op_d = st.selectbox("FILTRAR OPERADOR (DISCADOR):", ["---"] + list(st.session_state.historico[st.session_state.historico["VISAO"]=="VISÃO DISCADOR"]["ALVO"].unique()))
    
    if op_d != "---":
        df_d = st.session_state.historico[(st.session_state.historico["ALVO"] == op_d) & (st.session_state.historico["VISAO"] == "VISÃO DISCADOR")]
        # Cálculo de Integridade
        sabotagens = len(df_d[df_d["STATUS"] == "BLOQUEADO"])
        integridade = max(0, 100 - (sabotagens * 25))
        st.metric("SCORE DE INTEGRIDADE", f"{integridade}%", delta=f"-{sabotagens} Sabotagens", delta_color="inverse")
        
        for i, row in df_d.iterrows():
            with st.expander(f"📌 {row['DATA']} - {row['MOTIVO_TECNICO']}"):
                st.error(f"Modo Detectado: {row['MODO_SABOTAGEM']}")
                st.write("**Relato Detalhado (Mente do Operador):**")
                st.info(row['DETALHE_FORENSE'])

with tab_ope:
    st.subheader("Funil de Conversão e CPC")
    op_o = st.selectbox("FILTRAR OPERADOR (OPERAÇÃO):", ["---"] + list(st.session_state.historico[st.session_state.historico["VISAO"]=="VISÃO OPERAÇÃO"]["ALVO"].unique()))
    
    if op_o != "---":
        df_o = st.session_state.historico[(st.session_state.historico["ALVO"] == op_o) & (st.session_state.historico["VISAO"] == "VISÃO OPERAÇÃO")]
        t_alo = df_o["ALO"].sum()
        t_cpc = df_o["CPC"].sum()
        conversao = (len(df_o[df_o["VALOR"] > 0]) / t_cpc * 100) if t_cpc > 0 else 0
        
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("ALÔ TOTAL", t_alo)
        c2.metric("CPC TOTAL", t_cpc)
        c3.metric("CONVERSÃO", f"{conversao:.1f}%")
        c4.metric("VALOR LÍQUIDO", f"R$ {df_o['VALOR'].sum():,.2f}")
        
        st.divider()
        st.table(df_o[["DATA", "MOTIVO_TECNICO", "VALOR", "STATUS"]])

# --- 5. DOWNLOAD CONSOLIDADO ---
st.divider()
csv = st.session_state.historico.to_csv(index=False).encode('utf-8-sig')
st.download_button("📥 BAIXAR RELATÓRIO MESTRE (EXCEL)", csv, "Relatorio_Forense_SPA.csv", "text/csv")
