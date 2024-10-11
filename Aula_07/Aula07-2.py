assentos = [[0] * 8 for _ in range(5)]

def reservar_assento(fila, coluna):
    if 0 <= fila < 5 and 0 <= coluna < 8 and assentos[fila][coluna] == 0:
        assentos[fila][coluna] = 1
        return True
    return False

def cancelar_reserva(fila, coluna):
    if 0 <= fila < 5 and 0 <= coluna < 8 and assentos[fila][coluna] == 1:
        assentos[fila][coluna] = 0
        return True
    return False

def exibir_assentos():
    print("Mapa de Assentos:")
    for i, fila in enumerate(assentos):
        print(f"Fila {i + 1}: {' '.join(map(str, fila))}")

reservar_assento(0, 2)
reservar_assento(1, 4)
reservar_assento(3, 6)
cancelar_reserva(1, 4)

exibir_assentos()
