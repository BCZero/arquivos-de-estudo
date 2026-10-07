saldo = 1000.0
while True:
    opcao = input("1: saldo | 2: sair: ")
    if opcao == "1":
        print(f"R$ {saldo:.2f}")
    elif opcao == "2":
        break # encerra o laço
    else:
        print("Opção inválida")