import math

a = int(input("Digite o cateto (a) do triangulo: "))
b = int(input("Digite o cateto (b) do triangulo: "))
x = a * a
y = b * b
h = math.sqrt(x + y)

print(f"A hipetenusa é: {h}")