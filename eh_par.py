def filtrar_impares(numeros):

    impares = []

    for numero in numeros:
        if numero % 2 != 0:
            impares.append(numero)

    return impares


def filtrar_pares(numeros):

    pares = []

    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)

    return pares

numeros = []

for numero in range(8):

    numero = int(input("Digite um número inteiro: "))

    numeros.append(numero)

print("A lista digitada foi: ", numeros)

resultado_impares = filtrar_impares(numeros)
print(resultado_impares)

resultado_pares = filtrar_pares(numeros)
print(resultado_pares)