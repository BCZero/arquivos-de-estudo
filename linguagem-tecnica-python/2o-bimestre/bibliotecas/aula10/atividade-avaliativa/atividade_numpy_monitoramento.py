import numpy as np


def exibir_estrutura(matriz):
    print("\n=== 1. ESTRUTURA DA MATRIZ ===")
    print(f"Dimensões: {matriz.ndim}")
    print(f"Formato: {matriz.shape}")
    print(f"Total de elementos: {matriz.size}")
    print(f"Tipo dos elementos: {matriz.dtype}")
    print(f"Bytes por elemento: {matriz.itemsize}")
    print(f"Total de bytes dos dados: {matriz.nbytes}")
    print(f"São {matriz.shape[0]} linhas, uma por servidor,")
    print(f"e {matriz.shape[1]} colunas, uma por horário.")


def resumo_geral(matriz):
    print("\n=== 2. ESTATÍSTICAS GERAIS ===")
    print(f"Média geral: {np.mean(matriz):.2f}")
    print(f"Menor medição: {np.min(matriz)}")
    print(f"Maior medição: {np.max(matriz)}")
    print(f"Desvio padrão: {np.std(matriz):.2f}")


def analisar_servidores(matriz, servidores):
    print("\n=== 3. ANÁLISE POR SERVIDOR ===")
    medias = np.mean(matriz, axis=1)
    menores = np.min(matriz, axis=1)
    maiores = np.max(matriz, axis=1)
    desvios = np.std(matriz, axis=1)

    for i in range(len(servidores)):
        print(f"\n{servidores[i]}")
        print(f"Média: {medias[i]:.2f}")
        print(f"Menor uso: {menores[i]}")
        print(f"Maior uso: {maiores[i]}")
        print(f"Desvio padrão: {desvios[i]:.2f}")

    return medias


def analisar_horarios(matriz):
    print("\n=== 4. ANÁLISE POR HORÁRIO ===")
    medias = np.mean(matriz, axis=0)
    menores = np.min(matriz, axis=0)
    maiores = np.max(matriz, axis=0)

    for i in range(matriz.shape[1]):
        print(f"\nHorário {i + 1}")
        print(f"Média: {medias[i]:.2f}")
        print(f"Menor valor: {menores[i]}")
        print(f"Maior valor: {maiores[i]}")


def identificar_alertas(matriz, limite):
    print("\n=== 5. IDENTIFICAÇÃO DE ALERTAS ===")
    alertas = matriz >= limite
    print("Matriz booleana:")
    print(alertas)
    print("Medições que atingiram ou ultrapassaram o limite:")
    print(matriz[alertas])
    print(f"Quantidade total de alertas: {np.sum(alertas)}")
    return alertas


def contar_alertas_servidor(alertas, servidores):
    print("\n=== 6. ALERTAS POR SERVIDOR ===")
    quantidades = np.sum(alertas, axis=1)

    for i in range(len(servidores)):
        if quantidades[i] == 1:
            print(f"{servidores[i]}: 1 alerta")
        else:
            print(f"{servidores[i]}: {quantidades[i]} alertas")

    print("Servidores sem alertas:")
    encontrou = False
    for i in range(len(servidores)):
        if quantidades[i] == 0:
            print(servidores[i])
            encontrou = True

    if encontrou == False:
        print("Nenhum.")

    return quantidades


def classificar_servidores(medias, servidores):
    print("\n=== 7. CLASSIFICAÇÃO ===")
    classificacoes = []

    for i in range(len(servidores)):
        if medias[i] < 60:
            classificacao = "Normal"
        elif medias[i] < 75:
            classificacao = "Atenção"
        else:
            classificacao = "Crítico"

        classificacoes.append(classificacao)
        print(f"{servidores[i]}: {medias[i]:.2f} - {classificacao}")

    return classificacoes


def identificar_maior_media(medias, servidores, quantidades, classificacoes):
    print("\n=== 8. SERVIDOR COM MAIOR MÉDIA ===")
    maior_media = medias[0]
    posicao_maior = 0

    for i in range(1, len(medias)):
        if medias[i] > maior_media:
            maior_media = medias[i]
            posicao_maior = i

    print(f"Servidor: {servidores[posicao_maior]}")
    print(f"Média: {maior_media:.2f}")
    print(f"Alertas: {quantidades[posicao_maior]}")
    print(f"Classificação: {classificacoes[posicao_maior]}")
    return posicao_maior


