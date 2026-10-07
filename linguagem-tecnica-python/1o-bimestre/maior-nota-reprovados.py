maiorNota = 0
menorNota = 0
qtdReprovado = 0
qtdAprovado = 0

for i in range(0, 5):
    nota = float(input(f"Digite a nota {i+1}: "))
    if i == 0: #fcondição da primeira rodada
        maiorNota=nota
        menorNota=nota
    else:
        if nota > maiorNota:
            maiorNota = nota
        if nota < menorNota:
            menorNota = nota

    #estou fazendo fora do if e do else

    if nota <= 6:
        qtdReprovado += 1
    else:
        qtdAprovado += 1

print(f"Quantidade de aprovados: {qtdAprovado}")
print(f"Quantidade de reprovados: {qtdReprovado}")
print(f"Maior nota: {maiorNota}")
print(f"Menor nota: {menorNota}")