cisla = [1, 2, 3, 4, 5, 6]
cisla.append(17) #pridavam na konec seznamu 17
cisla.pop(0) #odebere položnu na místě 0 => 1
print(cisla[0]) #položka na nultém indexu => 1

for i in range(len(cisla)): #lem => (length) - délka seznamu
    cisla[i] += 1 # každé číslo zvýším o 1

matice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
# [řádek] [sloupec]

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
