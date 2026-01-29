import streamlit as st
import pandas as pd
import hashlib
from datetime import datetime
from docx import Document  # Requisito: pip install python-docx
from docx.shared import Pt
import io

# --- 1. CONFIGURAÇÃO DE AMBIENTE E SEGURANÇA S.A. ---
st.set_page_config(page_title="S.P.A. MASTER - SIDNEY ALMEIDA", layout="wide", page_icon="🛰️")

# CSS PROPRIETÁRIO - BLINDAGEM CONTRA TELA PRETA (SINTAXE FECHADA)
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
    
