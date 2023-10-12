def atualizar_produtos(produtos,nome,valor,quantidade,,imp1,imp2,imp3,frete,lucro,indice):
    if 0 <= indice < len(produtos)
        produtos[indice]['Nome'] = nome
        produtos[indice]['Valor'] = valor
        produtos[indice]['Quantidade'] = quantidade
        produtos[indice]['Imposto1'] = imp1
        produtos[indice]['Imposto2'] = imp2
        produtos[indice]['Imposto3'] = imp3
        produtos[indice]['Frete'] = frete
        produtos[indice]['Lucro'] = lucro
        print("Produto editado com sucesso!")
    else:
        print("Indice invalido. Cliente não encontrado.")

def excluir_produto(produtos,indice):
    if 0 <= indice < len(produtos):
        del produtos[indice]
        print("Cliente deletado com sucesso!")
        print("****************************")
        print("\n")

def mudar_quantidade(produtos,indice):
    if 0 <= indice <= len(produtos):
        print(f"Nome do produto: {produtos[indice]['Nome']}")
        print(f"Quantidade: {produtos[indice]['Quantidade']}")

        if a == '1':
            produtos[indice]['Quantidade'] = produtos[indice]['Quantidade'] + int(input("Digite o quantidade que deseja acrescentar: "))
        elif s == '2':
            produtos[indice]['Quantidade'] = produtos[indice]['Quantidade'] - int(input("Digite o quantidade que deseja diminuir: "))
        print("Quantidade atualizado com sucesso!")
        print(f"____________________")
        print("\n")
    else:
        print("Produto não encontrado")
