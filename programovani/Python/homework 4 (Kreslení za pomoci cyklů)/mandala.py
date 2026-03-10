import turtle
turtle.Screen().colormode(255)
pen = turtle.Turtle()
pen.shape("turtle")
screen = turtle.Screen()
screen.bgcolor("white")
pen = turtle.Turtle()
pen.speed(0)
def draw_flower():
    for i in range(36):
        pen.circle(100)
        pen.right(10)  
draw_flower()
turtle.done()