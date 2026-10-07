# Tupla de preços
precos = (100, 120, 40, 30, 50, 134)

# Menu de opções
print("Com base na lista de preços registrados, seguem as opções de cálculo:")
print("min - Menor preço")
print("max - Maior preço")
print("sum - Soma dos preços")

# Entrada do usuário
interacao = input("Digite qual operação você quer realizar: ").lower()

# Estruturas de decisão
if interacao == "min":
    print(f"\nMenor preço encontrado: R$ {min(precos)}")

elif interacao == "max":
    print(f"\nMaior preço encontrado: R$ {max(precos)}")

elif interacao == "sum":
    print(f"\nSoma total dos preços: R$ {sum(precos)}")

else:
    print("\nOpção indisponível.")
    print("Programa encerrado. Execute novamente o programa.")