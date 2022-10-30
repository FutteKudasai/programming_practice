import random

min, max = 1, 30
ans = random.randint(min, max)
count = 0

while(1):
    num = input("請猜1-30之間的數字:")
    if num == 'Q' or num =='q':
        break
    yourNum = int(num)
    count += 1
    if yourNum == ans:
        print("你答對了!")
        print("總共猜測 %d 次" % count)
        break
    elif yourNum < ans:
        print("請猜大一點")
    elif yourNum > ans:
        print("請猜小一點")
    else:
        print("發生錯誤!")
        break