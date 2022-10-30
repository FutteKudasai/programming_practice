def division(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print("除數不可為0")
    except TypeError:
        print("除法資料型態不符")

print(division(10, 2))
print(division('a', 'b'))
print(division(6, 3))