D = [12, 18, 5, 24, 7]
posicao_24 = D.index(24) if 24 in D else None
valor_proximo = min(D, key=lambda x: abs(x - 10))
print("Posição do número 24:", posicao_24)
print("Valor mais próximo de 10:", valor_proximo)