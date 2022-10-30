path = ['D:','ch6','ch6_36.py']
connect = '\\'
connect1 = connect.join(path)
print(connect1)
connect3 = connect1.split('\\')
print(connect3)
connect = '*'
connect2 = connect.join(path)
print(connect2)
connect4 = connect2.split('*')
print(connect4)