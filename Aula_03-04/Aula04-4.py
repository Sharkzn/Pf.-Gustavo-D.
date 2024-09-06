numeros = [float(input(f"Digite o número {i+1}: ")) for i in range(10)]
pos1 = int(input("Escolha uma posição: ")) - 1
pos2 = int(input("Escolha outra posição: ")) - 1
if 0 <= pos1 < 10 and 0 <= pos2 < 10:
    num1, num2 = numeros[pos1], numeros[pos2]
    print(f"{num1} + {num2} = {num1 + num2}")
    print(f"{num1} - {num2} = {num1 - num2}")
    print(f"{num1} * {num2} = {num1 * num2}")
    print(f"{num1} / {num2} = {num1 / num2 if num2 != 0 else 'Inf (divisão por zero)'}")
    print(f"{num1} ** {num2} = {num1 ** num2}")
else:
    print("Posições inválidas. As posições devem estar entre 1 e 10.")
