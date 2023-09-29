a=int(input("digite um numero "))
o=str(input("escolha sua operação +,-,/,*: "))
if o=='+':
    for b in range(1,11):
        print(a+b)
elif o=='-':
    for b in range(1,11):
        print(a-b)
elif o=='/':
    for b in range(1,11):
        print(a/b)
else:
    for b in range(1,11):
        print(a*b)