sc = [[1, '洪錦魁', 80, 95, 88, 0, 0, 0],
[2, '洪冰儒', 98, 97, 96, 0, 0, 0],
[3, '洪雨星', 91, 93, 95, 0, 0, 0],
[4, '洪冰雨', 92, 94, 90, 0, 0, 0],
[5, '洪星宇', 92, 97, 90, 0, 0, 0],]
print("填入總分與平均")
for i in range(len(sc)):
    sc[i][5] = sum(sc[i][2:5])
    sc[i][6] = round((sc[i][5] / 3), 1)
    print(sc[i])
sc.sort(key=lambda x:x[5],reverse=True)
print("填入名次")
for i in range(len(sc)):
    sc[i][7] = i + 1
    print(sc[i])
sc.sort(key=lambda x:x[0])
print("最後成績單")
for i in range (len(sc)):
    print(sc[i])