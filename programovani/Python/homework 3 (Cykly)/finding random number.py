import random
n = random.randrange(1,101)
y = int(input("enter your tip to mistery number:"))
while y != n:
    if n == y:
        print("nice job, you have it")
    elif n<y:
        print("reduce your tip")
        y = int(input("enter your tip to mistery number:"))
    else:
        print("scale up your tip")
        y = int(input("enter your tip to mistery number:"))