a = eval(input("輸入平方項係數 a:"))
b = eval(input("輸入一次項係數 b:"))
c = eval(input("輸入常數項係數 c:"))

r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
print("r1 = %6.4f,   r2 = %6.4f" % (r1, r2))