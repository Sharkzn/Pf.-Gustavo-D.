vendas_mensais = [120, 130, 140, 150, 160, 170, 160, 150, 140, 130, 120, 110]

total_vendas = sum(vendas_mensais)

media_vendas = total_vendas / len(vendas_mensais)

max_venda = max(vendas_mensais)
mes_max_venda = vendas_mensais.index(max_venda) + 1 

print(f"Total de vendas no ano: {total_vendas}")
print(f"Média mensal de vendas: {media_vendas:.2f}")
print(f"Mês com a máxima venda: Mês {mes_max_venda} com {max_venda} unidades vendidas.")
