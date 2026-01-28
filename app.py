import streamlit as st
import pandas as pd
from datetime import datetime
from io import BytesIO

# --- 1. CONFIGURAÇÃO ---
st.set_page_config(page_title="S.P.A. Sidney Almeida", layout="wide", page_icon="🛰️")

# --- 2. QUANTUM MEMORY: BANCO DE DADOS FICTÍCIO INTEGRADO ---
if 'db_ficticio' not in st.session_state:
    st.session_state.db_ficticio = {
        "ANA": {"ALO": 450, "CPC": 180, "VALOR": 12500.50, "STATUS": "LIBERADO", "MOTIVO": "Fase 3: Fechamento", "FORENSE": "Alta performance. Scripts de urgência aplicados.", "LEGAL": "Regimento Interno"},
        "MARCOS": {"ALO": 890, "CPC": 12, "VALOR": 0.00, "STATUS": "BLOQUEADO", "MOTIVO": "Desconexão Cabo", "FORENSE": "42 quedas de hardware detectadas. Sabotagem física.", "LEGAL": "Art. 482 CLT"},
        "RICARDO": {"ALO": 320, "CPC": 290, "VALOR": 150.00, "STATUS": "BLOQUEADO", "MOTIVO": "Mudo Proposital", "FORENSE": "Operador atende e silencia microfone.", "LEGAL": "Insubordinação"},
        "JULIA": {"ALO": 510, "CPC": 150, "VALOR": 4200.00, "STATUS": "LIBERADO", "MOTIVO": "Fase 2: Oferta", "FORENSE": "Volume constante, sem alertas.", "LEGAL": "Regimento Interno"},
        "VIVO": {"ALO": 5000, "CPC": 800, "VALOR": 3500.00, "STATUS": "BLOQUEADO", "MOTIVO": "Queda Trunk IP", "FORENSE": "Falha massiva no Gateway SIP.", "LEGAL": "SLA Técnica"}
    }

if 'historico' not in st.session_state:
    st.session_state.historico = pd.DataFrame(columns=[
        "DATA", "ALVO", "VISAO", "MOTIVO", "VALOR", "ALO", "CPC", 
        "STATUS", "FORENSE", "LEGAL", "PENETRACAO", "TICKET_MEDIO", 
        "AUTONOMIA_DIAS", "NOTIFICACAO", "STATUS_MEIO"
    ])

# --- 3. BARRA LATERAL: COMANDO DINÂMICO ---
with st.sidebar:
    st.header("🕵️ COMANDO CENTRAL")
    visao_ativa = st.radio("SISTEMA", ["VISÃO OPERAÇÃO (FUSÃO)", "VISÃO DISCADOR (STRAT/CAPACITY)", "VISÃO TELEFONIA", "VISÃO JURÍDICA"])
    
    st.divider()
    # Filtro inteligente de alvos
    if visao_ativa == "VISÃO TELEFONIA":
        lista_alvos = ["VIVO", "CLARO", "SIPvox"]
    else:
        lista_alvos = ["ANA", "MARCOS", "RICARDO", "JULIA", "CARTEIRA VIVO", "RETAIL"]
        
    alvo_ref = st.selectbox("SELECIONE O ALVO:", lista_alvos)
    
    # Puxa dados automáticos do banco fictício
    default = st.session_state.db_ficticio.get(alvo_ref, {"ALO":0, "CPC":0, "VALOR":0.0, "STATUS":"Pendente", "MOTIVO":"N/A", "FORENSE":"", "LEGAL":"N/A"})

    with st.form("master_sync"):
        st.subheader("⚙️ Input de Dados")
        
        if visao_ativa == "VISÃO DISCADOR (STRAT/CAPACITY)":
            f_ticket = st.number_input("TICKET MÉDIO (R$)", value=185.00)
            f_pen = st.slider("TAXA DE PENETRAÇÃO (%)", 0, 100, 42)
            f_leads = st.number_input("TOTAL DE LEADS NA BASE", value=60000)
            f_ops = st.number_input("OPERADORES ATIVOS", value=25)
            # Cálculo de Autonomia (Base / (Ops * 400 ligações/dia))
            f_auto = round(f_leads / (f_ops * 400), 2) if f_ops > 0 else 0
            f_meio = st.selectbox("STATUS DO MEIO", ["QUENTE", "NECESSITA ENRIQUECIMENTO", "BASE MORTA", "RECICLADO"])
            f_motivo = "AUDITORIA ESTRATÉGICA"
            f_valor, f_forense, f_legal = 0, "Análise estratégica de malha.", "N/A"
        else:
            f_motivo = st.text_input("MOTIVO/AÇÃO", value=default["MOTIVO"])
            f_valor = st.number_input("VALOR (R$)", value=default["VALOR"])
            f_forense = st.text_area("DETALHE (MENTE)", value=default["FORENSE"])
            f_legal = default["LEGAL"]
            f_ticket, f_pen, f_auto, f_meio = 0, 0, 0, "N/A"

        f_alo = st.number_input("ALÔ", value=default["ALO"])
        f_cpc = st.number_input("CPC", value=default["CPC"])

        if st.form_submit_button("🚀 SINCRONIZAR NO SERVIDOR"):
            alerta = "Sinal Estável"
            if "Cabo" in f_motivo or "Mudo" in f_motivo: alerta = "🚩 ALERTA DE SABOTAGEM"
            elif f_auto < 1 and visao_ativa.startswith("VISÃO DISCADOR"): alerta = "⚠️ MAILING ESGOTANDO"
            
            novo = pd.DataFrame([{
                "DATA": datetime.now().strftime("%H:%M %d/%m"), "ALVO": alvo_ref, "VISAO": visao_ativa,
                "MOTIVO": f_motivo, "VALOR": f_valor, "ALO": f_alo, "CPC": f_cpc,
                "STATUS": "BLOQUEADO" if "ALERTA" in alerta else "LIBERADO",
                "FORENSE": f_forense, "LEGAL": f_legal, "PENETRACAO": f"{f_pen}%",
                "TICKET_MEDIO": f_ticket, "AUTONOMIA_DIAS": f_auto, "NOTIFICACAO": alerta, "STATUS_MEIO": f_meio
            }])
            st.session_state.historico = pd.concat([st.session_state.historico, novo], ignore_index=True)

