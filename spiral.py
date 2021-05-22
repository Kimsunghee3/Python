import turtle

t = turtle.Turtle()

t.speed(0)
t.width = 10
length = 10  
colors =['red', 'purple', 'blue', 'green', 'yellow' ]

while length < 500:
    t.forward(length)
    t.pencolor(colors[length%len(colors)])
    t.right (89)
    length = length + 6
