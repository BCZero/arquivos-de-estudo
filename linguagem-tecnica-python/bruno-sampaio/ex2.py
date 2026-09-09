#Script Python de Situação do Aluno

#O usuário deve informar as duas notas
nota1 = float(input("Digite a sua nota 1: "))
nota2 = float(input("Digite a sua nota 2: "))

#O código faz o cálculo matemático da média e armazena em media
media = (nota1 + nota2) / 2

#É realizado uma sequência de comparações entre a média e o requisito
#A situação é armazenada na variável situacao
if media >= 7:
    situacao = "Aprovado"
elif 5 <= media <= 7:
    situacao = "Recuperação"
else:
    situacao = "Recuperação"

#Por fim, o código exibe o valor obtido na média e a situação correspondente
print(f"A média do aluno foi {media} e a situação dele é {situacao}")

print("Fim do código")