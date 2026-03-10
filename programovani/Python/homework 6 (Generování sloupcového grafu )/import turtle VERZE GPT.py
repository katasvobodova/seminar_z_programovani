import turtle
import colorsys

turtle.Screen().colormode(255)
turtle.bgcolor("black")
pen = turtle.Turtle()
pen.color("white")
pen.pensize(5)
pen.penup()
turtle.tracer(False)

#data = [10, 20, 30, 27, 15, 1, 5]
#data = [367, 454, 87, 316, 122, 322, 460, 289, 430, 234, 370, 136, 439, 9, 482]
data = [399, 392, 22, 416, 128, 315, 38, 245, 411, 228, 137, 461, 256, 353, 28, 68, 187, 213, 94, 363, 301, 256, 42, 302, 166, 313, 490, 67, 389, 406, 140, 331, 235, 159, 451, 18, 206, 313, 232, 429]

def DRAW_AXIS(length, angle, name):
    pen.left(angle)
    pen.pendown()
    pen.forward(length)
    pen.write(f"  {name}", font=("Arial", 12, "normal")) 
    DRAW_ARROW()  
    pen.penup()
    pen.right(angle)

def DRAW_ARROW():
    pen.forward(10)
    pen.left(150)
    pen.forward(10)
    pen.backward(10)
    pen.right(300)
    pen.forward(10)
    pen.left(150)
    pen.backward(10)

def draw_rectangle(height, width, color):
    height_new=(length_axis_x//2)*(column/max(data))
    pen.pendown()
    pen.color(color)
    pen.begin_fill()
    pen.forward(width)
    pen.left(90)
    pen.forward(height_new)
    pen.left(90)
    pen.forward(width//2)
    pen.color("white")
    pen.write(height)
    pen.color(color)
    pen.forward(width//2)
    pen.left(90)
    pen.forward(height_new)
    pen.left(90)
    pen.end_fill()
    pen.penup()

length_axis_x = 650
length_axis_y = length_axis_x/2
start_x = -300
start_y = -250

pen.goto(start_x, start_y)
DRAW_AXIS(length_axis_x, 0, "x")

pen.goto(start_x, start_y)
DRAW_AXIS(length_axis_y, 90, "y")

width_space = 20
width_columns = (length_axis_x - (len(data) + 3) * width_space) / len(data)
shadow = 0.0

pen.goto(start_x, start_y)

for column in data:
    shadow += 1 / len(data)
    r, g, b = colorsys.hsv_to_rgb(shadow, 1.0, 1.0)
    color = (int(r * 255), int(g * 255), int(b * 255))
    pen.forward(width_space)
    draw_rectangle(column, width_columns, color)

turtle.done()
