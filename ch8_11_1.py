dist = 384400
speed = 1225
#total_hours = dist // speed
data = divmod(dist // speed, 24)
print("divmod : ", type(data))
print("%d" % data[0])
print("%d " % data[1])