#Script Análise de números

#Primeiro, criamos os contadores por tipo, que iniciam zerados
positivos = 0
negativos = 0
zeros = 0
pares = 0
impares = 0

#Então fazemos um laço de repetição de 1 a 10, para o usuário digitar o número desejado
for i in range(1, 11):
    numero = int(input(f"Digite dez números. Digite o {i}º número: "))

    #Então, as regras abaixo classificam em positivos, negativo ou zero
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        zeros += 1

    #Por fim, há ainda a classificação de par ou ímpar
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print("\n=== RESULTADO ===")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")
print(f"Zeros: {zeros}")
print(f"Pares: {pares}")
print(f"Ímpares: {impares}")
print("Fim do código")