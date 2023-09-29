a=int(input("digite 1 numero inteiro"))
b=int(input("digite 1 numero de parada"))
soma=0
if a %2 == 1:
    for i in range(a,b):
        soma=soma+i
        print(soma)
else:
    for i in range(a,b,2):
        soma=soma+i
        print(soma)