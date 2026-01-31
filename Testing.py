password=int(input("Enter password to use the programe : "))
a=0
while a==0:
    while password!=1234:
        if password!=1234:
            print("wrong Password, Access Denied!!")
            print("Enter Correct Password")
            password=int(input("Password : "))
        else: break
    print("Access Granted!!")
    print("Which Programme you want to access?")
    print("1.Check whether a number is positive, negative or neither positive nor negative" )
    print("2.Triangle")
    print("3.Square")
    print("4.Rectangle")
    print("5.Cube")
    print("6.Cuboid")
    print("7.Cone")
    print("8.Circle")
    print("9.Quadratic roots")
    a=int(input("kindly choose any one of the give programs: "))
    if a==1:
        x=int(input("Enter any integer : "))
        if x>0:
            print("It is a positive number")
            print("Programe completed")
            a=int(input(("Enter 0 to go back to access programe page or just press enter key to end programme : ")))
        elif x<0:
            print("It is a negative number")
            print("Programe completed")
            a=int(input(("Enter 0 to go back to access programe page or just press enter key to end programme : ")))
        else:
            print("It is neither positive nor negative")
            print("Programe completed")
            a=int(input(("Enter 0 to go back to access programe page or just press enter key to end programme : ")))
    elif a==2:
        x=int(input("Lenths of first side: "))
        y=int(input("Length of second side: "))
        z=int(input("Length of third side: "))
        if x+y>z and x+z>y and y+z>x:
            sp=(x+y+z)/2
            print("Area of the triangle is: ",(sp*(sp-x)*(sp-y)*(sp-z))**(1/2))
            print("Perimeter of the triangle is: ",sp*2)
            if x==y and y==z:
                print("It is an Equilateral Traingle")
                print("Programe completed")
                a=int(input(("Enter 0 to go back to access programe page or just press enter key to end programme : ")))
            elif x==y or y==z or x==z:
                print("It is an Isosceleous Triangle")
                print("Programe completed")
                a=int(input(("Enter 0 to go back to access programe page or just press enter key to end programme : ")))
            elif x**2==y**2+z**2 or y**2==x**2+z**2 or z**2==y**2+x**2:    
                print("It is a Right angle triangle")
                print("Programe completed")
                a=int(input(("Enter 0 to go back to access programe page or just press enter key to end programme : ")))
            else:
                print("It is an scalene traingle.")    
                print("Programe completed")
                a=int(input(("Enter 0 to go back to access programe page or just press enter key to end programme : ")))
        else:
            print("It is not a triangle.")
            print("Programe completed")
            a=int(input(("Enter 0 to go back to access programe page or just press enter key to end programme : ")))
    elif a==3:
        x=int(input("Enter the side of Square : "))
        print("Area of the square is : ",a**2)
        print("Perimeter of the Square is : ", 4*a)     
        print("Programe completed")
        a=int(input(("Enter 0 to go back to access programe page or just press enter key to end programme : ")))

    elif a==4:
        x=int(input("Enter the first side of Rectangle : "))
        y=int(input("Enter the second side of Rectangle : "))
        print("The area of rectangle is : ",x*y)
        print("The perimeter of rectangle is : ",2*(x+y))
        print("Programe completed")
        a=int(input(("Enter 0 to go back to access programe page or just press enter key to end programme : ")))
    elif a==5:
        x=int(input("Enter the side of cube : "))
        print("Total surface area of cube is : ",6*x)
        print("Curved surface area of cube is : ",4*x)
        print("Volume of the cube is : ",x**3)
        print("Programe completed")
        a=int(input(("Enter 0 to go back to access programe page or just press enter key to end programme : ")))
    elif a==6:
        x=int(input("Enter length of cube : "))
        y=int(input("Enter width of the cuboid : "))
        z=int(input("Enter height of the cuboid : "))
        print("Curved surface area of cuboid is : ", 2*((y*z)+(x*z)))
        print("Total surface area of cuboid is : ",2(x*y+y*z+x*z))
        print("Volume of cuboid is : ",x*y*z)
        print("Programe completed")
        a=int(input(("Enter 0 to go back to access programe page or just press enter key to end programme : ")))
    elif a==7:
        x=int(input("Enter radius of cone : "))
        y=int(input("Enter height of cone : "))
        print("Curved surface area of cone is : ",(22/7)*x*((x**2+y**2)**(1/2)) )
        print("Total surface area of cone is : ",(((22/7)*x*((x**2+y**2)**(1/2)))+(22/7)*x**2))
        print("Volume of cone is : ",(((22/7)*x**2)*y)/3)
        print("Programe completed")
        a=int(input(("Enter 0 to go back to access programe page or just press enter key to end programme : ")))
    elif a==8:
        x=int(input("Enter radius of circle : "))
        print("Perimeter of circle is : ",2*(22/7)*x)
        print("Area of circle is : ",(22*7)*x**2)
        print("Programe completed")
        a=int(input(("Enter 0 to go back to access programe page or just press enter key to end programme : ")))
    elif a==9:
        a=int(input("Enter the value of coefficiant of x^2 : "))
        b=int(input("Enter the value of coefficiant of x : "))
        c=int(input("Enter the value of constant term : "))
        d=b**2-4*a*c
        if d<0:
            print("No roots")
            print("Programe completed")
            a=int(input(("Enter 0 to go back to access programe page or just press enter key to end programme : ")))
        elif d==0:
            print("Common roots i.e. : ", -b/(2*a))
            print("Programe completed")
            a=int(input(("Enter 0 to go back to access programe page or just press enter key to end programme : ")))
        else:
            print ("The roots are : ",((-b+d)/(2*a))**(1/2)," and ", ((-b-d)/(2*a))**(1/2))
            print("Programe completed")
            a=int(input(("Enter 0 to go back to access programe page or just press enter key to end programme : ")))        
    else:
        print("Wrong Input")
        a=int(input(("Enter 0 to go back to access programe page or just press enter key to end programme : ")))