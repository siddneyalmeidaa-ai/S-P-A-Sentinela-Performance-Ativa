import streamlit as st
import pandas as pd
from datetime import datetime
from io import BytesIO
from fpdf import FPDF
from docx import Document

# --- 1. CONFIGURAÇÃO E IDENTIDADE VISUAL ---
st.set_page_config(page_title="S.P.A. - Sidney Almeida", layout="wide", page_icon="🛰️")

# --- 2. QUANTUM MEMORY: BANCO DE DADOS AUTOMATIZADO (FICTÍCIO PARA DEMO) ---
# Aqui estão todos os cenários acumulados (Performance, Sabotagem, Omissão e Infra)
if 'db_ficticio' not in st.session_state:
    st.session_state.db_ficticio = {
        "ANA": {
            "ALO": 450, "CPC": 180, "VALOR": 12500.50, "STATUS": "LIBERADO", 
            "MOTIVO": "Fase 3: Fechamento", "LEGAL": "Regimento Interno",
            "FORENSE": "Alta performance. Operadora utiliza gatilhos de escassez com maestria. Perfil agressivo de fechamento e conversão limpa.",
            "VISAO": "VISÃO OPERAÇÃO"
        },
        "MARCOS": {
            "ALO": 890, "CPC": 12, "VALOR": 0.00, "STATUS": "BLOQUEADO", 
            "MOTIVO": "Desconexão Física (Cabo)", "LEGAL": "Art. 482 CLT - Desídia",
            "FORENSE": "O sistema detectou 42 interrupções manuais de hardware (Physical Link Down). Operador força a queda para evitar CPC e permanecer ocioso.",
            "VISAO": "VISÃO DISCADOR"
        },
        "RICARDO": {
            "ALO": 320, "CPC": 290, "VALOR": 150.00, "STATUS": "BLOQUEADO", 
            "MOTIVO": "Mudo Proposital", "LEGAL": "Insubordinação Técnica",
            "FORENSE": "Atendimento realizado, porém áudio do operador suprimido via software. Cliente desliga por falta de interação. CPC inflado artificialmente.",
            "VISAO": "VISÃO DISCADOR"
        },
        "JULIA": {
            "ALO": 510, "CPC": 150, "VALOR": 4200.00, "STATUS": "LIBERADO", 
            "MOTIVO": "Fase 2: Oferta", "LEGAL": "Regimento Interno",
            "FORENSE": "Volume de CPC dentro da média operacional. Mantém constância produtiva sem alertas de sabotagem detectados.",
            "VISAO": "VISÃO OPERAÇÃO"
        },
        "VIVO": {
            "ALO": 5000, "CPC": 800, "VALOR": 3500.00, "STATUS": "BLOQUEADO", 
            "MOTIVO": "Queda de Trunk IP", "LEGAL": "SLA de Contrato Técnica",
            "FORENSE": "Instabilidade massiva detectada no Gateway SIP. Perda de 65% de pacotes de voz (Jitter). Impacto direto na produtividade da célula.",
            "VISAO": "VISÃO TELEFONIA"
        }
    }

# Inicializa o histórico de registros se estiver vazio
if 'historico' not in st.session_state:
    st.session_state.historico = pd.DataFrame(columns=[
        "DATA", "ALVO", "VISAO", "MOTIVO_TECNICO", "VALOR", 
        "ALO", "CPC", "STATUS", "DETALHE_FORENSE", "BASE_LEGAL"
    ])

# --- 3. FUNÇÕES DE EXPORTAÇÃO (ACUMULATIVO) ---
def gerar_pdf(df):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="S.P.A. - RELATÓRIO DE AUDITORIA FORENSE", ln=True, align='C')
    pdf.set_font("Arial", size=9)
    for i, row in df.iterrows():
        pdf.multi_cell(0, 8, f"DATA: {row['DATA']} | ALVO: {row['ALVO']} | STATUS: {row['STATUS']}\nMOTIVO: {row['MOTIVO_TECNICO']} | VALOR: R$ {row['VALOR']}\nLEGAL: {row['BASE_LEGAL']}\nDETALHE: {row['DETALHE_FORENSE']}\n{'-'*80}")
    return pdf.output(dest='S').encode('latin-1', 'ignore')

def gerar_word(df):
    doc = Document()
    doc.add_heading('Dossiê S.P.A. - Sentinela de Performance Ativa', 0)
    for i, row in df.iterrows():
        doc.add_paragraph(f"DATA: {row['DATA']} - ALVO: {row['ALVO']}", style='Heading 2')
        doc.add_paragraph(f"STATUS: {row['STATUS']} | MOTIVO: {row['MOTIVO_TECNICO']}")
        doc.add_paragraph(f"DETALHAMENTO: {row['DETALHE_FORENSE']}")
    bio = BytesIO()
    doc.save(bio)
    return bio.getvalue()

