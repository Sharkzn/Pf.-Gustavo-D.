vetor = [3, 8, 1, 6, 7]

def exibir_tabela(vetor):
    print("|Posição  | Valor |")
    print("|--------|-------|")
    for i, valor in enumerate(vetor):
        print(f"| {i:<6} | {valor:<5} |")

print("Vetor original:")
exibir_tabela(vetor)
vetor.append(10)

print("\nVetor atualizado:")
exibir_tabela(vetor)