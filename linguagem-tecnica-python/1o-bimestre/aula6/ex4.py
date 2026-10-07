meses = ("jan", "fev", "mar", "abr", "mai", "jun")

print(meses[:3]) #da posição 0 até 3
print(meses[-2:])
print(meses[::-1])

# explicando:   
#meses[:3]    # do início até antes do índice 3 -> ('jan', 'fev', 'mar')
#meses[-2:]   # do penúltimo até o fim -> ('mai', 'jun')
#meses[::-1]  # inverte toda a tupla -> ('jun', 'mai', 'abr', 'mar', 'fev', 'jan')
