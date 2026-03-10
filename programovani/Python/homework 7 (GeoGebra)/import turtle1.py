import turtle
import colorsys

# Nastavení plátna a pera
screen = turtle.Screen()
screen.colormode(255)
turtle.bgcolor("black")
pen = turtle.Turtle()
pen.color("white")
pen.pensize(2)
pen.penup()
pen.shape ("blank")
turtle.tracer(False)

# Funkce pro vykreslení osy s šipkou na konci
def DRAW_AXIS(length, angle, name):
    pen.left(angle)
    pen.pendown()
    pen.forward(length)
    pen.write(f"  {name}", font=("Arial", 12, "normal"))  # Označení osy na konci
    DRAW_ARROW()  # Přidání šipky na konec osy
    pen.penup()
    pen.right(angle)

# Funkce pro vykreslení šipky
def DRAW_ARROW():
    pen.forward(10)
    pen.left(150)
    pen.forward(10)
    pen.backward(10)
    pen.right(300)
    pen.forward(10)
    pen.left(150)

# měřítko
def vykreslení_hodnot_na_ose(poc_x,poc_y,SOURADNICE, angle, delka_dane_osy):
    pen.left(angle)
    pen.goto(poc_x, poc_y)
    i = 0
    souradnice_now = -(delka_dane_osy)
    while(i<2*delka_dane_osy):
        pen.write(f"{SOURADNICE}", font=("Arial", 7, "normal"))
        pen.forward(krok)
        pen.backward(10)
        pen.pendown()
        pen.left(90)
        pen.forward(5)
        pen.backward(10)
        pen.forward(5)
        pen.right(90)
        pen.penup()
        pen.forward(10)
        SOURADNICE = SOURADNICE+1
        i = i+krok
        souradnice_now = souradnice_now+krok
    pen.right(angle)

krok = 20 # jak velké mezery budou mezi souřednicema

# Nastavení os a počáteční pozice
length_axis_x = 350
length_axis_y = length_axis_x
start_x = 0
start_y = 0

# Vykreslení osy X
pen.goto(start_x, start_y)
DRAW_AXIS(length_axis_x, 0, "x")

# Vykreslení osy Y
pen.goto(start_x, start_y)
DRAW_AXIS(length_axis_y, 90, "y")

# Vykreslení osy -X
pen.goto(start_x, start_y)
DRAW_AXIS(length_axis_x, 180,"")

# Vykreslení osy -Y
pen.goto(start_x, start_y)
DRAW_AXIS(length_axis_y, -90, "")

#kresleni liearni fce y = x * a + b
def Nakres_linearni_fce(a, b):
    x = -300
    while(x<300):
        y = (x/krok*a + b)*krok
        pen.goto(x*20, y*20)
        x = (x+0.05)
        pen.pendown()
        pen.forward(1)
        pen.penup()

# kresli kvadratickou fci y = a*x**2 + b*x + c
def Nakres_kvadraticke_fce(a, b, c):
    x = -300
    while(x<300):
        y=(a*(x/krok)**2+b*x+c)*krok
        pen.goto(x, y)
        x = (x+0.05)
        pen.pendown()
        pen.forward(1)
        pen.penup()


# kresli konstantní fci y = a
def Nakres_konstantni_fce(a):
        x = -300
        while(x<300):
            y=a*krok
            x = (x+0.05)
            pen.pendown()
            pen.forward(1)
            pen.penup()

def move_up():
    turtle.setheading(90)  # Face upward
    turtle.forward(10)

def move_down():
    turtle.setheading(270)  # Face downward
    turtle.forward(10)

def move_left():
    turtle.setheading(180)  # Face left
    turtle.forward(10)

def move_right():
    print("PRAVO")

# Vykreslení hodnot na osách
vykreslení_hodnot_na_ose(-length_axis_x,0,-(length_axis_x//krok), 0, length_axis_x) 
vykreslení_hodnot_na_ose(0,-length_axis_y,-(length_axis_x//krok), 90, length_axis_y)

# otazka na fci
chces_graf = (input("Napiš jestli chceš kreslit nějaký graf (jestli ano tak napiš jestli chceš konstantní finkci (ko) lineární funkci (l), nebo kvadratickou funkci (kv), nebo jetli žádnou funkci nechceš napiš (q):"))
if chces_graf == "ko":
    koefilient_a = int(input("Pro konstantní rovníci ve tvaru y = a vlož číslo za koeficient a:"))
    Nakres_konstantni_fce(koefilient_a)
elif chces_graf == "l":
    koefilient_a = int((input("Pro lineární rovnici ve tvaru y = x * a + b vlož číslo za koeficient a:")))
    koefilient_b = int((input("Pro lineární rovnici ve tvaru y = x * a + b vlož číslo za koeficient b:")))
    Nakres_linearni_fce(koefilient_a, koefilient_b)
elif chces_graf == "kv":
    koefilient_a = int((input("Pro lineární rovnici ve tvaru y = a*x**2 + b*x + c vlož číslo za koeficient a:")))
    koefilient_b = int((input("Pro lineární rovnici ve tvaru y = a*x**2 + b*x + c vlož číslo za koeficient b:")))
    koefilient_c = int((input("Pro lineární rovnici ve tvaru y = a*x**2 + b*x + c vlož číslo za koeficient c:")))
    Nakres_kvadraticke_fce(koefilient_a, koefilient_b, koefilient_c)
elif chces_graf == "q":
    turtle.done()
else:
    print("Jsi tupec")
turtle.done()
