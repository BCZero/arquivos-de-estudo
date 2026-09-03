passwd = "@joker123"

while True:
    senha_digitada = input("Digite a senha para acessar o sistema Jarvis: ")
    if senha_digitada == passwd:
        print("Acesso autorizado.") 
        print("Bem-vindo ao sistema. Aguarde o carregamento do ambiente.")
        break
    
    else:
        print("Senha incorreta. Tente novamente")
