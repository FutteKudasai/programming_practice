students = {"Peter","Norton","Kevin","Mary","John","Ford","Nelson","Damon","Ivan","Tom"}

Math = {"Peter","Kevin","Damon"}
Physics = {"Nelson","Damon","Tom"}

MandP = Math | Physics
print("有 %d 人參加數學和物理夏令營名單：" % len(MandP), MandP)
unAttend = students - Physics
print("沒有參加任何夏令營有 %d 人名單是：" % len(unAttend), unAttend)
MoreP = Math & Physics
print("同時參加夏令營有 %d 人名單是：" % len(MoreP), MoreP)