def simular_melhoria(matriz, limite, servidores):
    print("\n=== 9. SIMULAÇÃO DE MELHORIA ===")
    # Operação vetorizada: cria outra matriz, preservando a original.
    matriz_otimizada = matriz * 0.88
    media_antes = np.mean(matriz)
    media_depois = np.mean(matriz_otimizada)
    alertas_antes = np.sum(matriz >= limite)
    alertas_depois = np.sum(matriz_otimizada >= limite)
    reducao = media_antes - media_depois

    print(f"Média antes: {media_antes:.2f}")
    print(f"Média depois: {media_depois:.2f}")
    print(f"Alertas antes: {alertas_antes}")
    print(f"Alertas depois: {alertas_depois}")
    print(f"Redução da média: {reducao:.2f} pontos percentuais")

    medias_otimizadas = np.mean(matriz_otimizada, axis=1)
    criticos_otimizados = []
    print("Servidores ainda classificados como Crítico:")
    for i in range(len(servidores)):
        if medias_otimizadas[i] >= 75:
            criticos_otimizados.append(servidores[i])
            print(f"{servidores[i]}: média {medias_otimizadas[i]:.2f}")

    if len(criticos_otimizados) == 0:
        print("Nenhum.")

    return matriz_otimizada, criticos_otimizados


def gerar_relatorio(matriz, matriz_otimizada, limite, servidores,
                    medias, classificacoes, posicao_maior,
                    criticos_otimizados):
    print("\n=== 10. RELATÓRIO FINAL ===")
    media_antes = np.mean(matriz)
    media_depois = np.mean(matriz_otimizada)
    alertas_antes = np.sum(matriz >= limite)
    alertas_depois = np.sum(matriz_otimizada >= limite)

    print(f"Limite informado: {limite:.2f}")
    print(f"Média geral: {media_antes:.2f}")
    print(f"Maior medição: {np.max(matriz)}")
    print(f"Menor medição: {np.min(matriz)}")
    print(f"Quantidade total de alertas: {alertas_antes}")
    print(f"Servidor com maior média: {servidores[posicao_maior]}")
    print(f"Maior média: {medias[posicao_maior]:.2f}")

    print("Servidores classificados como críticos:")
    encontrou = False
    for i in range(len(servidores)):
        if classificacoes[i] == "Crítico":
            print(servidores[i])
            encontrou = True
    if encontrou == False:
        print("Nenhum.")

    print("Resultado da otimização de 12%:")
    print(f"Média: {media_antes:.2f} -> {media_depois:.2f}")
    print(f"Alertas: {alertas_antes} -> {alertas_depois}")
    print(f"Redução da média: {media_antes - media_depois:.2f} pontos percentuais")
    print("Servidores que permaneceram críticos:")
    for i in range(len(criticos_otimizados)):
        print(criticos_otimizados[i])
    if len(criticos_otimizados) == 0:
        print("Nenhum.")


# DADOS E EXECUÇÃO DO PROGRAMA

dados_cpu = [
    [42, 55, 61, 78, 84, 73, 68, 59],
    [35, 40, 38, 45, 50, 48, 44, 41],
    [70, 76, 82, 91, 88, 79, 85, 90],
    [55, 60, 58, 62, 67, 72, 69, 65],
    [80, 83, 79, 86, 92, 95, 89, 87]
]

servidores = [
    "Servidor A", "Servidor B", "Servidor C",
    "Servidor D", "Servidor E"
]

matriz = np.array(dados_cpu)

exibir_estrutura(matriz)
resumo_geral(matriz)
medias = analisar_servidores(matriz, servidores)
analisar_horarios(matriz)

limite = float(input("\nInforme o limite crítico: "))
alertas = identificar_alertas(matriz, limite)
quantidades = contar_alertas_servidor(alertas, servidores)
classificacoes = classificar_servidores(medias, servidores)

posicao_maior = identificar_maior_media(
    medias, servidores, quantidades, classificacoes
)

matriz_otimizada, criticos_otimizados = simular_melhoria(
    matriz, limite, servidores
)

gerar_relatorio(
    matriz, matriz_otimizada, limite, servidores,
    medias, classificacoes, posicao_maior, criticos_otimizados
)

# DESAFIO DE INTERPRETAÇÃO
# Os números abaixo foram obtidos executando o programa.
# Para os exemplos de alertas, foi usado o limite 80, salvo indicação contrária.
#
# 1. O Servidor E exige maior atenção, pois possui a maior média de uso.
# 2. Sua média é 86,38% (arredondada) e seu maior uso é 95%.
# 3. A quantidade de servidores em alerta depende do limite escolhido.
#    Com limite 80, A, C e E apresentam alertas: três servidores.
#    Em outra execução, com limite 90, apenas C e E apresentam alertas: dois.
#    Esse limite não modifica a classificação por média, cujas faixas são fixas.
# 4. Não. Com limite 80, a otimização reduz os alertas de 13 para 3,
#    mas o Servidor E permanece Crítico, com média otimizada de 76,01%.
# 5. Não. O Servidor A tem média 65,00%, abaixo da faixa Crítico,
#    mas apresenta uma medição de 84%, que gera alerta com limite 80.
#    A média pode ocultar picos; é preciso analisar também as medições individuais.
