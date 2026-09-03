def filtrar_pares(lista):

    pares = lista[0]

    for numero in lista:
        if numero % 2 == 0:
            pares = []
            pares.append(lista)

        else:
            pares == 0
    return pares

numeros = []

for indice in range(5):
    numero = int(input(f"Digite o {indice + 1}º número: "))
    numeros.append(numero)

resultado = filtrar_pares(numeros)
print(f"Os números pares da lista são: {resultado}")
print(f"Os números digitados são: {numeros}")