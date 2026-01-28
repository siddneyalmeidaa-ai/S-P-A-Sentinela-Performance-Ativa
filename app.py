import streamlit as st
import pandas as pd
from datetime import datetime
from io import BytesIO

# --- 1. CONFIGURAÇÃO E IDENTIDADE ---
st.set_page_config(page_title="S.P.A. Sidney Almeida", layout="wide", page_icon="🛰️")

# --- 2. BANCO DE DADOS INTEGRADO (ACUMULATIVO) ---
if 'historico' not in st.session_state:
    st.session_state.historico = pd.DataFrame(columns=[
        "DATA", "ALVO", "VISAO", "MOTIVO", "VALOR", "ALO", "CPC", 
        "STATUS", "FORENSE", "PENETRACAO", "TICKET_MEDIO", "AUTONOMIA_DIAS",
        "NOTIFICACAO", "STATUS_MEIO"
    ])

# --- 3. BARRA LATERAL: COMANDO DE ELITE ---
with st.sidebar:
    st.header("🕵️ COMANDO CENTRAL")
    visao_ativa = st.radio("SISTEMA", ["VISÃO OPERAÇÃO (FUSÃO)", "VISÃO DISCADOR (CAPACITY/MALHA)"])
    
    with st.form("master_form"):
        st.subheader("⚙️ Input de Dados")
        alvo = st.selectbox("ALVO/CARTEIRA", ["ANA", "MARCOS", "RICARDO", "CARTEIRA VIVO", "RETAIL"])
        
        if visao_ativa == "VISÃO OPERAÇÃO (FUSÃO)":
            f_motivo = st.selectbox("CONDUTA", ["Fase 3: Fechamento", "Vácuo", "Desconexão Cabo", "Mudo Proposital", "Fase 2: Oferta"])
            f_valor = st.number_input("VALOR RECUPERADO (R$)", 0.0)
            f_forense = st.text_area("DETALHE FORENSE (MENTE)")
            # Reset de campos de malha
            f_ticket, f_pen, f_auto, f_meio = 0, 0, 0, "N/A"
            
        else: # VISÃO DISCADOR (CAPACITY/MALHA)
            f_motivo = "AUDITORIA DE MALHA"
            f_ticket = st.number_input("TICKET MÉDIO (R$)", value=150.00)
            f_pen = st.slider("TAXA DE PENETRAÇÃO (%)", 0, 100, 40)
            f_leads = st.number_input("TOTAL DE LEADS NA BASE", value=50000)
            f_ops = st.number_input("OPERADORES ATIVOS", value=20)
            # Cálculo de Autonomia (Base / (Ops * 400 ligações/dia))
            f_auto = round(f_leads / (f_ops * 400), 2) if f_ops > 0 else 0
            f_meio = st.selectbox("QUALIDADE DO MEIO", ["HIGIENIZADO", "PRECISA ENRIQUECER", "MUITO DESCONHECIDO", "BASE ESGOTADA"])
            f_forense = st.text_area("ANÁLISE DE MELHORIA DO MEIO")
            f_valor = 0.0

        if st.form_submit_button("🚀 SINCRONIZAR E NOTIFICAR"):
            # Lógica de Notificações Automáticas
            alerta = "Sinal Estável"
            if visao_ativa == "VISÃO DISCADOR (CAPACITY/MALHA)":
                if f_pen < 30: alerta = "🚨 BAIXA PENETRAÇÃO"
                elif f_auto < 1: alerta = "⚠️ MAILING ESGOTANDO"
                elif "ENRIQUECER" in f_meio: alerta = "🔍 REQUER ENRIQUECIMENTO"
            elif "Cabo" in f_motivo or "Mudo" in f_motivo:
                alerta = "🚩 ALERTA DE SABOTAGEM"

            novo = pd.DataFrame([{
                "DATA": datetime.now().strftime("%d/%m/%Y %H:%M"), "ALVO": alvo, "VISAO": visao_ativa,
                "MOTIVO": f_motivo, "VALOR": f_valor, "STATUS": "BLOQUEADO" if "ALERTA" in alerta else "LIBERADO",
                "FORENSE": f_forense, "PENETRACAO": f"{f_pen}%", "TICKET_MEDIO": f_ticket,
                "AUTONOMIA_DIAS": f_auto, "NOTIFICACAO": alerta, "STATUS_MEIO": f_meio
            }])
            st.session_state.historico = pd.concat([st.session_state.historico, novo], ignore_index=True)

# --- 4. PAINEL PRINCIPAL ---
st.title("🛰️ S.P.A. - SENTINELA DE PERFORMANCE ATIVA")

# --- CENTRAL DE NOTIFICAÇÕES (DASHBOARD) ---
st.subheader("🔔 Central de Notificações em Tempo Real")
notificacoes = st.session_state.historico[st.session_state.historico["NOTIFICACAO"] != "Sinal Estável"].tail(3)
if not notificacoes.empty:
    for _, n in notificacoes.iterrows():
        st.toast(f"{n['NOTIFICACAO']}: {n['ALVO']}", icon="⚠️")
        if "SABOTAGEM" in n['NOTIFICACAO']: st.error(f"**{n['DATA']} - {n['NOTIFICACAO']}**: O alvo {n['ALVO']} apresentou conduta suspeita.")
        else: st.warning(f"**{n['DATA']} - {n['NOTIFICACAO']}**: {n['ALVO']} requer atenção na malha.")

t_ope, t_disc = st.tabs(["📈 OPERAÇÃO (FUSÃO TOTAL)", "🧠 DISCADOR (CAPACITY & MALHA)"])

with t_ope:
    df_o = st.session_state.historico[st.session_state.historico["VISAO"] == "VISÃO OPERAÇÃO (FUSÃO)"]
    c1, c2, c3 = st.columns(3)
    c1.metric("RECUPERADO", f"R$ {df_o['VALOR'].sum():,.2f}")
    c2.metric("SABOTAGENS", len(df_o[df_o["STATUS"] == "BLOQUEADO"]))
    c3.metric("ALERTAS", len(notificacoes))
    st.table(df_o[["DATA", "ALVO", "MOTIVO", "VALOR", "STATUS", "FORENSE"]])

with t_disc:
    st.subheader("Planejamento de Carga e Qualidade de Dados")
    df_d = st.session_state.historico[st.session_state.historico["VISAO"] == "VISÃO DISCADOR (CAPACITY/MALHA)"]
    if not df_d.empty:
        last = df_d.iloc[-1]
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("TICKET MÉDIO", f"R$ {last['TICKET_MEDIO']}")
        m2.metric("AUTONOMIA", f"{last['AUTONOMIA_DIAS']} Dias")
        m3.metric("PENETRAÇÃO", last['PENETRACAO'])
        m4.metric("MEIO", last['STATUS_MEIO'])
        st.dataframe(df_d[["DATA", "ALVO", "TICKET_MEDIO", "AUTONOMIA_DIAS", "PENETRACAO", "STATUS_MEIO", "FORENSE"]], use_container_width=True)

# --- 5. EXPORTAÇÃO ---
st.divider()
st.download_button("📊 EXPORTAR RELATÓRIO COMPLETO", st.session_state.historico.to_csv(index=False).encode('utf-8-sig'), "SPA_Final.csv")
            
