pesos = int(input("What do you have left in pesos ?: "))
soles = int(input("What do you have left in soles ?: "))
reais = int(input("What do you have left in reais ?: "))

pesos_to_usd = float(pesos * 0.00024)
soles_to_usd = float(soles * 0.27)
reais_to_usd = float(reais * 0.18)

total_usd = float(pesos_to_usd + soles_to_usd + reais_to_usd)
print("here dolars you have: ")
print(total_usd)