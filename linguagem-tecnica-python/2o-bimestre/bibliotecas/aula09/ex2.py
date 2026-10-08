import numpy as np

lista = [5, 10, 15, 20]
lista_array = np.array(lista, dtype=np.int32)

print(lista)
print(lista_array)

print(type(lista))
print(type(lista_array))

print("Qual é o tipo: ", lista_array.dtype)