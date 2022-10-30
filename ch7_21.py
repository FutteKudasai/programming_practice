prime = []
num = int(input("請輸入大於1的整數做質數測試 = "))
if(num == 2):
    prime.append(num)
else:
    for n in range(2, num):
        if(num % n == 0):
            break
        else:
            prime.append(num)
if(prime):
    print("{} 是質數".format(num))
else:
    print("{} 不是質數".format(num))