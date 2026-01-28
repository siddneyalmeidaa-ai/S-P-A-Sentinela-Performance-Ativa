import streamlit as st
import pandas as pd
from datetime import datetime
import io

# --- 1. CONFIGURAÇÃO PADRÃO OURO ---
st.set_page_config(page_title="S.P.A. MASTER - SIDNEY ALMEIDA", layout="wide", page_icon="⚖️")

# --- 2. QUANTUM MEMORY: CENÁRIOS INTEGRADOS ---
if 'db' not in st.session_state:
    st.session_state.db = {
        "OPERAÇÃO": {
            "ANA (PERFORMANCE)": {"ALO": 1200, "CON": 950, "CPC": 450, "VALOR": 45800.0, "PROJ": 91600.0, "LEGAL": "Art. 444 CLT (Conformidade)", "FOR": "Alta conversão.", "PERDA": 0.0, "STATUS": "LIBERADO"},
            "MARCOS (SABOTAGEM)": {"ALO": 2500, "CON": 50, "CPC": 5, "VALOR": 0.0, "PROJ": 0.0, "LEGAL": "Art. 482, 'e' CLT (Desídia)", "FOR": "Cabo Desconectado.", "PERDA": 1250.0, "STATUS": "BLOQUEADO"},
            "RICARDO (OMISSÃO)": {"ALO": 800, "CON": 780, "CPC": 700, "VALOR": 150.0, "PROJ": 300.0, "LEGAL": "Art. 482, 'h' CLT (Insubordinação)", "FOR": "Mudo Proposital.", "PERDA": 850.0, "STATUS": "BLOQUEADO"},
            "JULIA (VÁCUO)": {"ALO": 100, "CON": 20, "CPC": 10, "VALOR": 800.0, "PROJ": 1600.0, "LEGAL": "Art. 482, 'e' CLT (Desídia)", "FOR": "IA Detectou Vácuo.", "PERDA": 450.0, "STATUS": "BLOQUEADO"}
        },
        "DISCADOR": {
            "MAILING_VIVO_JAN": {"TOTAL": 150000, "PEN": 65, "AUTO": 12.5, "SPC": "HIGIENIZADO", "QUALIDADE": "QUENTE"},
            "BASE_RECOVERY": {"TOTAL": 300000, "PEN": 15, "AUTO": 2.1, "SPC": "PENDENTE", "QUALIDADE": "FRIO"}
        },
        "TELEFONIA": {
            "VIVO (TRUNK IP)": {"STATUS": "BLOQUEADO", "LAT": 250, "FOR": "Instabilidade SIP.", "PERDA": 5000.0},
            "SIPvox (BACKUP)": {"STATUS": "LIBERADO", "LAT": 25, "FOR": "Rota Premium.", "PERDA": 0.0}
        }
    }

# Consolidação de Dados Mestre
df_base = pd.DataFrame([
    {
        "OPERADOR": k, 
        "STATUS": v["STATUS"],
        "VALOR": v["VALOR"], 
        "X (-50%)": v["PROJ"]*0.5, 
        "LEGAL": v["LEGAL"], 
        "EVIDÊNCIA": v["FOR"],
        "ALO": v["ALO"],
        "CPC": v["CPC"]
    }
    for k, v in st.session_state.db["OPERAÇÃO"].items()
])

# --- 3. CABEÇALHO DO SISTEMA ---
st.title("🛰️ S.P.A. - SENTINELA DE PERFORMANCE ATIVA")
st.write(f"**COMANDANTE SIDNEY ALMEIDA** | 🕒 {datetime.now().strftime('%d/%m/%
