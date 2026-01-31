password,attempt=int(),0
while password!=1234 and attempt!=3:
    password = int(input("Enter Password : "))
    attempt = attempt+1
    if password==1234 and attempt <=3:
        print("Access Granted!!")
    elif password!=1234 and attempt < 3:
        print("Wrong Password")
    else:
        print("You enter Wrong Password too many times. Try after 10 minutes")