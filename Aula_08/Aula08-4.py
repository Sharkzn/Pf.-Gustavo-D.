import random

def criar_tabuleiro():
    tabuleiro = [[1 for _ in range(3)] for _ in range(3)]
    zero_x, zero_y = random.randint(0, 2), random.randint(0, 2)
    tabuleiro[zero_x][zero_y] = 0  # Coloca o zero
    return tabuleiro

def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(' '.join('1' for _ in linha)) 

def jogar():
    tabuleiro = criar_tabuleiro()
    tentativas = 0

    while True:
        imprimir_tabuleiro(tabuleiro)
        try:
            x = int(input("Escolha uma linha (0-2): "))
            y = int(input("Escolha uma coluna (0-2): "))
            tentativas += 1

            if tabuleiro[x][y] == 0:
                print(f"Parabéns! Você encontrou o zero em {tentativas} tentativas!")
                break
            else:
                print("Não há zero aqui. Tente novamente!")
        except (IndexError, ValueError):
            print("Entrada inválida. Por favor, insira índices entre 0 e 2.")

if __name__ == "__main__":
    jogar()
