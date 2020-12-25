def rightAngle(a,b,c):
    a = a ** 2
    b = b ** 2
    c = c ** 2

    if max(a,b,c) == (a + b + c - max(a,b,c)):
        print("The given lengths form Right Angle Triangle")
    else:
        print("Not a Right angle triangle")

a = int(input("enter side of triangle"))
b = int(input("enter side of triangle"))
c = int(input("enter side of triangle"))

rightAngle(a,b,c)
