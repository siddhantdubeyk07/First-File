a,b=int(input("Enter first number")),int(input("Enter second number"))
c,d,e,f,="+","-","*","/"
g=input("Enter operation")
if (g==c):
    print(a+b)
elif(g==d):
    print(a-b)
elif(g==e):
    print(a*b)
elif (g==f):
    print(a/b)
else: print("Error")