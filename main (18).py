#validação de entrada
while True:
    nub =int(input("digite um numero positivo:"))
    if nub >= 0:
        break
    print("numero negativo tente novamente.")
    print(f"numero inserido possitivo:{nub}")