# --- 4. BARRA LATERAL: COMANDO AUTOMATIZADO ---
with st.sidebar:
    st.header("🕵️ COMANDO CENTRAL")
    visao_ativa = st.radio("VISÃO", ["VISÃO OPERAÇÃO", "VISÃO DISCADOR", "VISÃO TELEFONIA", "VISÃO JURÍDICA"])
    
    st.divider()
    alvo_selecionado = st.selectbox("AUTOMATIZAR POR PERFIL:", list(st.session_state.db_ficticio.keys()))
    dados_auto = st.session_state.db_ficticio[alvo_selecionado]
    
    with st.form("master_input"):
        st.info(f"Modo Automatizado: {alvo_selecionado}")
        f_alo = st.number_input("VOL. ALÔ", value=dados_auto["ALO"])
        f_cpc = st.number_input("VOL. CPC", value=dados_auto["CPC"])
        f_valor = st.number_input("VALOR (R$)", value=dados_auto["VALOR"])
        f_motivo = st.text_input("MOTIVO TÉCNICO", value=dados_auto["MOTIVO"])
        f_legal = st.text_input("BASE LEGAL", value=dados_auto["LEGAL"])
        f_forense = st.text_area("DETALHAMENTO (MENTE):", value=dados_auto["FORENSE"])
        
        if st.form_submit_button("🚀 SINCRONIZAR NO SERVIDOR"):
            novo_dado = pd.DataFrame([{
                "DATA": datetime.now().strftime("%d/%m/%Y %H:%M"), "ALVO": alvo_selecionado, 
                "VISAO": visao_ativa, "MOTIVO_TECNICO": f_motivo, "VALOR": f_valor, 
                "ALO": f_alo, "CPC": f_cpc, "STATUS": dados_auto["STATUS"], 
                "DETALHE_FORENSE": f_forense, "BASE_LEGAL": f_legal
            }])
            st.session_state.historico = pd.concat([st.session_state.historico, novo_dado], ignore_index=True)
            st.success("DADOS INTEGRADOS!")

# --- 5. PAINEL DE CONTROLE E ABAS (ACUMULATIVO) ---
st.title("🛰️ S.P.A. - SENTINELA DE PERFORMANCE ATIVA")
st.markdown(f"**DATA:** {datetime.now().strftime('%d/%m/%Y')} | **SISTEMA PADRÃO OURO**")

t_ope, t_dis, t_tel, t_jur = st.tabs(["📈 OPERAÇÃO", "🔍 DISCADOR", "📡 TELEFONIA", "⚖️ JURÍDICO"])

with t_ope:
    st.subheader("Performance Financeira e Conversão")
    df_o = st.session_state.historico[st.session_state.historico["VISAO"] == "VISÃO OPERAÇÃO"]
    if not df_o.empty:
        c1, c2, c3 = st.columns(3)
        c1.metric("TOTAL RECUPERADO", f"R$ {df_o['VALOR'].sum():,.2f}")
        c2.metric("ALÔ (TOTAL)", int(df_o["ALO"].sum()))
        c3.metric("CPC (TOTAL)", int(df_o["CPC"].sum()))
        st.dataframe(df_o, use_container_width=True)

with t_dis:
    st.subheader("Auditoria de Comportamento (Shadow Logs)")
    df_d = st.session_state.historico[st.session_state.historico["VISAO"] == "VISÃO DISCADOR"]
    for i, row in df_d.iterrows():
        with st.expander(f"📌 {row['ALVO']} - {row['MOTIVO_TECNICO']} ({row['STATUS']})"):
            st.error(f"DETALHE FORENSE: {row['DETALHE_FORENSE']}")
            st.caption(f"Evidência Técnica vinculada ao Artigo: {row['BASE_LEGAL']}")

with t_tel:
    st.subheader("Status de Conectividade Externa")
    df_t = st.session_state.historico[st.session_state.historico["VISAO"] == "VISÃO TELEFONIA"]
    st.table(df_t)

with t_jur:
    st.subheader("🛡️ Blindagem Jurídica Ativa")
    st.warning("Dossiês gerados automaticamente com base em desvios técnicos e comportamentais.")
    st.dataframe(st.session_state.historico[["DATA", "ALVO", "MOTIVO_TECNICO", "BASE_LEGAL", "STATUS"]], use_container_width=True)

# --- 6. CENTRAL MULTIFORMATO DE EXPORTAÇÃO ---
st.divider()
st.subheader("📥 EXPORTAR EVIDÊNCIAS")
if not st.session_state.historico.empty:
    col1, col2, col3, col4 = st.columns(4)
    # Excel
    output_xlsx = BytesIO()
    with pd.ExcelWriter(output_xlsx, engine='xlsxwriter') as writer:
        st.session_state.historico.to_excel(writer, index=False)
    col1.download_button("📊 Excel (BI)", output_xlsx.getvalue(), "Relatorio_SPA.xlsx")
    # PDF
    col2.download_button("📄 PDF (Auditoria)", gerar_pdf(st.session_state.historico), "Relatorio_SPA.pdf")
    # CSV
    col3.download_button("📁 CSV (Sistemas)", st.session_state.historico.to_csv(index=False).encode('utf-8-sig'), "Relatorio_SPA.csv")
    # Word
    col4.download_button("📝 Word (Dossiê)", gerar_word(st.session_state.historico), "Relatorio_SPA.docx")
        
