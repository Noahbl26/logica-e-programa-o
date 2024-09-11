#menu 
while True:
    print("\nMenu")
    print("1.somar")
    print("2.subtrair")
    print("3.sair")
    opcao = int(input("escolhaq uma opcao: "))
    if opcao == 1:
        a=int(input("digite o primeiro numero:"))
        b=int(input("digite o segundo numero: "))
        print(f"resultado da soma: {a + b}")
    elif opcao == 2:
        c=int(input("digite o primeiro numero: "))
        d=int(input("digite o segundo numero: "))
        print(f"resultado da subtração: {c - d}")
    elif opcao == 3:
        print("saindo do programa.....")
    else:
        print("opção invalida tente novamente")
