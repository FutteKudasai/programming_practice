squares = []
n = int(input("請輸入整數:"))
if(n > 10):
    n = 10
for num in range(1, n + 1):
    value = num * num
    squares.append(value)
print(squares)