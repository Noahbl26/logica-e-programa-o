print("Calculadora Simples")

# Menu de operações
acao = ""

while acao != "sair":
    print("\nEscolha a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    acao = input("Digite o número da operação desejada (1/2/3/4/5): ")

    if acao in ["1", "2", "3", "4"]:
        # Solicita os números ao usuário
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))

        if acao == "1":
            resultado = numero1 + numero2
            print(f"Resultado da adição: {resultado}")
        elif acao == "2":
            resultado = numero1 - numero2
            print(f"Resultado da subtração: {resultado}")
        elif acao == "3":
            resultado = numero1 * numero2
            print(f"Resultado da multiplicação: {resultado}")
        elif acao == "4":
            if numero2 != 0:
                resultado = numero1 / numero2
                print(f"Resultado da divisão: {resultado}")
            else:
                print("Erro: Divisão por zero não é permitida.")
    elif acao == "5":
        print("Saindo...")
    else:
        print("Opção inválida. Tente novamente.")
