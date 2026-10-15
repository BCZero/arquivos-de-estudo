import pandas as pd

dados = {
    "produto": ["mouse", "teclado", "monitor"],
    "quantidade": [10, 5, 3],
    "preco_unitario": [80.0, 150.0, 900.0]
}

tabela = pd.DataFrame(dados)
print(tabela)