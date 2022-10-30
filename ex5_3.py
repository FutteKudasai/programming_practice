r = 20
x, y = eval(input("請輸入座標:"))
dist = (x * x + y * y) ** 0.5
if(dist > r):
    print("點座標({},{}不在圓內部)".format(x, y))
else:
    print("點座標({},{}在圓內部)".format(x, y))