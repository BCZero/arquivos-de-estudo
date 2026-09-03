numero = int(input("Digite um número para criarmos a tabuada: "))
for multiplicador in range (1,11,1):
    resultado = numero * multiplicador
    print(f"{numero} x {multiplicador} = {resultado}")