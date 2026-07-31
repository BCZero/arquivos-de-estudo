def encontrar_maior(lista):

    maior = lista[0]

    for numero in lista:
        if numero > maior:
            maior = numero

    return maior

numeros = []

for indice in range(5):
    numero = int(input(f"Digite o {indice + 1}º número: "))
    numeros.append(numero)

resultado = encontrar_maior(numeros)
print(f"O maior número da lista é: {resultado}")