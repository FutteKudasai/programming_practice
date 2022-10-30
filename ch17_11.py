import turtle

def stars(sides, size, cr, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    angle = 180 - (180 / sides)
    t.color(cr)
    t.begin_fill()
    for x in range(sides):
        t.forward(size)
        t.right(angle)
    t.end_fill()

t = turtle.Pen()
t.screen.bgcolor("blue")
stars(5, 60, "yellow", 0, 0)