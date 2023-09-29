numero1=float(input("digite um numero "))
maior_numero = numero1
for i in range(1,5):
    numero=float(input("digite um numero "))
    if numero> maior_numero:
        maior_numero = numero
print(f"maior numero é {maior_numero}")