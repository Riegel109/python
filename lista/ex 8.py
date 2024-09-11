x = []
moreThan90Kg = 0
adultAndLighterThan60Kg = 0
between10and30YearsOld = 0
ageSum = 0

for i in range(3):
    print(f"Pessoa n° {i+1}")
    personAge = int(input("Insira a idade da pessoa:"))
    personWeight = float(input("Insira o peso da pessoa:"))
    x.append({ "age": personAge, "weight": personWeight })
    print("-----")

for person in x:
    if person["age"] > 90:
        moreThan90Kg += 1

    if person["age"] >= 18 and person["weight"] < 60:
        adultAndLighterThan60Kg += 1

    if person["age"] >= 10 and person["age"] <= 30:
        between10and30YearsOld += 1

    ageSum += person["age"]

x = (100 / 3) * between10and30YearsOld

print(f"Média idade: {ageSum / 3:.2f}")
print(f"Mais de 90: {moreThan90Kg}")
print(f"Naior de idade e menor que 60kg: {adultAndLighterThan60Kg}")
print(f"Porcentagem de pessoas com idade entre 10 e 30 anos: {x:.2f}")



