nome_produto=[]
valor_venda=[]
valor_quantidade=[]
valor_imposto1=[]
valor_imposto2=[]
valor_imposto3=[]
valor_frete=[]
valor_custo=[]
valor_ganho=[]

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
        ganho=float(input("Digite a margem de lucro: "))
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
        valor_venda.append(valor)

    elif a == "2" :

        for i in range(len(nome_produto)):
            print(f"Produto: {nome_produto}")
            print(f"valor da venda: R${valor_venda}")
            print(f"Quantidade: {valor_quantidade}")
            print(f"primeiro imposto {valor_imposto1}")
            print(f"Segundo imposto {valor_imposto2}")
            print(f"Terceiro imposto {valor_imposto3}")
            print(f"preco final {valor_venda}")

    elif a == "3":
        print("encerando progama")
        break
else:
        print("ação não encontrada digite novamente")
