james = [['Lebron James','SF','12/30/84'],23,19,22,31,18]
games = len(james)
score_Max = max(james[1:games])
i = james.index(score_Max)
name = james[0][0]
position = james[0][1]
born = james[0][2]
print("姓名    : ", name)
print("位置    : ", position)
print("出生日期 : ", born)
print("在第 %d 場得最高分 %d" % (i,score_Max))