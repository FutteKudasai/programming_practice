import random
min1 = 0
max1 = 100
answer = random.randint(min1, max1)
guess = 0
index = 1
while guess!= answer:
    guess = int(input("請猜 %d - %d 間的數字" % (min1, max1)))
    if guess > answer:
        print("請猜小一點")
        if guess > max1:
            print("不要亂猜")
        else:
            max1 = guess
    elif guess < answer:
        print("請猜大一點")
        if guess < min1:
            print("不要亂猜")
        else:    
            min1 = guess
    else:
        print("恭喜答對了")
        print("共猜了 %d 次" % index)
    index += 1