def pode_acessar(cargo, dia_semana=None):
    dias_uteis = {"segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira"}
    
    cargo = cargo.lower()
    if dia_semana:
        dia_semana = dia_semana.lower()
    
    permissoes = {
        "gerente": True,  
        "analista": dia_semana in dias_uteis if dia_semana else False,  
        "estagiário": dia_semana in dias_uteis if dia_semana else False  
    }

    return permissoes.get(cargo, False)

cargo = input("Digite o cargo do funcionário: ")

if cargo.lower() == "gerente":
    dia_semana = None
else:
    dia_semana = input("Digite o dia da semana: ")

if pode_acessar(cargo, dia_semana):
    print("Acesso Permitido.")
else:
    print("Acesso Negado.")