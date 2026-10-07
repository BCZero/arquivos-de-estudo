#Script Python Soma dos números

#Inicialmente, criamos a variável "soma", cujo valor inicial é zero
soma = 0

#Criamos então o laço de repetição, que vai de 1 a 100
#Esse laço interage com a variável soma: a cada volta, "soma" é acrescentado
#do valor de "i" + o valor soma da volta anterior, ex: 0 + 1 = 1; 1 + 2 = 3; 3 + 3 = 6 etc. 
for i in range(1, 101):
    soma += i

#Por fim, o código exibe o resultado da última volta (100ª volta) que é somatório de todas as 100 voltas!
print(f"A some dos números de 1 a 100 é {soma}")
print("Fim do código.")