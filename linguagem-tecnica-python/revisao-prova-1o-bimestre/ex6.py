soma = 0
aprovadas = 0

for nota in (5, 8, 6):
    soma = soma + nota
    if nota >= 6:
        aprovadas = aprovadas + 1
print(soma, aprovadas)