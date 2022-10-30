x, y = eval(input("請輸入兩個數"))
max_ = x if x > y else y
print("方法1最大值:", max_)
max_ = max(x, y)
print("方法2最大值:", max_)

min_ = x if x < y else y
print("方法1最小值:", min_)
min_ = min(x, y)
print("方法2最小值:", min_)