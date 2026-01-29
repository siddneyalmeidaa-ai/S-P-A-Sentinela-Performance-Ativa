import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. CONFIGURAÇÃO E BLINDAGEM DE INTERFACE ---
st.set_page_config(page_title="S.P.A. MASTER - SIDNEY ALMEIDA", layout="wide", page_icon="🛰️")

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;} header {visibility: hidden;} footer {visibility: hidden;}
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
    </style>
""", unsafe_allow_html=True)

# --- 2. BANCO DE DADOS INTEGRAL (CORREÇÃO DOS 12 PRINTS) ---
# Fechamento rigoroso de todas as chaves para evitar SyntaxError
if 'db' not in st.session_state:
    st.session_state.db = {
        "OPERAÇÃO": {
            "ANA (PERFORMANCE)": {
                "VALOR_REAL": 45800.0, "PROJ": 91600.0, "VALOR_NEGOCIADO": 125400.0,
                "STATUS": "85% LIBERADO", "MINUTOS_PAUSA": 40, "DISCADAS": 1200, 
                "ALO": 450, "CPC": 120, "CPCA": 95, "PROMESSAS_N": 70,
                "P1": "00:10:00", "P2": "00:10:00", "LANCHE": "00:20:00", "BANHEIRO": "00:00:00"
            },
            "MARCOS (SABOTAGEM)": {
                "VALOR_REAL": 0.0, "PROJ": 0.0, "VALOR_NEGOCIADO": 0.0,
                "STATUS": "0% BLOQUEADO", "MINUTOS_PAUSA": 125, "DISCADAS": 800, 
                "ALO": 12, "CPC": 0, "CPCA": 0, "PROMESSAS_N": 0,
                "P1": "00:25:00", "P2": "00:30:00", "LANCHE": "01:00:00", "BANHEIRO": "00:30:00"
            },
            "JULIA (VÁCUO)": {
                "VALOR_REAL": 800.0, "PROJ": 1600.0, "VALOR_NEGOCIADO": 2500.0,
                "STATUS": "12% OK", "MINUTOS_PAUSA": 55, "DISCADAS": 500, 
                "ALO": 85, "CPC": 8, "CPCA": 4, "PROMESSAS_N": 1,
                "P1": "00:10:00", "P2": "00:10:00", "LANCHE": "00:20:00", "BANHEIRO": "00:15:00"
            }
        },
        "DISCADOR": {"PEN": 65, "MAILING": "Ativo 2026", "TOTAL_DISCADAS": 2500},
        "TELEFONIA": {"LAT": 250, "STATUS": "CRÍTICO", "SERVER": "Vivo Cloud"}
    }

# --- 3. LOGICA DE AUDITORIA E CÁLCULO X (-50%) ---
df_list = []
for k, v in st.session_state.db["OPERAÇÃO"].items():
    alo = v.get("ALO", 0)
    disc = v.get("DISCADAS", 1)
    cpc = v.get("CPC", 0)
    df_list.append({
        "OPERADOR": k,
        "LOC %": (alo / disc * 100),
        "CPCA (CONTATO)": v.get("CPCA", 0),
        "CONV %": (cpc / alo * 100) if alo > 0 else 0,
        "PROMESSAS (Nº)": int(v.get("PROMESSAS_N", 0)),
        "NEGOCIADO": v.get("VALOR_NEGOCIADO", 0.0),
        "REAL": v.get("VALOR_REAL", 0.0),
        "PROJEÇÃO": v.get("PROJ", 0.0),
        "X (-5
        
