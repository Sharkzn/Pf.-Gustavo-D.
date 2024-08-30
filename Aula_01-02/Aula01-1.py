nome = input("Digite o seu nome: ")
sexo = input("Digite seu sexo (m para masculino e f para feminino): ")

if sexo == 'm':
    saudacao = "Bom dia senhor"
elif sexo == 'f':
    saudacao = "Bom dia senhora"
else:
    saudacao = "Bom dia"

print(f"{saudacao} {nome}")