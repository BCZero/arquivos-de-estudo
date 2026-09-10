#Script Python de Controle de Acesso

#Inicialmente, estabelecemos a senha "", apenas para ter um parâmetro
senha = ""

#criamos um loop de repetição, em que enquanto a variável senha for diferente de "python123",
#O script fica pedindo para o usuário informar a senha
while senha != "python123":
    senha = input("Digite a senha: ")

#Encerra quando a senha correta é inserida
print("Acesso permitido!")