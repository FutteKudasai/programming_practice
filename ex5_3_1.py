r = eval(input("請輸入園半徑:"))
x, y = eval(input("請輸入座標:"))
dist = (x * x + y * y) ** 0.5
if(dist > r):
    print("點座標({},{}不在圓內部)".format(x, y))
elif(dist == r):
    print("點座標({},{}在圓周上)".format(x, y))
else:
    print("點座標({},{}在圓內部)".format(x, y))