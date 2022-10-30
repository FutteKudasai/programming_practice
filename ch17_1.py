import turtle
t = turtle
sides = 5
angle = 180 - (180 / sides)
size = 100
for x in range(sides):
    t.forward(size)
    t.right(angle)