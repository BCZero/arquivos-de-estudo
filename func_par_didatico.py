def eh_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

numero_digitado = int(input("Digite um número inteiro: "))

if eh_par(numero_digitado):
    print(f"O número {numero_digitado} é par")
else:
    print(f"O número {numero_digitado} é ímpar")