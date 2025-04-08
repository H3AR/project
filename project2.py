produtos = {
    'Nome': [],
    'Valor': [],
    'Quantidade': []
}

def cadastrar_produto():
    nome = input("Digite o nome do produto: ")
    valor = float(input("Digite o valor do produto: "))
    quantidade = int(input("Digite a quantidade do produto: "))

    produtos['Nome'].append(nome)
    produtos['Valor'].append(valor)
    produtos['Quantidade'].append(quantidade)

def remover_produto():
    nome = input("Digite o nome do produto que deseja remover: ")
    if nome in produtos['Nome']:
        index = produtos['Nome'].index(nome)
        del produtos['Nome'][index]
        del produtos['Valor'][index]
        del produtos['Quantidade'][index]
        print(f"Produto {nome} removido com sucesso.")
    else:
        print(f"Produto {nome} não encontrado.")

def listar_produtos():
    if not produtos['Nome']:
        print("Nenhum produto cadastrado.")
    else:
        print("Lista de produtos:")
        for i in range(len(produtos['Nome'])):
            print(f"Nome: {produtos['Nome'][i]}, Valor: {produtos['Valor'][i]}, Quantidade: {produtos['Quantidade'][i]}")

def buscar_produto():
    nome = input("Digite o nome do produto que deseja buscar: ")
    if nome in produtos['Nome']:
        index = produtos['Nome'].index(nome)
        print(f"Produto encontrado: Nome: {produtos['Nome'][index]}, Valor: {produtos['Valor'][index]}, Quantidade: {produtos['Quantidade'][index]}")
    else:
        print(f"Produto {nome} não encontrado.")

while True:
    print("Sistema de Controle de Estoque")
    print("1. Cadastrar produto")
    print("2. Remover produto")
    print("3. Listar produtos")
    print("4. Buscar produto")
    print("5. Sair")

    opcao = input("Escolha uma opção (1-5): ")
    if opcao == '5':
        print("Saindo do sistema.")
        break
    elif opcao == '1':
        cadastrar_produto()
    elif opcao == '2':
        remover_produto()
    elif opcao == '3':
        listar_produtos()
    elif opcao == '4':
        buscar_produto()
    else:
        print("Opção inválida. Tente novamente.")