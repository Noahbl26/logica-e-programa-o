#analise de batimentos cardiacos  n5
batimentos = []
for i in range(7):
    while True:
        try:
            card = int(input(f"Digite a quantidade de batimentos do dia {i+1}:"))
            batimentos.append(card)
            break
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

medio_card = sum(batimentos) / len(batimentos)
maior_card = max(batimentos)
menor_card = min(batimentos)


dias_acima_media = sum(1 for card in batimentos if card > medio_card)

# Exibição dos resultados
print(f"Média de batimentos cardiaco: {medio_card}")
print(f"Maior numero de batimentos cardiacos: {maior_card}")
print(f"Menor numero de batimentos cardiacos : {menor_card}")
print(f"Dias com batimentos cardiacos acima da media: {dias_acima_media}")