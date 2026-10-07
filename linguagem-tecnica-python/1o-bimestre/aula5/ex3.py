numeros = [10, 20, 30, 40, 50]

print(numeros[-20:20])
#leia(mumeros[-n:m])

#Nesse exerício, o que aconte:
#O python reconhece números negativos no índice como contar a lista de trás pra frente, partindo do elemento 0 e seguindo a partir do último elemento.
#Se não houver tantos elementos na lista como o -n conta, a contagem inicia no elemento 0. Segue a regra de contar a partir do último
#Ocorre que, se m for maior que a quantidade de elementos da lista, a lista toda é exibida.

print(numeros[::3])
print(numeros[::-3])