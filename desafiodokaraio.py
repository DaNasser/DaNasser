def atualizar_cliente(nome,email,telefone):
    if indice >= len(clientes) and indice < len(clientes):
        clientes[indice]['Nome'] = nome
        clientes[indice]['Email'] = email
        clientes[indice]['Telefone'] = telefone

        print("cliente editado com sucesso!")
    else:
        print("Indice invalido. Cliente não encontrado.")

def deletar_cliente(cliente,indice)
    if <= 1 < len(clientes)
    indice=int(input("Digite o seu ID para apagar: "))
    del clientes[indice]

clientes = []