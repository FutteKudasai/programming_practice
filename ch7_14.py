scores = [33, 22, 41, 25, 39, 43, 27, 38, 40]
games = 0
for score in scores:
    if(score < 30):
        continue
    games += 1
print("有 %d 場超過30分" % games)