participantes = int(input("insira a quantidade de participantes:"))
sala=input("classificacao da sala")
if participantes <= 5:
    print("sala pequena acomodara melhor os participantes")
elif participantes >= 6:
    print("sala media acomodara melhor os participantes")
elif participantes <15:
    print("sala media")
else:
    print("sala grande acomodara melhor os participantes")
