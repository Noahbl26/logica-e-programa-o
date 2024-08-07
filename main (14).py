departamento=input("digite o seu departamento:D.Sf,D.M,D.R,D.P")
if departamento == "D.Sf":
    recomendacao = "laptops de alto desenpenho"
elif departamento == "D.M":
    recomendacao = "tablets para maior mobilidade"
elif departamento == "D.R":    
    recomendacao = "computadores de desktop"
elif departamento == "D.P":
    recomendacao = "equipamentos com especificações de última geração."
else:
    recomendacao = "departamento desconhecido"

print(recomendacao)
