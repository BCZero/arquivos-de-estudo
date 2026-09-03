for i in range(0, 5):
    nome = input(f"Digite o nome do aluno {i+1}: ")
    nota_aluno = float(input(f"Digite a nota do aluno {i+1}: "))

    if nota_aluno >= 6:
        print(f"O aluno {i+1} foi aprovado")
    else:
        print(f"O aluno {i+1} foi reprovado")