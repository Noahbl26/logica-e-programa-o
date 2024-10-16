# Coleta de notas do usuário
notas = []
quantidade = int(input("Quantas notas deseja inserir? "))

if quantidade <= 0:
    print("A quantidade de notas deve ser maior que zero.")
else:
    for i in range(quantidade):
        while True:
            try:
                nota = float(input(f"Digite a nota {i+1} (0 a 10): "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("A nota deve estar entre 0 e 10. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")

    # Cálculo da média, maior e menor nota
    media = sum(notas) / len(notas)
    maior_nota = max(notas)
    menor_nota = min(notas)

    # Exibição dos resultados
    print(f"\nMédia das notas: {media:.2f}")
    print(f"Maior nota: {maior_nota}")
    print(f"Menor nota: {menor_nota}")
    