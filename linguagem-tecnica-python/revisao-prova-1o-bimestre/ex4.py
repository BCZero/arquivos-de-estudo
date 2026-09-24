#Calcule 2 + 3 * 4, (2 + 3) * 4, 11 // 3, 11 % 3 e 2 ** 3.

calculos_lista = [
    2 + 3 * 4,
    (2 + 3) * 4,
    11 // 3,
    11 % 3,
    2 ** 3
]

for indice, resultado in enumerate(calculos_lista, start=1):
    print(f"calc{indice} = {resultado}")