def binary_search(nLst):
    print("列印搜索串列：",nLst)
    low = 0
    high = len(nLst) - 1
    middle = int((high + low) / 2)
    times = 0 
    while(1):
        times += 1
        if key == nLst[middle]:
            rtn = middle
            break

        elif key > nLst[middle]:
            low = middle + 1

        else:
            high = middle - 1
        
        middle = int((high + low) / 2)
        if low > high:
            rtn = -1
            break

    return rtn, times

data = [19, 32, 28, 99, 10, 88, 62, 8, 6, 3]
sorted_data = sorted(data)
key = int(input("請輸入搜尋值："))
index, times = binary_search(sorted_data)
if index != -1:
    print("在索引 %d 位置找到了，共找了 %d 次" % (index, times))
else:
    print("查無此搜尋號碼")