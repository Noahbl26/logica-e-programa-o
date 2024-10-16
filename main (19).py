#controle de vendas 0.2   n1
vendas = []
for i in range(7):
    while True:
        try:
            vend = int(input(f"Digite a venda do dia {i+1}: "))
            vendas.append(vend)
            break
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

# Cálculo da média, maior e menor temperatura
media_vend = sum(vendas) / len(vendas)
maior_vend = max(vendas)
menor_vend = min(vendas)

# Contagem de dias com temperatura acima da média
dias_acima_media = sum(1 for vend in vendas if vend > media_vend)

# Exibição dos resultados
print(f"Média das vendas: {media_vend:.2f}")
print(f"Maior venda: {maior_vend}")
print(f"Menor venda: {menor_vend}")
print(f"Dias com vendas acima da média: {dias_acima_media}")