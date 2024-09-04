C = int(input("Digite seu capital inicial: "))
i = int(input("Digite a taxa de juros (em porcentagem): "))
t = int(input("Digite o tempo que ira deixar (em anos): "))

z= i / 100

M = C + (C * z * t)
print(f"O montante final é: {M}")