while True:
    print("Calculadora")
    print("1. Somar")  
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Sair")

    opcao = input("Escolha uma opção (1-5): ")
    if opcao == '5':
        print("Saindo da calculadora.")
        break
    if opcao not in ['1', '2', '3', '4']:
        print("Opção inválida. Tente novamente.")
        continue
    
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Entrada inválida. Por favor, insira números válidos.")
        continue

    if opcao == '1':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif opcao == '2':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif opcao == '3':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif opcao == '4':
        if num2 == 0:
            print("Erro: Divisão por zero não é permitida.")
        else:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
    else:
        print("Opção inválida. Tente novamente.")