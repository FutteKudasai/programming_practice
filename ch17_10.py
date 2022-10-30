import turtle

t = turtle.Pen()
sides = 5
angle = 180 - (180 / sides)
size = 100
t.color("blue")
t.begin_fill()
for x in range(sides):
    t.forward(size)
    t.right(angle)
t.end_fill()