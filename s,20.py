#pedido de senha
senha = 1234
tentativa = int(input("insira a sua senha de quatro digitos: "))
while True:
    if senha == tentativa:
        print("a sua senha esta correta")
        break
    else:
        tentativa = int(input("senha incorreta,insira a senha novamente: "))
