#ax^2 + bx + c = 0
a = int(input("enter vatue on place a"))
b = int(input("enter vatue on place b"))
c = int(input("enter vatue on place c"))
if a == 0 and b == 0 and c == 0:
    print("x = Solution of this equation is every value of x")
elif a == 0 and b == 0:
    print("It has no solution")
elif a == 0 and c == 0:
    print("x = 0")
elif b == 0 and c == 0:
    print("x = 0")
elif a== 0:
    print(x = -c/b)
elif b == 0 and c >=0 and a >=0:
    print("It has no solution")
elif b == 0 and c <=0 and a <=0:
    print("It has no solution")
elif b == 0 and c >=0 and a <=0:
    print(x = (-c/a)**(1/2))
elif b == 0 and c <=0 and a >=0:
    print(x = (-c/a)**(1/2))
elif c == 0:
    print(Xx = 0, Xy = -b/a)
else :
    if b**2 >= (4*a*c):
        print(xx = (-b+(b**2-4*a*c)**(1/2))/2/a, xy = (-b-(b**2-4*a*c)**(1/2))/2/a)
    else:
        print("It has no solution")



    