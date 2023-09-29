habitantes1=int(input("digite sua população do primeiro país "))
habitantes2=int(input("digite sua população do segundo país "))
taxa_crescimento1=float(input("Digite a '%' de crescimento do primeiro país "))
taxa_crescimento2=float(input("Digite a '%' de crescimento do segundo país "))
anos=0 

while habitantes1<habitantes2:
    habitantes1 = habitantes1*(1+taxa_crescimento1/100)
    habitantes2 = habitantes2*(1+taxa_crescimento2/100)
    anos = anos+1 
    
    print(anos ,"anos")
    