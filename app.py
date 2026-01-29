import streamlit as st
import pandas as pd
import hashlib
from datetime import datetime
from docx import Document
from docx.shared import Pt
import io

# --- 1. CONFIGURAÇÃO DE AMBIENTE E SEGURANÇA S.A. ---
st.set_page_config(page_title="S.P.A. MASTER - SIDNEY ALMEIDA", layout="wide", page_icon="🛰️")

# CSS PROPRIETÁRIO - BLINDAGEM TOTAL (TODAS AS ASPAS FECHADAS)
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;} 
    header {visibility: hidden;} 
    footer {visibility: hidden;}
    .stDeployButton {display:none;}
    .manifesto-container {
        background-color: #050505; 
        border-left: 5px solid #00FF41;
        padding: 20px; 
        border-radius: 10px; 
        margin-bottom: 25px;
    }
    .quote-text { color: #00FF41; font-size: 18px; font-weight: bold; font-style: italic; }
    .signature { color: #D4AF37; font-size: 12px; text-transform: uppercase; letter-spacing: 2px; }
    .diag-box { background-color: #1a1a1a; border-left: 5px solid #FF4B4B; padding: 15px; margin: 10px 0; border-radius: 5px; }
    .sol-box { background-color: #1a1a1a; border-left: 5px solid #00FF41; padding: 15px; margin: 10px 0; border-radius: 5px; }
    .ofensor-red { color: #FF0000; font-weight: bold; border: 2px solid #FF0000; padding: 10px; border-radius: 5px; text-align: center; }
    </style>
""", unsafe_allow_html=True)

# --- 2. BANCO DE DADOS INTEGRAL (QUANTUM MEMORY - SEM ERRO DE CHAVE) ---
if 'db' not in st.session_state:
    st.session_state.db = {
        "OPERAÇÃO": {
            "ANA (PERFORMANCE)": {
                "CPF": "123.456.789-01", 
                "VALOR_REAL": 46600.0, 
                "PROJ": 93200.0, 
                "STATUS": "85% LIBERADO", 
                "TEMPO_LOGADO": "08:00:00", 
                "PAUSA": 40, 
                "ALO": 450, 
                "CPC": 120, 
                "CPCA": 95, 
                "PROMESSAS_N": 70, 
                "SABOTAGEM_SCORE": 0
            },
            "MARCOS (SABOTAGEM)": {
                "CPF": "456.123.789-55", 
                "VALOR_REAL": 0.0, 
                "PROJ": 0.0, 
                "STATUS": "0% PENDENTE", 
                "TEMPO_LOGADO": "03:15:00", 
                "PAUSA": 125, 
                "ALO": 12, 
                "CPC": 2, 
                "CPCA": 1, 
                "PROMESSAS_N": 0, 
                "SABOTAGEM_SCORE": 85
            }
        },
        "DISCADOR": {
            "IA_SENTINELA": "ATIVO", 
            "MAILING": "MAILING_OURO_V1", 
            "DESCONHECIDOS": 42.5, 
            "INEXISTENTES": 28.1, 
            "CAIXA_POSTAL": 15.4
        },
        "TELEFONIA": {
            "LAT": 380, 
            "SERVER": "Vivo Cloud", 
            "JITTER": "15ms", 
            "LOSS": "2.5%"
        }
    }

# --- 3. LÓGICA DE PROCESSAMENTO (FÓRMULA: PROMESSA / CPCA) ---
LIMITE_PAUSA = 45
df_list = []
for k, v in st.session_state.db["OPERAÇÃO"].items():
    prom = v.get("PROMESSAS_N", 0)
    cpca = v.get("CPCA", 0)
    # REGRA ATUALIZADA: PROMESSA / CPCA
    conv = round((prom / cpca * 100), 1) if cpca > 0 else 0
    df_list.append({
        "OPERADOR": k, 
        "CPF": v.get("CPF"), 
        "ALÔ": v.get("ALO"), 
        "CPC": v.get("CPC"), 
        "CPCA": cpca, 
        "PROMESSAS": prom, 
        "CONV %": conv, 
        "REAL": v.get("VALOR_REAL", 0.0), 
        "X (-50%)": (v.get("PROJ", 0.0) * 0.5),
        "LOGADO": v.get("TEMPO_LOGADO", "00:00:00"), 
        "PAUSA": v.get("PAUSA", 0),
        "SABOTAGEM": v.get("SABOTAGEM_SCORE", 0), 
        "STATUS": v.get("STATUS")
    })
df_audit = pd.DataFrame(df_list)

# --- 4. ENGINE DE ADVERTÊNCIA JURÍDICA (WORD .DOCX) ---
def gerar_termo_docx(nome, cpf, pausa, dano_financeiro):
    doc = Document()
    doc.add_heading('TERMO DE ADVERTÊNCIA DISCIPLINAR - S.A. COMPLIANCE', 0)
    p = doc.add_paragraph()
    p.add_run(f"DATA DE EMISSÃO: {datetime.now().strftime('%d/%m/%Y')}\n").bold = True
    p.add_run(f"OPERADOR(A): {nome}\n")
    p.add_run(f"IDENTIFICAÇÃO (CPF): {cpf}\n")
    doc.add_heading('1. RELATÓRIO DE INFRAÇÃO', level=1)
    doc.add_paragraph(f"Detectada pausa de {pausa} minutos. Limite excedido ({LIMITE_PAUSA}m).")
    doc.add_heading('2. FUNDAMENTAÇÃO LEGAL', level=1)
    doc.add_paragraph("Artigo 482 da CLT, alínea 'e' (Desídia operacional).")
    doc.add_heading('3. MENSURAÇÃO DE PREJUÍZO', level=1)
    doc.add_paragraph(f"Dano patrimonial calculado: R$ {dano_financeiro:.2f}.")
    doc.add_paragraph("\n\n__________________________________________\nAssinatura do Colaborador")
    doc.add_paragraph("__________________________________________\nSidney Almeida - Comando S.A.")
    output = io.BytesIO()
    doc.save(output)
    output.seek(0)
    return output

# --- 5. INTERFACE DE COMANDO S.A. (7 ABAS INTEGRALIZADAS) ---
st.markdown("""
<div class="manifesto-container">
    <div class="quote-text">"S.P.A. MASTER - SIDNEY ALMEIDA"</div>
    <div class="signature">👊🚀
