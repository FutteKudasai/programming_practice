age = eval(input("計算票價，請輸入年齡"))
ticket = 100
if age >= 80 or age <= 6: ticket *= 0.2
elif age >= 60 or age <= 12: ticket *= 0.5
else: ticket *= 1
print("%d" % ticket)