'''
determina que  tipo de triangulo é
'''
N1=int(input("insira o primeiro número:"))
N2=int(input("insira o segundo número:"))
N3=int(input("insira o terceiro número:"))

if N1 > N2 and N1 > N3:
    print(f"{N1} é o maior número")
elif N2 > N1 and N2 > N3:
    print(f"{N2} é o maior número")
else:
    print(f"{N3} é o maior número")