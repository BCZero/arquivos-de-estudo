#Script Python para Sistema de Compras

#Inicialmente, o sistema inicia com total zerado.
valor_total_compra = 0

#O sistema usará a letra "S" para que o usuário continue inserindo novos itens
continuar = "S"

#Foi criado um laço de repetição, em que enquanto o usuário inserir "S" serão exibidas mensagens de adicionar itens ao carrinho
while continuar.upper() == "S":

    #O usuário informa o nome do produto, sua quantidade e valor unitário
    produto = input("Digite o nome do produto comprado: ")
    quantidade = int(input("Digite a quantidade do produto escolhido: "))
    preco_unit = float(input("Digite o preço unitário do produto escolhido: "))

    #Cálculos matemáticos para definir o valores por produto e esse valor é acrescentado ao valor total 
    valor_produto = (quantidade * preco_unit)
    valor_total_compra += valor_produto

    print(f"\nProduto: {produto}")
    print(f"Quantidade: {quantidade}")
    print(f"Preço unitário do produto: R$ {preco_unit:.2f}")
    print(f"Total do produto: R$ {valor_produto:.2f}\n")

    continuar = input("Deseja cadastrar outro porudo na compra? (S/N): ")

print(f"\n Valor total da compra: R$ {valor_total_compra:.2f}")