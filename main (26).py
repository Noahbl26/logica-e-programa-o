#analise de dados de temperatura
# """"""temperaturas = []
for i in range(7):
    while True:
        try:
            temp = float(input(f"Digite a temperatura do dia {i+1}: "))
            temperaturas.append(temp)
            break
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

# Cálculo da média, maior e menor temperatura
media_temp = sum(temperaturas) / len(temperaturas)
maior_temp = max(temperaturas)
menor_temp = min(temperaturas)

# Contagem de dias com temperatura acima da média
dias_acima_media = sum(1 for temp in temperaturas if temp > media_temp)

# Exibição dos resultados
print(f"Média das temperaturas: {media_temp:.2f}°C")
print(f"Maior temperatura: {maior_temp}°C")
print(f"Menor temperatura: {menor_temp}°C")
print(f"Dias com temperatura acima da média: {dias_acima_media}")"""