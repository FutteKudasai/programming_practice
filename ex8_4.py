tp = (1, 2, 3, 4, 5, 2, 3, 1, 4)
lst = list(tp)
newlst =[]
for i in lst:
    if i not in newlst:
        newlst.append(i)
newtp = tuple(newlst)
print("新的元祖內容 : ", newtp)