lista = []
for i in range(11):
    num = int(input("Digite um numero: "))
    lista.append(num)


biggerNumber = max(lista)
lista.remove(biggerNumber)
secondBiggerNumber = max(lista)

print(biggerNumber)
print(secondBiggerNumber)