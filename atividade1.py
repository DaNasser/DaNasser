numero=[]
impar=[]
par=[]

for a in range(10):
    num = int(input("Digite um numero "))
    numero.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

        print("numeros digitados",numero)
        print("vetor PAR", par)
        print("vetor impar", impar)       