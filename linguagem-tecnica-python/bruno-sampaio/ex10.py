#Script Python para Caixa Eletrônico

#Inicialmente, o usuário começa com R$1.000,00
saldo = 1000

#Foi criado um laço de repetição para continuar exibindo o menu principal após cada interação, até ser acionado break na opção 4
while True:
    print("\n=========SISTEMA BANCÁRIO========= \n=========CAIXA ELETRÔNICO=========\n")
    print("1 - Consultar saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")

    #O usuário interage pelo teclado, digitando uma das 4 operações disponíveis
    operacao = int(input("Digite o número da operação desejada: "))

    if operacao == 1:
        print(f"Saldo atual: R$ {saldo:.2f}")

    elif operacao == 2:
        deposito = float(input("Digite o valor do depósito: "))

        #Se o usuário usar valores menores ou iguais a zero, será alertado e retornará ao menu principal
        if deposito <= 0:
            print("Valor de depósito Inválido!")

        #Somente ao digitar um valor válido, o depósito vai ser aceito e processado, com exibição do novo saldo.
        else:
            saldo += deposito
            print("Depósito realizado com sucesso")
            print(f"Novo saldo: R${saldo:.2f}")

    elif operacao == 3:

        #Se o usuário tentar fazer saque de valor menor que zero, será alertado e retornará ao menu principal.
        saque = float(input("Digite o valor do saque: "))
        if saque <= 0:
            print("Valor de saque inválido!")

        #Se o usuário tentar um valor de saque maior que seu saldo atual, será alertado e retornará ao menu principal.
        elif saque > saldo:
            print("Saldo insuficiente.")
        else:
            saldo -= saque
            print("Saque realizado com sucesso.")
            print(f"Novo saldo: R${saldo:.2f}")

    #Para interromper o laço de repetição do sistema, somente se o usuário acionar a operação 4.
    elif operacao == 4:
        print("Sistema encerrado pelo usuário.")
        break

#Quaisquer outros valores diversos dos disponíveis no menu principal, geram alerta e retornam ao menu principal.
    else:
        print("Opção inválida!")
