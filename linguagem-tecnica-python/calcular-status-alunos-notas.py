
for i in range (0, 2):
    aluno = input(f"Digite o {i+1} nome do aluno: ")
    nota_1 = float(input(f"Digite a primeira nota do aluno: "))
    nota_2 = float(input(f"Digite a segunda nota do aluno: "))


media = (nota_1 + nota_2) / 2

if media > 6:
    print(f"O aluno {aluno} teve média {media} e foi aprovado!")
else:
    print(f"O aluno {aluno} teve média {media} e foi reprovado!")