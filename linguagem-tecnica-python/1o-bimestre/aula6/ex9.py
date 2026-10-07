precos = (100, 120, 40, 30, 50, 134)

#min, max, sum, busca

min(precos)
max(precos)
sum(precos)

print("Com base na lista de preços registrados, seguem as opções de cálculo: \nmin \nmax \nsum")
interacao = input("Digite qual operação você quer realizar: ")

if interacao == min:
    for valor in precos:
        print(min(precos))

elif interacao == max:
    for valor in precos:
        print(max(precos))

elif interacao == sum:
    for valor in precos:
        print(sum(precos))

else:
    print("Opção indisponível")
    print("Programa encerrado. Execute novamente o programa.")