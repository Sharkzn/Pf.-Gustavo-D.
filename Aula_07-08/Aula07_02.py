def aprovar_ferias(tempo_servico, mes):
    temporada_alta = ['dezembro', 'janeiro', 'fevereiro']
    
    if tempo_servico >= 3:
        return "Pedido de férias aprovado."
    
    if mes.lower() in temporada_alta:
        return "Pedido de férias negado. Funcionários novos não podem tirar férias durante a temporada alta."
    
    return "Pedido de férias aprovado."

tempo_servico = float(input("Digite o tempo de serviço em anos: "))
mes = input("Digite o mês desejado para as férias: ")
print(aprovar_ferias(tempo_servico, mes))