import turtle # stáhneme knihovnu s potřebnou sadou příkazů
turtle.Screen().colormode(255) # umožnění barev
turtle_t = turtle.Turtle() # vytvoříme si pero na kreslení (nazývejme ho želva)
turtle_t.shape("turtle") # pero má tvar želvičky (jinak je to šipka)

# TLOUŠŤKA A BARVA PERA
turtle_t.pensize(5) # tloušťka pera
turtle_t.color("red") # nastavení barvy, kterou kreslíme na červenou, celý list názvů je zde: https://trinket.io/docs/colors 
turtle_t.color(152,25,47) # nastavení barvy pomocí RGB

# RYCHLOST ŽELVY
turtle_t.speed(10)
n = int(input("entrr n:"))
for i in range(n):
    turtle_t.forward(i+10)
    turtle_t.right(90)
turtle.done()

