dist = 384400
speed = 1225
total_hours = dist // speed
print(total_hours)
days, hours = divmod(total_hours, 24)
print("總共需要天數")
print(days)
print("小時數")
print(hours)