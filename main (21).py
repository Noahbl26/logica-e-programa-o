#controle de consumo de agua  n3
consumo = []
for i in range(7):
    while True:
        try:
            cons = int(input(f"Digite o consumo do dia {i+1}: "))
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
print(f"Média das vendas: {medio_consumo:.2f}")
print(f"Maior venda: {maior_consumo}")
print(f"Menor venda: {menor_consumo}")
print(f"Dias com vendas acima da média: {dias_acima_media}")