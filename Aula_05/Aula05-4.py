inventario = []

quantidade_itens = int(input("Quantos itens você deseja adicionar ao inventário? "))

for i in range(quantidade_itens):
    print(f"\nItem {i + 1}:")
    nome = input("Nome do equipamento: ")
    categoria = input("Categoria do equipamento: ")
    quantidade = int(input("Quantidade: "))
    
    item = {
        "nome": nome,
        "categoria": categoria,
        "quantidade": quantidade
    }
    inventario.append(item)

print("\nInventário Completo:")
print("---------------------")
for item in inventario:
    print(f"Nome: {item['nome']}, Categoria: {item['categoria']}, Quantidade: {item['quantidade']}")
