fields = ['台北', '台中', '高雄']
info = [80000, 50000, 60000]
zipData = zip(fields, info)
print('zipData 資料類型', type(zipData))
player = list(zipData)
print('player 資料類型', type(player))
print(player)