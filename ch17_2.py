import turtle

t = turtle.Pen()
t.pensize(5)
colorValue = 1.0
colorStep = colorValue / 36
for x in range(1, 37):
    colorValue -= colorStep
    t.color(0.5, 1, colorValue)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)