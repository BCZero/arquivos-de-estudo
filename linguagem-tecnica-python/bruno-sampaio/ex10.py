# Script Python para Caixa Eletrônico

# Define o saldo inicial da conta bancária
saldo = 1000.00

#Laço de repetição que mantém o sistema em execução até que o usuário escolha sair
while True:

    # Exibe o menu de opções
    print("\n===== CAIXA ELETRÔNICO =====")
    print("1 - Consultar saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")

    # Solicita ao usuário a operação desejada
    operacao = int(input("Digite a operação desejada: "))

    # Opção 1: Consulta de saldo
    if operacao == 1:

        print(f"Saldo atual: R$ {saldo:.2f}")

    # Opção 2: Depósito
    elif operacao == 2:

        # Solicita o valor que será depositado
        deposito = float(input("Digite o valor do depósito: "))

        # Verifica se o valor informado é válido
        if deposito <= 0:
            print("Valor de depósito inválido!")
        # Atualiza o saldo com o valor do depósito
        else:
            saldo += deposito
            print(f"Depósito realizado com sucesso.")
            print(f"Novo saldo: R$ {saldo:.2f}")

    # Opção 3: Saque
    elif operacao == 3:

        # Solicita o valor desejado para saque
        saque = float(input("Digite o valor do saque: "))

        # Verifica se o valor de saque é válido
        if saque <= 0:
            print("Valor de saque inválido!")

        # Verifica se existe saldo suficiente para o saque
        elif saque > saldo:
            print("Saldo insuficiente!")

        # Realiza o saque e atualiza o saldo
        else:
            saldo -= saque
            print("Saque realizado com sucesso.")
            print(f"Novo saldo: R$ {saldo:.2f}")

    # Opção 4: Encerrar o sistema
    elif operacao == 4:

        print("Sistema encerrado pelo usuário.")
        break

    # Trata opções inexistentes no menu
    else:

        print("Opção inválida!")