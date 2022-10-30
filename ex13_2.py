import MyMath

print("請輸入運算")
print("1:加法")
print("2:減法")
print("3:乘法")
print("4:除法")
op = int(input("輸入1/2/3/4:"))
a = int(input("a = "))
b = int(input("b = "))

if op == 1:
    print("a + b = ", MyMath.add(a, b))
elif op == 2:
    print("a - b = ", MyMath.sub(a, b))
elif op == 3:
    print("a * b = ", MyMath.mul(a, b))
elif op == 4:
    print("a / b = ", MyMath.div(a, b))
else:
    print("錯誤!")