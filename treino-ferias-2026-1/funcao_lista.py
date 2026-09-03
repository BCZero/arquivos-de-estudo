#Nesse código, usamos a função calular_media para modificar uma lista

def calcular_media(lista):
    return sum(lista) / len(lista)
    #A função soma todos os itens da lista e depois divide o resultado
    #pela quantidade de itens dessa lista, isto é, calcula uma média

notas = [8, 9, 10, 7]
#A partir daqui, criamos uma variável notas que é uma lista

media = calcular_media(notas)
#A variável media chama a função calcular_media, aplicando sua estrutura para a lista notas

print(media)

#O print vai imprimir o cáclulo do calcular_media aplicado a lista notas