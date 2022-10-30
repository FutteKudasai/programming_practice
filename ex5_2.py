n1, n2, n3 = eval(input("請輸入3個整數值: "))
if(n1 < n2):
    n1, n2 = n2, n1
if(n2 < n3):
    n2, n3 = n3, n2
if(n1 < n2):
    n1 ,n2 = n2, n1
print(n1,n2,n3)