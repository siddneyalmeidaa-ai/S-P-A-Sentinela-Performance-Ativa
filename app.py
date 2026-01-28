import streamlit as st
import pandas as pd
from datetime import datetime
from io import BytesIO

# --- 1. CONFIGURAÇÃO E IDENTIDADE ---
st.set_page_config(page_title="S.P.A. Sidney Almeida", layout="wide", page_icon="🛰️")

# --- 2. QUANTUM MEMORY: BANCO DE DADOS REALÍSTICO (ACUMULATIVO) ---
if 'db_ficticio' not in st.session_state:
    st.session_state.db_ficticio = {
        # OPERADORES (Pessoas para Visão Operação)
        "ANA": {"ALO": 450, "CPC": 180, "VALOR": 12500.50, "STATUS": "LIBERADO", "TABULACAO": "Promessa de Pagamento", "FORENSE": "Alta performance. Scripts de urgência aplicados.", "LEGAL": "Regimento Interno"},
        "MARCOS": {"ALO": 890, "CPC": 12, "VALOR": 0.00, "STATUS": "BLOQUEADO", "TABULACAO": "Queda de Sistema (Falsa)", "FORENSE": "42 quedas de hardware detectadas. Sabotagem física.", "LEGAL": "Art. 482 CLT"},
        "RICARDO": {"ALO": 320, "CPC": 290, "VALOR": 150.00, "STATUS": "BLOQUEADO", "TABULACAO": "Chamada Muda", "FORENSE": "Operador atende e silencia microfone.", "LEGAL": "Insubordinação"},
        "JULIA": {"ALO": 510, "CPC": 150, "VALOR": 4200.00, "STATUS": "LIBERADO", "TABULACAO": "Negociação em Curso", "FORENSE": "Volume constante, sem alertas.", "LEGAL": "Regimento Interno"},
        # CARTEIRAS (Mailing para Visão Discador)
        "VIVO MÓVEL": {"LEADS": 50000, "PENETRACAO": 45, "STATUS_MEIO": "PRECISA RECARGA", "TICKET": 145.00},
        "RETAIL": {"LEADS": 120000, "PENETRACAO": 15, "STATUS_MEIO": "MAILING ESGOTADO", "TICKET": 320.00},
        "VIVO (TRUNK)": {"ALO": 5000, "CPC": 800, "VALOR": 3500.00, "STATUS": "BLOQUEADO", "MOTIVO": "Queda Trunk IP", "FORENSE": "Falha massiva no Gateway SIP.", "LEGAL": "SLA Técnica"}
    }

if 'historico' not in st.session_state:
    st.session_state.historico = pd.DataFrame(columns=[
        "DATA", "ALVO", "VISAO", "TABULACAO", "VALOR", "ALO", "CPC", 
        "STATUS", "FORENSE", "LEGAL", "PENETRACAO", "TICKET_MEDIO", 
        "AUTONOMIA_DIAS", "NOTIFICACAO", "STATUS_MEIO"
    ])

