count = int(input("Enter a number : "))
while count>0 and count<=100:
  print(count)
  count=count-1

password=""
while password != "Python@123":
  password = input("Enter Password : ")
  if password != "Python@123":
    print("Wrong Password")
  else: print("Access is granted!!") 

number=int(input("Enter a number : "))
while number != 1:
    if number % 2 == 0:
       number = number/2
    else: number = number*3+1
print (number)

def Mean(data):
    total = sum(data)
    n = len (data)
    mean = total/n
    return print (mean)
A=[10,20,30,40,50]
Mean(A)

a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(a is b)
print(a is c)
print(a == b)
