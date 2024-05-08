'''
calcula ano bissexto

'''
ano = int (input("por favor,insira o ano: "))

if (ano % 4==0) and (ano % 100 != 0):
    print(f"{ano} È um ano bissexto.")
elif ano % 400 ==0:
    print(f"{ano} é um  bissexto")
else:
    print(f"{ano} não é um ano bissexto.")