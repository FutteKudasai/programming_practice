sc = [['洪錦魁', 80, 95, 88, 0],
      ['洪水儒', 98, 97, 96, 0],
     ]
sc[0][4] = sum(sc[0][1:4])
sc[1][4] = sum(sc[1][1:4])
print(sc[0])
print(sc[1])