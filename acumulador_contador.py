total = 0
contador = 0

while contador < 5:
    numero = int(input("Digite um número: "))
    if numero < 0:
        break

    total = total + numero
    contador = contador + 1   

print("O total acumulado é: ", total)

    
print("Número negativo informado. Encerrando a soma.")