import turtle
colour = [ "red", "blue", "green", "yellow", "purple", "orange", "white", "black" ]
number=random.randint(1,9)
number.range(50)
turtle.Screen().colormode(number)
turtle_t = turtle.Turtle()
turtle_t.shape("turtle") 
for m in range(3, 10):
    for n in range(m):
        turtle_t.forward(10)
        turtle_t.right(360/m)
    turtle_t.penup() # přestává kreslit
    turtle_t.forward(20) # o kolik jednotek se pohne dopředu
    turtle_t.pendown() # zase kreslí
turtle.done()
