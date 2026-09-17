ev1 = []
ev2 = []

for i in range (0,2):
    print(f"\nCadastro do evento {i + 1}")


    nome_evento = input("Digite o nome do evento: ")

    dia_evento = input("Digite a data do evento: ")

    local_evento = input("Digite o local do evento: ")

evento = [nome_evento, dia_evento, local_evento]

print("\nEventos Cadastrados: ")
print(evento)