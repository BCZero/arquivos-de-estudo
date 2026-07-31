def encontrar_maior(lista):

    maior = lista[0]

    for numero in lista:
        if numero > maior:
            maior = numero

    return maior

numeros = [7, 2, 15, 4, 9]
resultado = encontrar_maior(numeros)
print(resultado)