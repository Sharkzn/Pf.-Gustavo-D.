def ler_nota():
    while True:
        try:
            nota = float(input())
            if 0 <= nota <= 10:
                return nota
            else:
                print("nota inválida")
        except ValueError:
            print("nota inválida")

def main():
    print("Digite a primeira nota:")
    nota1 = ler_nota()
    
    print("Digite a segunda nota:")
    nota2 = ler_nota()
    
    media = (nota1 + nota2) / 2
    print(f"média = {media:.2f}")

if __name__ == "__main__":
    main()
