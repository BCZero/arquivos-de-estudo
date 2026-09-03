total = 0

while True:
    numero = int(input("Digite um número: "))
    if numero < 0:
        break

    total = total + numero  

print("O total acumulado é: ", total)

    
print("Número negativo informado. Encerrando a soma.")