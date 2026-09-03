notas = []

for i in range(5):
    nota = float(input(f"Digite a {i + 1}ª nota: "))
    notas.append(nota)

def calcular_media(notas):
    if notas == []:
    # Também é usual descrever: if not notas:

        return 0.0

    media_notas = sum(notas) / len(notas)
    return media_notas

resultado = calcular_media(notas)
print(resultado)

if resultado > 7:
    print("O aluno está aprovado!")
elif resultado <= 7:
    print("O aluno está de recuperação")
