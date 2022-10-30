import turtle

t = turtle.Pen()
colorsList = ["red","orange","yellow","green","blue","cyan","purple","violet"]
tWidth = 1
for x in range(1, 41):
    t.color(colorsList[x % 8])
    t.forward(2 + x * 5)
    t.right(45)
    tWidth += x * 0.05
    t.width(tWidth)