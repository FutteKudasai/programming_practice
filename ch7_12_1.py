for i in range(1,10,1):
    for j in range(1,10,1):
        result = i * j
        print("%d*%d=%-3d" % (i, j, result), end = " ")
        print()