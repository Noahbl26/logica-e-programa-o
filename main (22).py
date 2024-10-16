#controle de consumo de combustivel   n4

consumo = []
for i in range(7):
    while True:
        try:
            cons = int(input(f"Digite o consumo do dia {i+1}:"))
            consumo.append(cons)
            break
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

# Cálculo da média, maior e menor consumo
medio_consumo = sum(consumo) / len(consumo)
maior_consumo = max(consumo)
menor_consumo = min(consumo)

# Contagem de dias com consumo acima da média
dias_acima_media = sum(1 for cons in consumo if cons > medio_consumo)

# Exibição dos resultados
print(f"Média do uso e combustivel: {medio_consumo:.2f}")
print(f"Maior consumo de combustivel: {maior_consumo}mL")
print(f"Menor consumo de combustivel : {menor_consumo}mL")
print(f"Dias com comsumo acima da média: {dias_acima_media}")