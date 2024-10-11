dados = [17, 1.69, "Stella", "Roxo"] 

def exibir_tabela(dados):
    print("| Posição| Dados          |")
    print("|--------|---------------|")
    for i, dado in enumerate(dados):
        print(f"| {i:<6} | {dado:<13} |")

print("Vetor original:")
exibir_tabela(dados)
dados[3] = "Azul"
print("\nVetor atualizado:")
exibir_tabela(dados)