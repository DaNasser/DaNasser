distancia=int(input("digite quantos kilometros andou "))
velocidade=int(input("digite quantos km/h você percorreu esse percurso "))
tempoh=int(distancia/velocidade)
tempom=int(distancia/velocidade)*60%60
print(f"sua viagem demorara {tempoh} horas e {tempom} minutos ") 