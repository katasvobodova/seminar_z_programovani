import turtle
import colorsys

# Nastavení plátna a pera
turtle.Screen().colormode(255)
turtle.bgcolor("black")
pen = turtle.Turtle()
pen.color("white")
pen.pensize(5)
pen.penup()
turtle.tracer(False)

# Data pro sloupcový graf
data = [399, 392, 22, 416, 128, 315, 38, 245, 411, 228, 137, 461, 256, 353, 28, 68, 187, 213, 94, 363, 301, 256, 42, 302, 166, 313, 490, 67, 389, 406, 140, 331, 235, 159, 451, 18, 206, 313, 232, 429]
#data = [10, 20, 30, 27, 15, 1, 5]
#data = [367, 454, 87, 316, 122, 322, 460, 289, 430, 234, 370, 136, 439, 9, 482]

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
    pen.backward(10)

# Funkce pro vykreslení sloupce
def draw_rectangle(height, width, color):
    pen.pendown()
    pen.color(color)
    pen.begin_fill()
    pen.forward(width)
    pen.left(90)
    pen.forward(height)
    pen.left(90)
    pen.forward(width)
    pen.left(90)
    pen.forward(height)
    pen.left(90)
    pen.end_fill()
    pen.penup()  # Posun na další sloupec

# Nastavení os a počáteční pozice
length_axis_x = 650
length_axis_y = 300  # Výška osy Y je zvolena jako polovina délky osy X
start_x = -300
start_y = -250

# Vykreslení osy X
pen.goto(start_x, start_y)
DRAW_AXIS(length_axis_x, 0, "x")

# Vykreslení osy Y
pen.goto(start_x, start_y)
DRAW_AXIS(length_axis_y, 90, "y")

# Výpočet šířky sloupců a mezer mezi nimi
width_space = 10  # Mírně zúžené mezery mezi sloupci
width_columns = (length_axis_x - (len(data) + 1) * width_space) / len(data)

# Vykreslení sloupců grafu
pen.goto(start_x, start_y)

max_height = max(data)  # Nejvyšší hodnota pro výpočet velikosti sloupce

for column in data:
    # Vytvoření barvy pro každý sloupec podle jeho pořadí
    color = colorsys.hsv_to_rgb((column / max_height) % 1, 1.0, 1.0)  # Barva se mění podle výšky
    pen.forward(width_space)  # Posun na pozici sloupce
    draw_rectangle((column / max_height) * length_axis_y, width_columns, color)

turtle.done()
