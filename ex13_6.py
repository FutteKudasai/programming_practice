import random

lotterys = random.sample(range(1, 50), 6)
specialNum = random.randint(1, 8)

print("第1000期威力彩號碼")
for lottery in sorted(lotterys):
    print(lottery, end=" ")
print("\n特別號: %d" % specialNum)