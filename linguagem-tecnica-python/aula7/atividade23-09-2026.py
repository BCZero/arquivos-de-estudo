listaAlunos = []

while True:
    # O dicionário é criado aqui dentro para ser um novo registro a cada volta
    aluno = {}
    
    chave = input("Digite o nome: ")
    valor = input("Digite o curso: ")
    
    aluno["nome"] = chave
    aluno["curso"] = valor
    
    listaAlunos.append(aluno)
    
    # Pergunta se o usuário deseja continuar
    continuar = input("Deseja continuar adicionando? (s/n): ").strip().lower()
    
    if continuar == 'n':
        print("\nEncerrando cadastros...")
        break

# Exibindo o resultado final para conferência
print("\nLista de Alunos cadastrados:")
for a in listaAlunos:
    print(f"Nome: {a['nome']} | Curso: {a['curso']}")