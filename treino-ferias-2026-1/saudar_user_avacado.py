def saudar_usuario(nome):
    if nome:
        print(f"Olá, {nome.title()}! Seja bem-vindo ao VS Code!")
    else:
        print("Você precisa informar um nome válido.")


nome_digitado = input("Digite o seu nome: ").strip()

saudar_usuario(nome_digitado)
