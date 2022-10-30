accopnts = []
accopnt = input("請輸入新帳號")
accopnts.append(accopnt)
print("深石公司系統")
ac = input("請輸入帳號")
if ac in accopnts:
    print("歡迎進入深石系統")
else:
    print("帳號錯誤")