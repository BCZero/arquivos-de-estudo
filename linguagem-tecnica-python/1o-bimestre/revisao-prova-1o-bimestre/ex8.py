#Sintaxe do fatiamento de lista:
# A fatia [início:fim:passo] exclui o índice fim. Quando os extremos ficam fora dos limites, o
#fatiamento é ajustado. Um passo negativo caminha para trás.

#Obs: Por padrão, quando não colocamos o passo, ele vale +1 (ou seja, ele sempre anda da esquerda para a direita).

meses = ("jan", "fev", "mar", "abr", "mai", "jun")
print(meses[:3]) # ('jan', 'fev', 'mar')
print(meses[-2:]) # ('mai', 'jun')
print(meses[::-1]) # tupla na ordem inversa