def eh_par(numero):
    
    return numero % 2 == 0

numero_digitado = int(input("Digite um número inteiro: "))

if eh_par(numero_digitado):
    print(f"O número {numero_digitado} é par")
else:
    print(f"O número {numero_digitado} é ímpar")