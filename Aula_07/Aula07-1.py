estoque = [20, 15, 10, 30, 5]

def atualizar_estoque(estoque, produto, quantidade):
    if 0 <= produto < len(estoque) and estoque[produto] >= quantidade:
        estoque[produto] -= quantidade

def adicionar_estoque(estoque, produto, quantidade):
    if 0 <= produto < len(estoque):
        estoque[produto] += quantidade

def exibir_estoque(estoque):
    print("Estoque atual:", estoque)

atualizar_estoque(estoque, 0, 3)
atualizar_estoque(estoque, 3, 2)
adicionar_estoque(estoque, 4, 10)

exibir_estoque(estoque)
