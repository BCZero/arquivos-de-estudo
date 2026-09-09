#Script Python de Tabuada

#Inicialmente, o usuário insere um número inteiro
numero = int(input("Digite um número para calcular ver sua tabuada de 1 a 10: "))

#Criamos um laço de repetição com for, que inicia em 1 e termina em 10, armazenando o valor do laço em "i"
for i in range (1, 11, 1):
    print(f"{numero} x {i} = {numero * i}")

#Na f string, número recupera o valor inserido pelo usuário e "i" é aumentado de 1 em 1 a cada laço, até a 10ª repetição.

print("Fim do código.")