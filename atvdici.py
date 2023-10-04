produtos = []
def cadastrar_produto(produtos,nome,valor,quantidade,frete,imposto1,imposto2,imposto3,custo,venda):
    produto ={
        'Nome': nome,
        'Valor': valor,
        'Quantidade': quantidade,
        'Frete': frete,
        'Imposto1': imposto1,
        'Imposto2': imposto2,
        'Imposto3': imposto3,
        'Custo': custo,
        'Valor': valor
    }
    while True:
            
        print("Menu:")
        print("Cadastrar produtos  1")
        print("Imprimir produto  2")
        print("Finalizar progama  3")
        a=str(input("digite sua ação: "))
            
        if a == "1":
    
            nome=str(input("Digite nome do produto que quer cadastrar: "))
            valor=float(input("Digite o valor do seu produto: "))
            quantidade=int(input("Digite a quantidade de produtos que quer cadastrar: "))
            imposto1=float(input("Digite a quantidade do primeiro imposto do seu produto: "))   
            imposto2=float(input("Digite a quantidade do segundo imposto do seu produto: ")) 
            imposto3=float(input("Digite a quantidade do terceira imposto do seu produto: ")) 
            frete=float(input("Digite o frete do seu produto: "))
            custo=float(input("Digite o custo do seu produto: "))
            venda=float(input("Digite a margem de lucro: "))
            print("produto cadastrado")

            imposto1 = (valor*imposto1)/ 100
            imposto2 = (valor*imposto2)/ 100
            imposto3 = (valor*imposto3)/ 100
            frete = frete/quantidade
            custo = valor + imposto1 + imposto2 + imposto3 + frete
            venda = custo + (custo * (ganho / 100))

            nome_produto.append(nome)
            valor_quantidade.append(quantidade)
            valor_imposto1.append(imposto1) 
            valor_imposto2.append(imposto2) 
            valor_imposto3.append(imposto3)
            valor_frete.append(frete)
            valor_custo.append(custo)
            valor_venda.append(valor)

        elif a == "2" :

            def imprimir_produtos(produtos):

                for i,produto in enumerate(produtos):
                    print(f"ID cliente {i+1}")
                    print(f"Nome: {produtos['Nome']}")
                    print(f"Valor: {produtos['valor']}")
                    print(f"Quantidade: {produto['quantidade']}")
                    print(f"Frete: {produtos['frete']}")
                    print(f"Imposto 1: {produtos['imposto1']}")
                    print(f"Imposto 2: {produtos['imposto2']}")
                    print(f"Imposto 3: {produtos['imposto3']}")
                    print(f"Custo: {produtos['custo']}")
                    print(f"Venda: {produtos['venda']}")
                    print("***********************************")
                    print("\n")


    else:
        print("encerando progama")
    break