# --- 4. PAINEL S.P.A. (ABAS ACUMULATIVAS) ---
st.title("🛰️ S.P.A. - SENTINELA DE PERFORMANCE ATIVA")

# Exibição de Notificações Ativas
avisos = st.session_state.historico[st.session_state.historico["NOTIFICACAO"] != "Sinal Estável"].tail(3)
for _, n in avisos.iterrows():
    st.error(f"**{n['DATA']} - {n['NOTIFICACAO']}**: {n['ALVO']} | {n['FORENSE']}")

t_ope, t_disc, t_tel, t_jur = st.tabs(["📈 OPERAÇÃO (FUSÃO)", "🧠 DISCADOR (STRAT/MALHA)", "📡 TELEFONIA", "⚖️ JURÍDICO"])

with t_ope:
    st.subheader("Performance Integrada")
    df_o = st.session_state.historico[st.session_state.historico["VISAO"] == "VISÃO OPERAÇÃO (FUSÃO)"]
    st.table(df_o[["DATA", "ALVO", "MOTIVO", "VALOR", "STATUS", "FORENSE"]])

with t_disc:
    st.subheader("Capacity, Malha e Enriquecimento")
    df_d = st.session_state.historico[st.session_state.historico["VISAO"] == "VISÃO DISCADOR (STRAT/CAPACITY)"]
    if not df_d.empty:
        l = df_d.iloc[-1]
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("AUTONOMIA", f"{l['AUTONOMIA_DIAS']} Dias")
        c2.metric("PENETRAÇÃO", l['PENETRACAO'])
        c3.metric("TICKET MÉDIO", f"R$ {l['TICKET_MEDIO']}")
        c4.metric("QUALIDADE", l['STATUS_MEIO'])
        st.dataframe(df_d[["DATA", "ALVO", "PENETRACAO", "STATUS_MEIO", "AUTONOMIA_DIAS", "FORENSE"]], use_container_width=True)

with t_tel:
    st.subheader("Status de Rede")
    st.dataframe(st.session_state.historico[st.session_state.historico["VISAO"] == "VISÃO TELEFONIA"], use_container_width=True)

with t_jur:
    st.subheader("Evidências Jurídicas")
    st.table(st.session_state.historico[["DATA", "ALVO", "STATUS", "LEGAL", "MOTIVO"]])

# --- 5. EXPORTAÇÃO ---
st.divider()
st.download_button("📊 EXPORTAR RELATÓRIO SPA", st.session_state.historico.to_csv(index=False).encode('utf-8-sig'), "Relatorio_SPA_Completo.csv")
