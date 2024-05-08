'''
determina que  tipo de triangulo é
'''
lado1=int(input("insira o primeiro lado:"))
lado2=int(input("insira o segundo lado:"))
lado3=int(input("insira o terceiro lado:"))

if lado1 ==lado2 and lado1==lado3:
    print("seu triangulo e equilatero")
elif lado1 != lado2 and lado1 != lado3:
    print("seu triangulo é escaleno")
else:
    print("seu triangulo é isóseles")