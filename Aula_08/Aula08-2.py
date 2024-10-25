import random

def create_board():
    board = [[0]*3 for _ in range(3)]
    board[random.randint(0, 2)][random.randint(0, 2)] = 1
    return board

def play_game():
    board = create_board()
    attempts = 0

    print("Bem-vindo ao jogo 'Encontre o Tesouro'!")
    while True:
        try:
            row, col = map(int, input("Escolha uma célula (linha coluna): ").split())
            if board[row][col] == 1:
                attempts += 1
                print(f"Parabéns! Você encontrou o tesouro em {attempts} tentativas.")
                break
            else:
                attempts += 1
                print("Não há tesouro. Tente novamente!")
        except (ValueError, IndexError):
            print("Entrada inválida. Use índices de 0 a 2.")

if __name__ == "__main__":
    play_game()
