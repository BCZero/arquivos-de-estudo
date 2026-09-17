status = ("pago", "pendente", "pago", "cancelado", "pago")

sentinela = False
interacao = input("Digite o status que você está procurando: ")

for i in range(len(status)):
    if status[i] == interacao:
        print(f"{interacao} foi encontrado na posição {i}")
        sentinela = True
if sentinela == False:
    print(f"O valor {interacao} não consta na lista!")