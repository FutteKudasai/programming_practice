fruits = {"西瓜":15, "香蕉":20, "水蜜桃":25}
key = input("請輸入鍵(key) = ")
value = input("請輸入值(value) = ")
if key in fruits:
    print("%s已在字典裡了" % key)
else:
    fruits[key] = value
    print("新的fruits字典內容 = ", fruits)