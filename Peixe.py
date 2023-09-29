peso=int(input("quantos kilos você pescou? "))
Multa=(peso-50)*4

if peso<50:
    print("não tem multa na pesca ")
else:
    print(f"sua multa foi de ",Multa)