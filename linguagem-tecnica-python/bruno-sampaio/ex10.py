# Script Python para Caixa Eletrônico

# Inicialmente, o usuário começa com R$ 1.000,00.
saldo = 1000.00

# Laço de repetição para manter o sistema em execução até o usuário sair.
while True:
    print("\n========= SISTEMA BANCÁRIO =========")
    print("========= CAIXA ELETRÔNICO =========\n")
    print("1 - Consultar saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")

    # Usuário escolhe a operação desejada.
    operacao = int(input("Digite o número da operação desejada: "))

    if operacao == 1:
        print(f"Saldo atual: R$ {saldo:.2f}")

    elif operacao == 2:
        deposito = float(input("Digite o valor do depósito: "))

        if deposito <= 0:
            print("Valor de depósito inválido!")
        else:
            saldo += deposito
            print("Depósito realizado com sucesso.")
            print(f"Novo saldo: R$ {saldo:.2f}")

    elif operacao == 3:
        saque = float(input("Digite o valor do saque: "))

        if saque <= 0:
            print("Valor de saque inválido!")
        elif saque > saldo:
            print("Saldo insuficiente.")
        else:
            saldo -= saque
            print("Saque realizado com sucesso.")
            print(f"Novo saldo: R$ {saldo:.2f}")

    elif operacao == 4:
        print("Sistema encerrado pelo usuário.")
        break

    else:
        print("Opção inválida!")
