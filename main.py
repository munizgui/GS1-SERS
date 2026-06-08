import random
import time

# --- CONFIGURAÇÕES DE LIMITES (Tomada de Decisão Básica) ---
TEMP_MAX = 85.0  # Temperatura máxima segura em °C
ENERGIA_MIN = 20.0  # Porcentagem mínima de energia segura
SINAL_MIN = 30.0  # Qualidade mínima de sinal de comunicação


def simular_telemetria():
    """Simula a geração de dados operacionais da missão espacial."""
    dados = {
        "temperatura": round(random.uniform(15.0, 95.0), 2),  # em °C
        "energia": round(random.uniform(10.0, 100.0), 2),  # em %
        "comunicacao": round(random.uniform(10.0, 100.0), 2),  # em % (qualidade do sinal)
        "modulo_propulsao": random.choice(["ATIVO", "OCIOSO", "FALHA"]),
        "modulo_suporte_vida": random.choice(["ATIVO", "RESERVA", "FALHA"])
    }
    return dados


def analisar_dados(dados):
    """
    Interpreta os dados e aplica a tomada de decisão automática (geração de alertas).
    """
    alertas = []
    acoes_corretivas = []

    # Verificação de Temperatura
    if dados["temperatura"] > TEMP_MAX:
        alertas.append(f"ALERTA CRÍTICO: Temperatura elevada ({dados['temperatura']}°C)!")
        acoes_corretivas.append("AÇÃO AUTOMÁTICA: Ativando sistema de resfriamento líquido criogênico.")

    # Verificação de Energia
    if dados["energia"] < ENERGIA_MIN:
        alertas.append(f"ALERTA CRÍTICO: Bateria em nível crítico ({dados['energia']}%).")
        acoes_corretivas.append("AÇÃO AUTOMÁTICA: Desligando módulos secundários. Redirecionando painéis solares.")

    # Verificação de Comunicação
    if dados["comunicacao"] < SINAL_MIN:
        alertas.append(f"AVISO: Instabilidade no sinal de comunicação ({dados['comunicacao']}%).")
        acoes_corretivas.append("AÇÃO AUTOMÁTICA: Reorientando antena principal para o satélite mais próximo.")

    # Verificação dos Módulos
    if dados["modulo_propulsao"] == "FALHA":
        alertas.append("ALERTA CRÍTICO: Falha detectada no Módulo de Propulsão!")
        acoes_corretivas.append(
            "AÇÃO AUTOMÁTICA: Isolando injetores de combustível e acionando propulsores de emergência.")

    if dados["modulo_suporte_vida"] == "FALHA":
        alertas.append("ALERTA MÁXIMO: Falha no Sistema de Suporte de Vida!")
        acoes_corretivas.append("AÇÃO AUTOMÁTICA: Ativando cilindros de oxigênio reserva imediatamente.")

    return alertas, acoes_corretivas


def exibir_painel(dados, alertas, acoes):
    """Exibe as informações monitoradas de forma clara e organizada no console."""
    print("\n" + "=" * 60)
    print("      SISTEMA INTELIGENTE DE MONITORAMENTO ESPACIAL (SERS)     ")
    print("=" * 60)

    print("\n[ TELEMETRIA DOS MÓDULOS ]")
    print(f" -> Temperatura Interna:    {dados['temperatura']} °C")
    print(f" -> Nível de Energia:       {dados['energia']} %")
    print(f" -> Sinal de Comunicação:   {dados['comunicacao']} %")
    print(f" -> Módulo de Propulsão:    {dados['modulo_propulsao']}")
    print(f" -> Suporte de Vida:        {dados['modulo_suporte_vida']}")

    print("\n" + "-" * 60)
    print("[ STATUS DO SISTEMA / ALERTAS ]")

    if not alertas:
        print(" -> Todos os sistemas operando dentro dos parâmetros normais. [ESTÁVEL]")
    else:
        for alerta in alertas:
            print(f" [!] {alerta}")

        print("\n[ TOMADA DE DECISÃO AUTOMATIZADA ]")
        for acao in acoes:
            print(f" -> {acao}")

    print("=" * 60 + "\n")


def main():
    """Loop principal do monitoramento da missão."""
    print("Iniciando monitoramento da Missão Espacial Experimental...")
    time.sleep(1)

    # Executa o monitoramento em loop (simulando tempo real)
    ciclos = 5
    contador = 0

    try:
        while contador < ciclos:
            dados_atuais = simular_telemetria()
            alertas, acoes = analisar_dados(dados_atuais)
            exibir_painel(dados_atuais, alertas, acoes)

            # Espera 3 segundos antes da próxima leitura de dados
            time.sleep(3)
            contador += 1

        print("Simulação finalizada com sucesso.")

    except KeyboardInterrupt:
        print("\nMonitoramento encerrado pelo operador.")


if __name__ == "__main__":
    main()