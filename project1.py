def soma(a, b):
    result = a + b
    return result

def subtracao(a, b):
    result = a - b
    return result


def multiplicacao(a, b):
    result = a * b
    return result

def divisao(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    result = a / b
    return result

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
        resultado = soma(num1, num2)
        print(f"Resultado: {resultado}")
    elif opcao == '2':
        resultado = subtracao(num1, num2)
        print(f"Resultado: {resultado}")
    elif opcao == '3':
        resultado = multiplicacao(num1, num2)
        print(f"Resultado: {resultado}")
    elif opcao == '4':
        try:
            resultado = divisao(num1, num2)
            print(f"Resultado: {resultado}")
        except ValueError as e:
            print(e)
    else:
        print("Opção inválida. Tente novamente.")