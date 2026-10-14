import numpy as np

def menu_servidor(medicoes):
    while True:
        print("\n" + "="*30)
        print("     PAINEL DO SERVIDOR")
        print("="*30)
        print("1 - Quantidade de CPUs")
        print("2 - Média de gastos no servidor")
        print("3 - CPU com mais folga (uso mínimo)")
        print("4 - CPU com menos folga (uso máximo)")
        print("5 - Listar CPUs críticas (> 80%)")
        print("6 - Ver relatório completo")
        print("0 - Sair")
        print("="*30)

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
                print("\n===== RELATÓRIO COMPLETO =====")
                print("Quantidade de amostras:", medicoes.size)
                print(f"Média das amostras: {np.mean(medicoes):.2f}%")
                print("CPU com mais folga:", np.min(medicoes), "%")
                print("CPU com menos folga:", np.max(medicoes), "%")
                print("CPUs críticas:", medicoes[medicoes > 80])
            case "0":
                print("\nEncerrando o programa... Até logo!")
                break
            case _:
                print("\n[!] Opção inválida! Digite um número de 0 a 6.")


# DADOS E EXECUÇÃO
cpus = np.array([30, 43, 55, 67, 76, 89, 90, 93])
menu_servidor(cpus)