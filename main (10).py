
print("Bem vindo a pizzaria TF")
print("Conheça nosso menu")
print("Pizza - R$ 40,00 cada")
print("Esfiha - R$ 3,00 cada")
print("Refrigerante - R$ 10,00 cada")
print("Suco Natural - R$ 12,00 cada")
print("Se você deseja continuar, digite 1")
print("Se você deseja cancelar, digite 0")  
pedido = int(input())
produto = 0
valor_pedido = 0
qtdpizza = 0
qtdesfiha = 0
qtdrefri = 0
qtdsuco = 0

if pedido == 1:
      while produto != 5:
        print("Inclua o que desejar")
        print("1- Pizza ")
        print("2- Esfiha ")
        print("3- Refrigerante ")
        print("4- Suco Natural ")
        print("5- Finalizar pedido")
        produto = int(input())
        if produto == 1:
          qtdpizza += 1
          valor_pedido += 40
        elif produto == 2:
          qtdesfiha += 1
          valor_pedido += 3
        elif produto == 3:
          qtdrefri += 1
          valor_pedido += 10
        elif produto == 4:
          qtdsuco += 1
          valor_pedido += 12
        elif produto == 5:
          print("Pedido finalizado")
          print("Total de pizzas: ", qtdpizza)
          print("Total de esfihas: ", qtdesfiha)
          print("Total de refrigerantes: ", qtdrefri)
          print("Total de sucos: ", qtdsuco)
          print("Valor total: R$", "%.2f" % valor_pedido)

if pedido == 0:
    print("Obrigado pela sua presença")

