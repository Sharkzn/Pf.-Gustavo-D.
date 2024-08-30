def e_vogal(caractere):
    return caractere.lower() in 'aeiou'
caracteres = []
print("Digite as letras:")
for i in range(5):
    caractere = input(f"{i + 1}: ")
    caracteres.append(caractere)
vogais = []
posicoes = []
for i, caractere in enumerate(caracteres):
    if e_vogal(caractere):
        vogais.append(caractere)
        posicoes.append(i + 1)
num_vogais = len(vogais)
if num_vogais > 0:
    print(f"Foram lidas {num_vogais} vogais.")
    print(f"As vogais estão nas posições: {', '.join(map(str, posicoes))}.")
else:
    print("Foram lidas 0 vogais.")
    print("Não há vogais no vetor.")
