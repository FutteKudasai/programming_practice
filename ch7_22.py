e = 1
val = 1
for i in range(1,101,1):
    val = val / i
    e += val
    if(i % 10 == 0):
        print("當i是 %3d 時 e = %40.39f" % (i, e))