# Script Python para Sistema de Compras

#inicialmente, valor total é zerado
valor_total_compra = 0

#Foi criado a variável continuar, acionada pela string "S", que o usuário insere após cada produto
#Se quiser cadastrando novos itens
continuar = "S"

#Início do loop de repetição: enquanto o usuário finalizar um item inserindo "S", abre nova chamada
#para cadastrar outro produto
while continuar.upper() == "S":

    produto = input("Digite o nome do produto comprado: ")
    quantidade = int(input("Digite a quantidade do produto escolhido: "))
    preco_unit = float(input("Digite o preço unitário do produto escolhido: "))

    #A cada produto, é feito o cálculo matemático do produto, cujo total é acrescido do total da compra
    valor_produto = quantidade * preco_unit
    valor_total_compra += valor_produto

    #Exibições para o usuário ver o que foi cadastrado em um loop
    print(f"\nProduto: {produto}")
    print(f"Quantidade: {quantidade}")
    print(f"Preço unitário: R$ {preco_unit:.2f}")
    print(f"Total do produto: R$ {valor_produto:.2f}\n")

    #Chamada para o usuário decidir se quer adicionar outro item ou finalizar
    continuar = input("Deseja cadastrar outro produto? (S/N): ")

#Encerrado o loop, o sistema apresenta o total da compra e encerra.
print(f"\nValor total da compra: R$ {valor_total_compra:.2f}")