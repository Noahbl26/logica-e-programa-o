#soma de numeros
nub = int(input("digite um numero inteiro positivo: "))
soma_dig = 0
while True:
    soma_dig += nub % 10
    nub //= 10
    if nub == 0:
      break
print(f"soma dos digitos: {soma_dig}")
