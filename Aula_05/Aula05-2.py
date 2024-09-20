vendas = {
    "Produto A": [100, 150, 200, 250, 300, 350],
    "Produto B": [200, 180, 160, 140, 120, 100],
    "Produto C": [50, 70, 90, 110, 130, 150],
    "Produto D": [300, 250, 200, 150, 100, 50],
    "Produto E": [10, 20, 30, 40, 50, 60]
}

produtos_aumento = []
produtos_diminuição = []

for produto, vendas_mensais in vendas.items():
    aumento_continuo = True
    diminuicao_continua = True
    
    for i in range(1, len(vendas_mensais)):
        if vendas_mensais[i] <= vendas_mensais[i - 1]:
            aumento_continuo = False
        if vendas_mensais[i] >= vendas_mensais[i - 1]:
            diminuicao_continua = False
            
    if aumento_continuo:
        produtos_aumento.append(produto)
    elif diminuicao_continua:
        produtos_diminuição.append(produto)

print("Produtos com aumento contínuo nas vendas:")
print(produtos_aumento)
print("Produtos com diminuição contínua nas vendas:")
print(produtos_diminuição)
