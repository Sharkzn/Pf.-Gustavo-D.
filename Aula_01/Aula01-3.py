def tipo_triangulo(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "As medidas devem ser maiores que zero."
    if a + b <= c or a + c <= b or b + c <= a:
        return "As medidas fornecidas não formam um triângulo válido."
    if a == b == c:
        return "O triângulo é equilátero."
    elif a == b or b == c or a == c:
        return "O triângulo é isósceles."
    else:
        return "O triângulo é escaleno."
def main():
    try:
        a = float(input("Digite o comprimento do primeiro lado: "))
        b = float(input("Digite o comprimento do segundo lado: "))
        c = float(input("Digite o comprimento do terceiro lado: "))
        resultado = tipo_triangulo(a, b, c)
        print(resultado)
    except ValueError:
        print("Por favor, digite valores numéricos válidos.")
if __name__ == "__main__":
    main()