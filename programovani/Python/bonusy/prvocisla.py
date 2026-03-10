#prvocisla :>
i = 2
n = int(input("enter n:"))
prvocisla = []
while n > 1:
    if(n % i == 0): #číslo n je dělitelné číslem i
        prvocisla.append(i) #přidáme do seznamu prvočísla
        n = n // i
    else:
        i += 1
print(prvocisla)
text = " * ".join(map(str, prvocisla))
print(text)