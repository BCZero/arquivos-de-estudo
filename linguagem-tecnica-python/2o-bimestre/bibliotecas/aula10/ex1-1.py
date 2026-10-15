import numpy as np

# ==========================================
# 1. FUNÇÃO: MENU DE USO DAS CPUs (%)
# ==========================================
def menu_servidor(medicoes):
    while True:
        print("\n" + "="*35)
        print("      PAINEL DE USO DAS CPUs (%)")
        print("="*35)
        print("1 - Quantidade de CPUs")
        print("2 - Média de uso no servidor")
        print("3 - CPU com mais folga (menor uso)")
        print("4 - CPU com menos folga (maior uso)")
        print("5 - Listar CPUs críticas (> 80%)")
        print("6 - Ver relatório completo de uso")
        print("0 - Voltar ao Menu Principal")
        print("="*35)

        opcao = input("Escolha uma opção: ").strip()

        match opcao:
            case "1":
                print(f"\n[+] Quantidade de amostras: {medicoes.size}")
            case "2":
                print(f"\n[+] Média das amostras: {np.mean(medicoes):.2f}%")
            case "3":
                print(f"\n[+] CPU com mais folga: {np.min(medicoes)}%")
            case "4":
                print(f"\n[+] CPU com menos folga: {np.max(medicoes)}%")
            case "5":
                print("\n===== CPUs CRÍTICAS (> 80%) =====")
                encontrou = False
                for i in range(medicoes.size):
                    if medicoes[i] > 80:
                        print(f"CPU {i} com processamento {medicoes[i]}%")
                        encontrou = True
                if not encontrou:
                    print("Nenhuma CPU acima do limite crítico.")
            case "6":
                print("\n===== RELATÓRIO COMPLETO DE USO =====")
                print("Quantidade de amostras:", medicoes.size)
                print(f"Média das amostras: {np.mean(medicoes):.2f}%")
                print(f"CPU com mais folga: {np.min(medicoes)}%")
                print(f"CPU com menos folga: {np.max(medicoes)}%")
                print("CPUs críticas:", medicoes[medicoes > 80])
            case "0":
                print("\nVoltando ao Menu Principal...")
                break
            case _:
                print("\n[!] Opção inválida! Digite um número de 0 a 6.")


# ==========================================
# 2. FUNÇÃO: MENU DE TEMPERATURAS (°C)
# ==========================================
def menu_temperaturas(temperaturas):
    while True:
        print("\n" + "="*35)
        print("  PAINEL DE TEMPERATURA DAS CPUs (°C)")
        print("="*35)
        print("1 - Quantidade de sensores")
        print("2 - Média de temperatura")
        print("3 - Menor temperatura registrada")
        print("4 - Maior temperatura registrada")
        print("5 - CPUs em superaquecimento (> 75°C)")
        print("6 - Ver relatório completo de temperatura")
        print("0 - Voltar ao Menu Principal")
        print("="*35)

        opcao = input("Escolha uma opção: ").strip()

        match opcao:
            case "1":
                print(f"\n[+] Sensores monitorados: {temperaturas.size}")
            case "2":
                print(f"\n[+] Temperatura média: {np.mean(temperaturas):.2f}°C")
            case "3":
                print(f"\n[+] Menor temperatura: {np.min(temperaturas)}°C")
            case "4":
                print(f"\n[+] Maior temperatura: {np.max(temperaturas)}°C")
            case "5":
                print("\n===== SUPERAQUECIMENTO (> 75°C) =====")
                aquecidas = False
                for i in range(temperaturas.size):
                    if temperaturas[i] > 75:
                        print(f"CPU {i} com temperatura de {temperaturas[i]}°C [ALERTA]")
                        aquecidas = True
                if not aquecidas:
                    print("Todas as temperaturas estão dentro da faixa segura.")
            case "6":
                print("\n===== RELATÓRIO COMPLETO DE TEMPERATURA =====")
                print("Total de sensores:", temperaturas.size)
                print(f"Temperatura média: {np.mean(temperaturas):.2f}°C")
                print(f"Mais fria: {np.min(temperaturas)}°C")
                print(f"Mais quente: {np.max(temperaturas)}°C")
                print("Acima de 75°C:", temperaturas[temperaturas > 75])
            case "0":
                print("\nVoltando ao Menu Principal...")
                break
            case _:
                print("\n[!] Opção inválida! Digite um número de 0 a 6.")


# ==========================================
# 3. FUNÇÃO: MENU PRINCIPAL DO SISTEMA
# ==========================================
def menu_principal(medicoes_cpu, temperaturas_cpu):
    while True:
        print("\n" + "="*35)
        print("     SISTEMA DE MONITORAMENTO")
        print("="*35)
        print("1 - Painel de Uso de CPU (%)")
        print("2 - Painel de Temperaturas (°C)")
        print("0 - Sair do Sistema")
        print("="*35)

        escolha = input("Selecione o modo: ").strip()

        match escolha:
            case "1":
                menu_servidor(medicoes_cpu)
            case "2":
                menu_temperaturas(temperaturas_cpu)
            case "0":
                print("\nEncerrando o sistema de monitoramento... Até logo!")
                break
            case _:
                print("\n[!] Opção inválida! Escolha 1, 2 ou 0.")


# ==========================================
# 4. DADOS E EXECUÇÃO
# ==========================================
cpus = np.array([30, 43, 55, 67, 76, 89, 90, 93])
temperaturas = np.array([31, 45, 37, 82, 95, 99, 52, 62])

# Inicia o sistema pelo Menu Principal
menu_principal(cpus, temperaturas)