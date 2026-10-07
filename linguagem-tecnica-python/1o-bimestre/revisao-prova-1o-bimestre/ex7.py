# Lista de notas/valores para testar (incluindo negativos para ilustrar o aviso da apostila)
notas = [-5, -2, -10, -1]

# Variáveis que receberão o maior e o menor
maior = 0
menor = 0

print("--- INÍCIO DO LAÇO ---")

for i in range(len(notas)):
    nota = notas[i]
    print(f"\nRodada i = {i} | Nota atual: {nota}")

    # Na 1ª rodada (quando i == 0): inicializa maior e menor com a primeira nota lida
    if i == 0:
        maior = menor = nota
        print(f"-> Primeira rodada: definindo maior = {maior} e menor = {menor}")
    else:
        # Nas próximas rodadas (i > 0): compara com os valores já armazenados
        if nota > maior:
            maior = nota
            print(f"-> Encontrou novo maior: {maior}")
            
        if nota < menor:
            menor = nota
            print(f"-> Encontrou novo menor: {menor}")

print("\n--- RESULTADO FINAL ---")
print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")