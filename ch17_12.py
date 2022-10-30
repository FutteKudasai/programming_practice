import turtle
import random

def stars(sides, size, cr, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    angle = 180 - (180  / sides)
    t.color(cr)
    t.begin_fill()
    for x in range(sides):
        t.forward(size)
        t.right(angle)
    t.end_fill()

t = turtle.Pen()
t.ht()
color_list = ["red","orange","yellow","green","blue","cyan","purple","violet"]

while True:
    ran_sides = random.randint(2, 5) * 2 + 1
    ran_size = random.randint(5, 30)
    ran_color = random.choice(color_list)
    ran_x = random.randint(-250, 250)
    ran_y = random.randint(-250, 250)
    stars(ran_sides, ran_size, ran_color, ran_x, ran_y)