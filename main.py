# ==========================================================
# 🛰️ SISTEMA S.P.A. - SENTINELA DE PERFORMANCE ATIVA
# VERSION: 2.5 | GESTOR: S.A. | PADRAO OURO CONSOLIDADO
# DATA: 27/01/2026 | STATUS: SINCRONIZADO
# ==========================================================

import datetime

class SistemaSPA_Oficial:
    def __init__(self):
        self.gestor = "S.A."
        self.operadores = {}
        self.estorno_acumulado = 0.0
        self.vacuo_minutos = 0
        self.mailing_score = 100.0
        self.logs_auditoria = []

    def auditoria_360(self, id_op, evento, status_sip="OK", sentimento="NEUTRO"):
        """
        Executa a Auditoria Total: Comportamento (B1) + Telefonia (B2) + NLP
        """
        hora_log = datetime.datetime.now().strftime("%H:%M:%S")
        
        # --- BLOCO 2: AUDITORIA DE TELEFONIA (OPERADORAS) ---
        if status_sip == "FALSO_ALO":
            valor_fraude = 0.22 
            self.estorno_acumulado += valor_fraude
            self.logs_auditoria.append(f"[{hora_log}] BLOCO 2: Fraude detectada. Estorno gerado p/ {id_op}")
        
        # --- BLOCO 1: GESTAO DE CONDUTA (REGRA DO X) ---
        if id_op not in self.operadores:
            self.operadores[id_op] = {"X": 100.0, "falhas": 0, "status": "LIBERADO"}
        
        op = self.operadores[id_op]
        
        # Monitoramento de Sabotagem: Dedo no Gancho, Omissao, Conversa Paralela
        if evento in ["DEDO_GANCHO", "OMISSAO", "SABOTAGEM"]:
            op['falhas'] += 1
            if op['falhas'] == 2:
                op['X'] *= 0.50  # REGRA PADRAO OURO: -50% DA PROJECAO
                op['status'] = "PENDENTE"
            elif op['falhas'] >= 3:
                op['status'] = "BLOQUEADO"
                op['X'] = 0.0
            self.logs_auditoria.append(f"[{hora_log}] BLOCO 1: Falha de conduta ({evento}) por {id_op}")

        # --- MENTORIA NLP (INTELIGENCIA DE VOZ) ---
        if sentimento == "AGRESSIVO":
            return f"☕ [SPA]: {id_op}, cliente agressivo. Recomendamos PAUSA CAFE."
        return "🔥 [SPA]: Fluxo de operacao saudavel."

    def gerar_tabela_favelinha(self):
        """
        Visual Interface: Otimizada para leitura rapida em Mobile (Sem acentos)
        """
        data_obs = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
        print("\n" + "="*75)
        print(f"🛰️  S.P.A. DASHBOARD | GESTOR: {self.gestor} | {data_obs}")
        print("="*75)
        print(f"{'OPERADOR':<15} | {'STATUS':<12} | {'META X':<12} | {'FALHAS'}")
        print("-" * 75)
        
        for op, d in self.operadores.items():
            # Sincronizacao de Status
            status_visual = d['status']
            print(f"{op:<15} | {status_visual:<12} | {d['X']:>10.1f}% | {d['falhas']}")
        
        print("-" * 75)
        print(f"💰 ESTORNO RECUPERADO (OPERADORAS) : R$ {self.estorno_acumulado:.2f}")
        print(f"📡 EFICIENCIA DO DISCADOR/MAILING : {self.mailing_score}%")
        print("="*75)
        print("DIRETRIZ FINAL: ENTRA OU PULA.")
        print("="*75 + "\n")

# --- INSTANCIACAO E EXECUCAO ---
if __name__ == "__main__":
    spa = SistemaSPA_Oficial()
    
    # Simulando auditoria real para popular o Dashboard
    spa.auditoria_360("MARCOS", "OMISSAO")
    spa.auditoria_360("MARCOS", "DEDO_GANCHO", status_sip="FALSO_ALO")
    spa.auditoria_360("ANA", "NORMAL")
    
    # Gerando a saida visual
    spa.gerar_tabela_favelinha()
          
