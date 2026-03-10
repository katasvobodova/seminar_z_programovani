a = 0
b = 0
c = 0
z = 0
asks = ["Jak se jmenuje planeta, na které žijeme?", "Když se zamlží okulár nebo čočka jak ho budu čistit?", "Jaké jsou ideální podmínky pro pozorování?", "Jak poznám polárku?", "Na jeké se nacházíme polokouli?", "Jaké existují typy dalekohledů?", "Jak poznáme, kde se sever?", "Jak se jmenuje galaxie, ve které se nacházíme?", "Jak se jmenovala první exoplaneta?", "Kde se nachází největší dalekohled v čr?"]
answers = [["Pluto", " Země", "Mars"], ["ukazováčkem", "nebudu ho čistit", "palcem"], ["Svit měsíce, abychom něco viděli", "Jasná obloha, žádný déšt ani mraky", "Teplo, abychom neumrzli"], ["Podle severu", "Podle velké a malé medvědice", "Podle Andromedy"], ["Jižní", "Severní", "Střední"], ["čočkový", "zrdcadlový", "laserový"], ["Podle polárky", "Podle západu slunce", "Podle stínu stromů"], ["Andromeda", "Sluneční soustava", "Mléčná dráha"], ["Země", "51 Pegasi", "K2-18b"], ["Na petříně", "V Ondřejivě", "Na Štefánikově hvězdárně v Brně"]]
print("1.", asks[0], "a. ", answers[0][0], "b. ", answers[0][1], "c. ", answers[0][2])
answer = (input("enter just a or b or c:"))
if answer == "a":
    a = a+1
elif answer == "b":
    b = b + 1
elif answer == "c":
    c = c + 1
else:
    z = z + 1
print("2.", asks[1], "a. ", answers[1][0], "b. ", answers[1][1], "c. ", answers[1][2])
answer = (input("enter just a or b or c:"))
if answer == "a":
    a = a+1
elif answer == "b":
    b = b + 1
elif answer == "c":
    c = c + 1
else:
    z = z + 1
print("3.", asks[2], "a. ", answers[2][0], "b. ", answers[2][1], "c. ", answers[2][2])
answer = (input("enter just a or b or c:"))
if answer == "a":
    a = a+1
elif answer == "b":
    b = b + 1
elif answer == "c":
    c = c + 1
else:
    z = z + 1
print("4.", asks[3], "a. ", answers[3][0], "b. ", answers[3][1], "c. ", answers[3][2])
answer = (input("enter just a or b or c:"))
if answer == "a":
    a = a+1
elif answer == "b":
    b = b + 1
elif answer == "c":
    c = c + 1
else:
    z = z + 1
print("5.", asks[4], "a. ", answers[4][0], "b. ", answers[4][1], "c. ", answers[4][2])
answer = (input("enter just a or b or c:"))
if answer == "a":
    a = a+1
elif answer == "b":
    b = b + 1
elif answer == "c":
    c = c + 1
else:
    z = z + 1
print("6.", asks[5], "a. ", answers[5][0], "b. ", answers[5][1], "c. ", answers[5][2])
answer = (input("enter just a or b or c:"))
if answer == "a":
    a = a+1
elif answer == "b":
    b = b + 1
elif answer == "c":
    c = c + 1
else:
    z = z + 1
print("7.", asks[6], "a. ", answers[6][0], "b. ", answers[6][1], "c. ", answers[6][2])
answer = (input("enter just a or b or c:"))
if answer == "a":
    a = a+1
elif answer == "b":
    b = b + 1
elif answer == "c":
    c = c + 1
else:
    z = z + 1
print("8.", asks[7], "a. ", answers[7][0], "b. ", answers[7][1], "c. ", answers[7][2])
answer = (input("enter just a or b or c:"))
if answer == "a":
    a = a+1
elif answer == "b":
    b = b + 1
elif answer == "c":
    c = c + 1
else:
    z = z + 1
print("9.", asks[8], "a. ", answers[8][0], "b. ", answers[8][1], "c. ", answers[8][2])
answer = (input("enter just a or b or c:"))
if answer == "a":
    a = a+1
elif answer == "b":
    b = b + 1
elif answer == "c":
    c = c + 1
else:
    z = z + 1
print("10.", asks[9], "a. ", answers[9][0], "b. ", answers[9][1], "c. ", answers[9][2])
answer = (input("enter just a or b or c:"))
if answer == "a":
    a = a+1
elif answer == "b":
    b = b + 1
elif answer == "c":
    c = c + 1
else:
    z = z + 1
if z > 0:
    print("The answer should have been either a b or c. Try again!")
elif a > b or c > b:
    print("You probably won't be an astrophysicist!")
elif b > c or b > a:
    print("Well done!!!!")
else:
    print("There is something wrong, try it agan.")