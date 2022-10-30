import random
answer = random.randint(0, 100)
guess = 0
index = 1
while guess!= answer:
    guess = int(input("請猜1-100間的數字"))
    if guess > answer:
        print("請猜小一點")
    elif guess < answer:
        print("請猜大一點")
    else:
        print("恭喜答對了")
        print("共猜了 %d 次" % index)
    index += 1