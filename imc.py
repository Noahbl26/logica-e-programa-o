'''
determina qual é o triangulo
'''
altura=float(input())
peso=float(input())
imc = peso/altura**2


if imc < 16.0:
    print("magreza grau III")
elif imc >16.0 and imc <16.9:
    print("magraza de grau II")
elif imc >17.0 and imc <18.4:
    print("magreza grau I")
elif imc >18.4 and imc <24.9:
    print("saudavel")
elif imc >25.0 and imc <29.9:
    print("pré-peso")
elif imc >30.0 and imc <34.29:
    print("obesidade grau I")
elif imc >35.0 and imc < 39.9:
    print("obesidade grau II")
else:
    print("obesidade grau III")
