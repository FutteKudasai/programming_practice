scores = [94, 82, 60, 91, 88, 79, 61, 93, 99, 77]
scores.sort(reverse = True)
count = 0
for sc in scores:
    count += 1
    print(sc, end = " ")
    if(count == 5):
        break