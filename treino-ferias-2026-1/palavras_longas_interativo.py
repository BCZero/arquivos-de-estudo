palavras = []

tamanho_minimo = int(input("Digite o número de letras para filtrar palavras: "))

def contar_palavras_longas(palavras, tamanho_minimo):
    contador = 0

    for palavra in palavras:
        if len(palavra) <= tamanho_minimo:
            contador = contador + 1

    return contador

for indice in range(5):
    palavra = input(f"Digite a {indice + 1}ª palavra: ")
    palavras.append(palavra)



resultado = contar_palavras_longas(palavras, tamanho_minimo)

print(resultado)