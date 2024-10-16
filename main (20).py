#monitoramento de velocidae de carros n2
velocidade= []
for i in range(10):
    while True:
        try:
            km = int(input(f"Digite a velocidade do carro {i+1}: "))
            velocidade.append(km)
            break
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

# Cálculo da média, maior e menor temperatura
media_veloc = 80 
maior_veloc = max(velocidade)
menor_veloc = min(velocidade)

# Contagem de dias com temperatura acima da média
velocidade_acima_media = sum(1 for km in velocidade if km > media_veloc)

# Exibição dos resultados
print(f"Média das velocidade: {media_veloc:.2f}km/h")
print(f"Maior velocidade: {maior_veloc}km/h")
print(f"Menor velocidade: {menor_veloc}km/h")
print(f"carros com velocidade acima da média: {velocidade_acima_media}")