# --- 3. BARRA LATERAL: COMANDO DINÂMICO ---
with st.sidebar:
    st.header("🕵️ COMANDO CENTRAL")
    visao_ativa = st.radio("DESTINO DO REGISTRO", ["VISÃO OPERAÇÃO (OPERADORES)", "VISÃO DISCADOR (MAILING/STRAT)", "VISÃO TELEFONIA", "VISÃO JURÍDICA"])
    
    st.divider()
    
    # CORREÇÃO DO FILTRO SOLICITADA: Separação por categoria
    if visao_ativa == "VISÃO OPERAÇÃO (OPERADORES)":
        lista_alvos = ["ANA", "MARCOS", "RICARDO", "JULIA"]
        label_selecao = "OPERADOR EM LOGON:"
    elif visao_ativa == "VISÃO DISCADOR (MAILING/STRAT)":
        lista_alvos = ["VIVO MÓVEL", "RETAIL", "CARTEIRA JURÍDICO"]
        label_selecao = "CARTEIRA DE MAILING:"
    else:
        lista_alvos = ["VIVO (TRUNK)", "CLARO (TRUNK)", "SIPvox"]
        label_selecao = "CANAL DE TELEFONIA:"
        
    alvo_ref = st.selectbox(label_selecao, lista_alvos)
    default = st.session_state.db_ficticio.get(alvo_ref, {"ALO":0, "CPC":0, "VALOR":0.0, "STATUS":"Pendente", "TABULACAO":"N/A", "FORENSE":"", "LEGAL":"N/A", "LEADS":0, "PENETRACAO":0})

    with st.form("master_sync"):
        st.subheader("⚙️ Input Real da Operação")
        
        if visao_ativa == "VISÃO OPERAÇÃO (OPERADORES)":
            f_tab = st.selectbox("TABULAÇÃO/STATUS", ["Promessa de Pagamento", "Vácuo (Omissão)", "Cabo Desconectado", "Mudo Proposital", "Pausa Indevida"])
            f_val = st.number_input("VALOR RECUPERADO (R$)", value=default["VALOR"])
            f_for = st.text_area("ANÁLISE DE CONDUTA (FORENSE)", value=default["FORENSE"])
            f_pen, f_auto, f_meio, f_ticket = 0, 0, "N/A", 0
            
        elif visao_ativa == "VISÃO DISCADOR (MAILING/STRAT)":
            f_tab = "AUDITORIA DE ESTRATÉGIA"
            f_ticket = st.number_input("TICKET MÉDIO DA BASE", value=default.get("TICKET", 180.00))
            f_pen = st.slider("TAXA DE PENETRAÇÃO (%)", 0, 100, default.get("PENETRACAO", 40))
            f_leads = st.number_input("TOTAL DE LEADS ATIVOS", value=default.get("LEADS", 50000))
            f_ops = st.number_input("OPERADORES EM LOGON", value=20)
            # Cálculo de Capacity
            f_auto = round(f_leads / (f_ops * 400), 2) if f_ops > 0 else 0
            f_meio = st.selectbox("STATUS DA RECICLAGEM", ["MAILING QUENTE", "NECESSITA HIGIENIZAÇÃO", "BASE ESGOTADA"])
            f_for = st.text_area("MELHORIA DO MEIO", value="Análise de malha.")
            f_val = 0.0
        
        else:
            f_tab, f_val, f_for, f_pen, f_auto, f_meio, f_ticket = "N/A", default["VALOR"], default["FORENSE"], 0, 0, "N/A", 0

        f_alo = st.number_input("VOL. ALÔ", value=default.get("ALO", 0))
        f_cpc = st.number_input("VOL. CPC", value=default.get("CPC", 0))

        if st.form_submit_button("🚀 SINCRONIZAR E NOTIFICAR"):
            alerta = "Sinal Estável"
            if any(x in f_tab for x in ["Cabo", "Mudo", "Vácuo"]): alerta = "🚩 ALERTA DE SABOTAGEM"
            elif f_auto < 1 and visao_ativa.startswith("VISÃO DISCADOR"): alerta = "⚠️ MAILING CRÍTICO"
            
            novo = pd.DataFrame([{
                "DATA": datetime.now().strftime("%H:%M %d/%m"), "ALVO": alvo_ref, "VISAO": visao_ativa,
                "TABULACAO": f_tab, "VALOR": f_val, "ALO": f_alo, "CPC": f_cpc,
                "STATUS": "BLOQUEADO" if "ALERTA" in alerta else "LIBERADO",
                "FORENSE": f_for, "LEGAL": default["LEGAL"], "PENETRACAO": f"{f_pen}%",
                "TICKET_MEDIO": f_ticket, "AUTONOMIA_DIAS": f_auto, "NOTIFICACAO": alerta, "STATUS_MEIO": f_meio
            }])
            st.session_state.historico = pd.concat([st.session_state.historico, novo], ignore_index=True)

# --- 4. PAINEL S.P.A. (ABAS ACUMULATIVAS) ---
st.title("🛰️ S.P.A. - SENTINELA DE PERFORMANCE ATIVA")

# Painel de Notificações em Tempo Real
avisos = st.session_state.historico[st.session_state.historico["NOTIFICACAO"] != "Sinal Estável"].tail(3)
for _, n in avisos.iterrows():
    st.error(f"**ALERTA ATIVO ({n['DATA']}):** {n['NOTIFICACAO']} em {n['ALVO']} | {n['FORENSE']}")

t_ope, t_disc, t_tel, t_jur = st.tabs(["📈 OPERAÇÃO (FUSÃO)", "🧠 DISCADOR (STRAT/CAPACITY)", "📡 TELEFONIA", "⚖️ JURÍDICO"])

with t_ope:
    st.subheader("Performance Integrada (Dinheiro + Conduta)")
    df_o = st.session_state.historico[st.session_state.historico["VISAO"] == "VISÃO OPERAÇÃO (OPERADORES)"]
    st.table(df_o[["DATA", "ALVO", "TABULACAO", "VALOR", "STATUS", "FORENSE"]])

with t_disc:
    st.subheader("Capacidade de Mailing e Inteligência de Malha")
    df_d = st.session_state.historico[st.session_state.historico["VISAO"] == "VISÃO DISCADOR (MAILING/STRAT)"]
    if not df_d.empty:
        l = df_d.iloc[-1]
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("AUTONOMIA (DIAS)", f"{l['AUTONOMIA_DIAS']}")
        c2.metric("PENETRAÇÃO", l['PENETRACAO'])
        c3.metric("TICKET MÉDIO", f"R$ {l['TICKET_MEDIO']}")
        c4.metric("STATUS MEIO", l['STATUS_MEIO'])
        st.dataframe(df_d[["DATA", "ALVO", "PENETRACAO", "STATUS_MEIO", "AUTONOMIA_DIAS", "FORENSE"]], use_container_width=True)

with t_tel:
    st.subheader("Status de Rede e Trunking IP")
    st.dataframe(st.session_state.historico[st.session_state.historico["VISAO"] == "VISÃO TELEFONIA"], use_container_width=True)

with t_jur:
    st.subheader("Blindagem Forense e Legal")
    st.table(st.session_state.historico[["DATA", "ALVO", "STATUS", "LEGAL", "TABULACAO"]])

# --- 5. EXPORTAÇÃO ---
st.divider()
st.download_button("📊 EXPORTAR RELATÓRIO SPA COMPLETO", st.session_state.historico.to_csv(index=False).encode('utf-8-sig'), "SPA_Completo_Acumulado.csv")
    
