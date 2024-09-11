# tabuada de um a cem

nub=int(input("insira o numero:"))
cont= 1
while True:
    cont = cont + 1
    result = nub * cont 
    print(f"{nub}x{cont}= {result}")
    if cont == 10:
         break
     