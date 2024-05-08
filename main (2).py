'''
classificação de idade 

'''
idade = int(input("por favor,insira sua idade:"))

if idade <= 12:
    print("Você é uma criança.")
elif 13 <= idade <= 19:
    print("Você é um adolescente.")
elif 20<= idade <= 59:
    print("Você é um adulto.")
else:
    print("Você é um idoso.")