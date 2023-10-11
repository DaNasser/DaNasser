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


