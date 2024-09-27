Nomes = [
    "Stella",
    "Richard",
    "Kaio",
    "Sabina",
    "Moisés",
    "Daniel",
    "William"
    ]

def exibir_tabela(Nomes):
    print("|Posição | Nome   |")
    print("|--------|--------|")
    for i, nome in enumerate(Nomes):
        print(f"| {i:<6} | {nome:<6} |")

print("Vetor original:")
exibir_tabela(Nomes)
Nomes[2] = "William"
print("\nVetor atualizado:")
exibir_tabela(Nomes)