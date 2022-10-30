height = input("請輸入身高(公分)")
weight = input("請輸入體重(公斤)")
bmi = int(weight) / ((float(height) / 100 ) ** 2)
if(bmi >= 18.5 and bmi < 24):
    print("體重正常")
    print("bmi = %4.1f" % bmi)
elif(bmi >= 24):
    print("體重過重")
    print("bmi = %4.1f" % bmi)
elif(bmi < 18.5):
    print("體重過輕")
    print("bmi = %4.1f" % bmi)
else:
    print("發生錯誤!")