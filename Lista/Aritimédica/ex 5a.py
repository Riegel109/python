x = int(input("escolha um numero: "))
y = int(input("escolha outro numero: "))
opcao = ''
while opcao != "5":
    print("1. 'soma'")
    print("2. 'subtração'")
    print("3. 'multiplacação'")
    print("4. 'divisão'")
    print("5. sair")

    opcao = input("Escolha a operação desejada: ")

    if opcao == "1":
        print(f"O resultado é: {x + y}")
    elif opcao == '2':
        print(f"O resultado é: {x - y}")
    elif opcao == '3':
        print(f"O resultado é: {x * y}")
    elif opcao == '4':
        print(f"O resultado é: {x / y}")
    elif opcao == '5':
        print("saindo.")
    else:
        print("Operação não encontarda.")