import turtle
turtle.Screen().colormode(255)
pen = turtle.Turtle()
pen.penup()
turtle.tracer(False)

data = [10, 20, 30, 27, 15, 1, 5] # hodnoty na ose y
#data = [367, 454, 87, 316, 122, 322, 460, 289, 430, 234, 370, 136, 439, 9, 482]
#data = [399, 392, 22, 416, 128, 315, 38, 245, 411, 228, 137, 461, 256, 353, 28, 68, 187, 213, 94, 363, 301, 256, 42, 302, 166, 313, 490, 67, 389, 406, 140, 331, 235, 159, 451, 18, 206, 313, 232, 429]

def KresliOsu(delka, uhel, jmeno):
    pen.pendown()
    pen.forward(delka)
    pen.right(uhel)
    pen.text(50, -25, '"jmeno"')
    pen.penup()
    # TODO smažte pass a implementujte tělo funkce, které vykreslí osu dané délky pod daným úhlem s daným jménem
    # TODO osa má mít na konci šipečku ;)

def KresliObdelnik(vyska, sirka, barva):
    pen.pendown()
    pen.forward(vyska)
    pen.penup()
    # TODO smažte pass a implementujte tělo funkce, které vykreslí jeden sloupec grafu o dané výšce, šířce a barvě



# VYKRESLENÍ OS
delka_osy_x = 100
start_x = -50
start_y = -25

pen.goto(start_x, start_y)
KresliOsu(delka_osy_x, 0,"x"),
arrowprops=dict(arrowstyle='->', color='black', lw=2)

pen.goto(start_x, start_y)
pen.right(270)
KresliOsu(delka_osy_x//2, 270, "y")
pen.goto(start_x, start_y),
arrowprops=dict(arrowstyle='->', color='black', lw=2)



# TODO napište zbytek programu, který vykreslí jednotlivé sloupce
    

turtle.done()