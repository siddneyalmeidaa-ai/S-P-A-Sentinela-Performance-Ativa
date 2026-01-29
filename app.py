import streamlit as st
import pandas as pd
import hashlib
from datetime import datetime
from docx import Document
from docx.shared import Pt
import io

# --- 1. CONFIGURAÇÃO E BLINDAGEM S.A. ---
st.set_page_config(page_title="S.P.A. MASTER - SIDNEY ALMEIDA", layout="wide", page_icon="🛰️")

# CSS Proprietário para Interface de Guerra
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;} header {visibility: hidden;} footer {visibility: hidden;}
    .stDeployButton {display:none;}
    .manifesto-container {
        background-color: #050505; border-left: 5px solid #00FF41;
        padding: 20px; border-radius: 10px; margin-bottom: 25px;
    }
    .quote-text { color: #00FF41; font-size: 18px; font-weight: bold; font-style: italic; }
    .signature { color: #D4AF37; font-size: 12px; text-transform: uppercase; letter-spacing: 2px; }
    .diag-box { background-color: #1a1a1a; border-left: 5px solid #FF4B4B; padding: 15px; margin: 10px 0; border-radius: 5px; }
    .prog-box { background-color: #1a1a1a; border-left: 5px solid #FFA500; padding: 15px; margin: 10px 0; border-radius: 5px; }
    .sol-box { background-color: #1a1a1a; border-left: 5px solid #00FF41; padding: 15px; margin: 10px 0; border-radius: 5px; }
    .ofensor-red { color: #FF0000; font-weight: bold; border: 2px solid #FF0000; padding: 10px; border-radius: 5px; text-align: center; }
    </style>
""", unsafe_allow_html=True)

# --- 2. BANCO DE DADOS INTEGRAL (ACUMULADO) ---
if 'db' not in st.session_state:
    st.session_state.db = {
        "OPERAÇÃO": {
            "ANA (PERFORMANCE)": {
                "CPF": "123.456.789-01", "VALOR_REAL": 46600.0, "PROJ": 93200.0, 
                "STATUS": "85% LIBERADO", "TEMPO_LOGADO": "08:00:00", "PAUSA": 40, 
                "DISCADAS": 1200, "ALO": 450, "CPC": 120, "CPCA": 95, "PROMESSAS_N": 70, "SABOTAGEM_SCORE": 0
            },
            "MARCOS (SABOTAGEM)": {
                "CPF": "456.123.789-55", "VALOR_REAL": 0.0, "PROJ": 0.0, 
                "STATUS": "0% PENDENTE", "TEMPO_LOGADO": "03:15:00", "PAUSA": 125, 
                "DISCADAS": 800, "ALO": 12, "CPC": 2, "CPCA": 1, "PROMESSAS_N": 0, "SABOTAGEM_SCORE": 85
            }
        },
        "DISCADOR": {
            "IA_SENTINELA": "ATIVO", "MAILING": "MAILING_OURO_V1", 
            "DESCONHECIDOS": 42.5, "INEXISTENTES": 28.1, "CAIXA_POSTAL": 15.4
        },
        "TELEFONIA": {
            "LAT": 380, "SERVER": "Vivo Cloud", "JITTER": "15ms", "LOSS": "2.5%"
        }
    }

# --- 3. LÓGICA TÁTICA E CÁLCULOS (MÉTRICA CORRIGIDA) ---
LIMITE_PAUSA = 45
df_list = []
for k, v in st.session_state.db["OPERAÇÃO"].items():
    prom = v.get("PROMESSAS_N", 0)
    cpca = v.get("CPCA", 0)
                
