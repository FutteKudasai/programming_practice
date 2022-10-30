print("判斷輸入字元類別")
ch = input("請輸入字元")
if(ord(ch) >= ord("A") and ord(ch) <= ord("Z")):
    print("大寫字元")
elif(ord(ch) >= ord("a") and ord(ch) <= ord("z")):
    print("小寫字元")
elif(ord(ch) >= ord("0") and ord(ch) <= ord("9")):
    print("數字")
else:
    print("特殊字元")