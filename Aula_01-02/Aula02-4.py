def calcular_imc(peso, altura):
    if altura == 0:
        raise ValueError("A altura não pode ser zero.")
    return peso / (altura ** 2)
def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade grau 1"
    elif 35 <= imc < 39.9:
        return "Obesidade grau 2"
    else:
        return "Obesidade grau 3"
def main():
    try:
        peso = float(input("Informe o peso (kg): "))
        altura = float(input("Informe a altura (m): "))
        imc = calcular_imc(peso, altura)
        classificacao = classificar_imc(imc)
        print(f"Seu IMC é {imc:.2f}. Classificação: {classificacao}.")
    except ValueError as e:
        print(f"Erro: {e}. Por favor, insira valores numéricos válidos.")
if __name__ == "__main__":
    main()