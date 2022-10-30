import turtle

t = turtle.Pen()
t.color("white")
r = 30
t.penup()
t.setheading(180)
t.forward(270)
t.setheading(0)
colorsList = ["red","orange","yellow","green","blue","cyan","purple","violet"]
for edge in range(3, 13, 1):
    t.pendown()
    t.fillcolor(colorsList[edge % 8])
    t.begin_fill()
    t.circle(r, steps=edge)
    t.end_fill()
    t.penup()
    t.forward(60)