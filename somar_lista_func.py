def somar_lista(lista):
    total = 0

    for numero in lista:
        total = total + numero

    return total

lista_1 = [2, 4, 6]
lista_2 = [10, 20, 30, 40]
lista_3 = [-5, 10, 3]

resultado = somar_lista(lista_3)
print(resultado)