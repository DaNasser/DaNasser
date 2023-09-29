salario=float(input("digite quanto você ganha por hora "))
horas=float(input("quantas horas trabalhou no mês "))
salariomensal=salario*horas
impos=salariomensal*0.11
inss=salariomensal*0.08
sind=salariomensal*0.05
print(f"seu salario bruto é {salariomensal}")
print(f"você ira pagar {impos} de imposto de renda")
print(f"você ira pagar {inss} ao INSS")
print(f"você ira pagar {sind} ao Sindicato")
saldo=salariomensal-impos-inss-sind
print ("seu salario liquido é", saldo)