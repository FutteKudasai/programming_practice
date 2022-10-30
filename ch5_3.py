print("奇數偶數判斷")
number = eval(input("輸入任一數字"))
if(number == 0):
    print("0不是奇數也不是偶數")
else:
    rem = number % 2
    if(rem):
        print("%d 是奇數" % number)
    else:
        print("%d 是偶數" % number)