asks = [
    "Jak se jmenuje planeta, na které žijeme?", 
    "Když se zamlží okulár nebo čočka jak ho budu čistit?", 
    "Jaké jsou ideální podmínky pro pozorování?", 
    "Jak poznám polárku?", 
    "Na jaké se nacházíme polokouli?", 
    "Jaké existují typy dalekohledů?", 
    "Jak poznáme, kde se sever?", 
    "Jak se jmenuje galaxie, ve které se nacházíme?", 
    "Jak se jmenovala první exoplaneta?", 
    "Kde se nachází největší dalekohled v ČR?"
]
answers = [
    ["Pluto", "Země", "Mars"],
    ["ukazováčkem", "nebudu ho čistit", "palcem"],
    ["Svit měsíce, abychom něco viděli", "Jasná obloha, žádný déšt ani mraky", "Teplo, abychom neumrzli"],
    ["Podle severu", "Podle velké a malé medvědice", "Podle Andromedy"],
    ["Jižní", "Severní", "Střední"],
    ["čočkový", "zrdcadlový", "laserový"],
    ["Podle polárky", "Podle západu slunce", "Podle stínu stromů"],
    ["Andromeda", "Sluneční soustava", "Mléčná dráha"],
    ["Země", "51 Pegasi", "K2-18b"],
    ["Na Petříně", "V Ondřejivě", "Na Štefánikově hvězdárně v Brně"]
]

a = b = c = z = 0

for i in range(10):
    print(f"{i+1}. {asks[i]} a. {answers[i][0]} b. {answers[i][1]} c. {answers[i][2]}")
    answer = input("enter just a or b or c: ")
    
    if answer == "a":
        a += 1
    elif answer == "b":
        b += 1
    elif answer == "c":
        c += 1
    else:
        z += 1

if z > 0:
    print("The answer should have been either a, b, or c. Try again!")
elif a > b and a > c:
    print("You probably won't be an astrophysicist!")
elif b > a and b > c:
    print("Well done!!!!")
else:
    print("There is something wrong, try it again.")
