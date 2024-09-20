Numero = int(input("Digite o Número de funcionarios: "))
Horas_trabalhadas = int(input("Digite o Número de Horas trabalhadas: "))
Valor_por_hora = float(input("Digite o Pagamento por Hora: "))

salario = Horas_trabalhadas * Valor_por_hora

print(f'Número = {Numero}')
print(f'Salário = R$ {salario:.2f}')