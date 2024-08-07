funcionario=(input("insira o seu cargo:"))
dia=(input("insira o dia da semana:"))

if funcionario == 'analista' or funcionario == 'gerente': 
      print("acesso permitido")
elif funcionario == 'estagiario':
    if dia == 'sabado' or dia == 'domingo':
        print("acesso negado")
    else:
        print("acesso permitido")