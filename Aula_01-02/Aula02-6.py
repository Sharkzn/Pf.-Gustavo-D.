def pode_doar_sangue():
    idade = int(input("Qual é a sua idade? "))
    if idade < 19 or idade > 69:
        print("Você não pode doar sangue porque a idade deve estar entre 19 e 69 anos.")
        return
    peso = float(input("Qual é o seu peso em kg? "))
    if peso < 50:
        print("Você não pode doar sangue porque o peso deve ser ao menos 50 kg.")
        return
    tatuagem = input("Você fez alguma tatuagem no último ano? (sim/não) ").strip().lower()
    if tatuagem == "sim":
        print("Você não pode doar sangue porque não é permitido ter feito tatuagens no último ano.")
        return
    alcool = input("Você ingeriu álcool nas últimas 12 horas? (sim/não) ").strip().lower()
    if alcool == "sim":
        print("Você não pode doar sangue porque não é permitido ter ingerido álcool nas últimas 12 horas.")
        return
    print("Parabéns! Você pode doar sangue.")
if __name__ == "__main__":
    pode_doar_sangue()