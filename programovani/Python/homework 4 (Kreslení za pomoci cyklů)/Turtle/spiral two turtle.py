import turtle
turtle.Screen().colormode(255)
turtle_t = turtle.Turtle()
turtle_t.shape("turtle") 
n = int(input("entrr n:"))
for i in range(n):
    turtle_t.forward(i+10)
    turtle_t.right(72.7)
turtle.done()