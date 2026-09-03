def contar_palavras_longas(palavras, tamanho_minimo):
    contador = 0

    for palavra in palavras:
        if len(palavra) > tamanho_minimo:
            contador = contador + 1

    return contador

resultado = contar_palavras_longas(
    ["sol", "banana", "nau", "casa", "computador"], 
    4
)

print(resultado)