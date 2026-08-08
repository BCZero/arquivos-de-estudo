def calcular_media(notas):
    if notas == []:
    # Também é usual descrever: if not notas:

        return 0.0

    media_notas = sum(notas) / len(notas)
    return media_notas

print(calcular_media([7.0, 8.0, 6.0]))
print(calcular_media([]))

