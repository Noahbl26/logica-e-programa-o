#jogo da memoria
import random

# Lista de pares de números
elementos = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
random.shuffle(elementos)  # Embaralha os números
ocultos = ['_'] * 10  # Lista que mostra os números ocultos

def mostrar_lista():
    print("Posições: ", list(range(10)))
    print("Valores:   ", ocultos)

# Jogo
while '_' in ocultos:
    mostrar_lista()
    
    # Escolha do primeiro número
    while True:
        try:
            pos1 = int(input("Escolha a primeira posição (0-9): "))
            if 0 <= pos1 <= 9 and ocultos[pos1] == '_':
                break
            else:
                print("Posição inválida ou já revelada. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número entre 0 e 9.")

    ocultos[pos1] = elementos[pos1]
    mostrar_lista()
    
    # Escolha do segundo número
    while True:
        try:
            pos2 = int(input("Escolha a segunda posição (0-9): "))
            if 0 <= pos2 <= 9 and pos2 != pos1 and ocultos[pos2] == '_':
                break
            else:
                print("Posição inválida ou já revelada. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número entre 0 e 9.")

    ocultos[pos2] = elementos[pos2]
    
    # Verificar se formam um par
    if elementos[pos1] == elementos[pos2]:
        print("Par encontrado!")
    else:
        print("Não formam par.")
        ocultos[pos1] = '_'
        ocultos[pos2] = '_'

    mostrar_lista()

print("Você encontrou todos os pares!")

