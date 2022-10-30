money = 50000
rate = 0.015
n = 5
for i in range(n):
     money *= (1 + rate)
     print("第{0:^3d}年本金和 : {1:<10.1f} " .format((i+1),money))