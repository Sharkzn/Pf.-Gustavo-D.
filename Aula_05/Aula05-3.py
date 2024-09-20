vendas_diarias = [
    ("Produto A", 10),
    ("Produto B", 5),
    ("Produto A", 15),
    ("Produto C", 20),
    ("Produto B", 10),
    ("Produto A", 5),
    ("Produto C", 10),
]

totais_vendas = {}
contagem_dias = {}

for produto, venda in vendas_diarias:
    if produto not in totais_vendas:
        totais_vendas[produto] = 0
        contagem_dias[produto] = 0
    totais_vendas[produto] += venda
    contagem_dias[produto] += 1

print("Relatório de Vendas")
print("-------------------")
for produto in totais_vendas:
    total = totais_vendas[produto]
    dias = contagem_dias[produto]
    media = total / dias if dias > 0 else 0
    print(f"{produto}: Total de Vendas = {total}, Média Diária = {media:.2f}")
