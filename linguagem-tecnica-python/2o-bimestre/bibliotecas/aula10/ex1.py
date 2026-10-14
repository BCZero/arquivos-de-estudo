#numpy
import numpy as np

#Criando a função
def analisar_servidor(medicoes):
    print("Quantidade de amostras:", medicoes.size)
    print("Média das amostras:", np.mean(medicoes))
    print("CPU com mais folga: ", np.min(medicoes))
    print("CPU com menos folga:", np.max(medicoes))
    cpus_criticas = medicoes[medicoes > 80]
    print("=====CPUs CRÍTICAS=====")
    print(cpus_criticas)
    for i in range(medicoes.size):
        if medicoes[i] > 80:
            print(f"CPU {i} com processamento {medicoes[i]}%")

#CHAMADA DE FUNÇÕES
cpus= np.array([30, 43, 55, 67, 76, 89, 90, 93])
analisar_servidor(cpus)
