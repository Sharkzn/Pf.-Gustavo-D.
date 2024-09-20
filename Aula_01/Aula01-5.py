def precisa_abastecer(km_por_litro, litros_atual, distancia_desejada):
    litros_necessarios = distancia_desejada / km_por_litro  
    if litros_necessarios > litros_atual:
        litros_para_abastecer = litros_necessarios - litros_atual
        return True, litros_para_abastecer
    else:
        return False, 0
def main():
    km_por_litro = float(input("Quantos quilômetros o carro faz por litro? "))
    litros_atual = float(input("Quantos litros de gasolina há no momento? "))
    distancia_desejada = float(input("Qual distância você deseja percorrer (em quilômetros)? "))
    precisa, litros_para_abastecer = precisa_abastecer(km_por_litro, litros_atual, distancia_desejada)
    if precisa:
        print(f"Você precisa abastecer {litros_para_abastecer:.2f} litros de gasolina.")
    else:
        print("Você não precisa abastecer o carro. Há gasolina suficiente.")
if __name__ == "__main__":
    main()