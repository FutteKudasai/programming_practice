fields = ['台北', '台中', '高雄']
info = [80000, 50000, 60000]
zipData = zip(fields, info)
sold_info = list(zipData)
for city, sales in sold_info:
    #print('{} 銷售金額是 {}'.format(city, sales))
    print('%s 銷售金額是 %d' % (city, sales))