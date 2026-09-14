# Script Python para Sistema de Compras

# Inicialmente, o sistema inicia com total zerado.
valor_total_compra = 0

# O sistema usará a letra "S" para continuar inserindo novos itens.
continuar = "S"

# Loop para cadastrar produtos até o usuário decidir encerrar.
while continuar.upper() == "S":
    produto = input("Digite o nome do produto comprado: ")
    quantidade = int(input("Digite a quantidade do produto escolhido: "))
    preco_unit = float(input("Digite o preço unitário do produto escolhido: "))

    # Cálculo do valor do produto e somatório ao total da compra.
    valor_produto = quantidade * preco_unit
    valor_total_compra += valor_produto

    print(f"\nProduto: {produto}")
    print(f"Quantidade: {quantidade}")
    print(f"Preço unitário do produto: R$ {preco_unit:.2f}")
    print(f"Total do produto: R$ {valor_produto:.2f}\n")

    continuar = input("Deseja cadastrar outro produto na compra? (S/N): ")

print(f"\nValor total da compra: R$ {valor_total_compra:.2f}")
