from collections import Counter

F = [4, 7, 9, 4, 2, 4, 7]
contagem_4 = F.count(4)
contagem = Counter(F)
numero_mais_frequente = contagem.most_common(1)[0] 
print("O número 4 aparece:", contagem_4, "vezes.")
print("O número que aparece mais vezes é:", numero_mais_frequente[0], "com", numero_mais_frequente[1], "vezes.")