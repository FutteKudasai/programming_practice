week = {"sumday": "星期天",
        "monday": "星期一",
        "tuesday": "星期二",
        "wednesday": "星期三",
        "thursday": "星期四",
        "friday": "星期五",
        "saturday": "星期六"}

key = input("請輸入星期幾的英文: ")
if key.lower() in week:
    print(week[key.lower()])
else:
    print("輸入錯誤")