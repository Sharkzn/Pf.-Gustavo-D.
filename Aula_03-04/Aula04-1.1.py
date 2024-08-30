numeros = []
for i in range(10):
    numero = int(input(f"Digite o número {i+1}: "))
    numeros.append(numero)
decimo_numero = numeros[9]
contagem = numeros.count(decimo_numero)
print(f"{decimo_numero} foi lido {contagem} vezes.")
