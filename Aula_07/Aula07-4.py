temperaturas = [
    [22, 25, 28, 32],
    [20, 23, 26, 30],
    [18, 22, 25, 29]
]

matriz_transposta = [[temperaturas[j][i] for j in range(len(temperaturas))] for i in range(len(temperaturas[0]))]

print("Matriz Transposta:")
for linha in matriz_transposta:
    print(linha)
