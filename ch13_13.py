import random

lotterys = random.sample(range(1,50),7)
specialNum = lotterys.pop()

print("第xxx期大樂透號碼 ", end = '')
for lottery in sorted(lotterys):
    print(lottery, end = ' ')
print("\n特別號:%d" % specialNum)