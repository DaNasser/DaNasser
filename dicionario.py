def cadastrar_cliente(clientes,nome,email,telefone):
    cliente ={
        'Nome': nome,
        'Email': email,
        'Telefone': telefone
    }
    clientes.append(cliente)
    print("Cliente cadastrado com sucesso!")
    print("***********************************")
    print("\n")

def imprimir_clientes(clientes):

    for i,cliente in enumerate(clientes):
        print(f"ID cliente {i+1}")
        print(f"Nome: {cliente['Nome']}")
        print(f"Email: {cliente['Email']}")
        print(f"Telefone: {cliente['Telefone']}")
        print("***********************************")
        print("\n")

clientes = []
nome = input("Digite o nome: ")
email = input("Digite o email: ")
telefone = input("Digite o telefone: ")
cadastrar_cliente(clientes,nome,email,telefone)
imprimir_clientes(clientes)