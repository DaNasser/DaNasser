inicio=int(input("digite um numero de inicio par/impar "))
final=int(input("digite um numero de parada "))
soma=0
if inicio %2 == 0:
    for i in range (inicio,final,2):
        soma = soma+i
        print(soma)
else:
    for i in range (inicio,final,2):
         soma = soma+i
         print(soma)