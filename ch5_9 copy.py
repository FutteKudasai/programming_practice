a = eval(input("a="))
b = eval(input("b="))
c = eval(input("c="))

r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
print("r1 = %6.4f, r2 = %6.4f" % (r1, r2))