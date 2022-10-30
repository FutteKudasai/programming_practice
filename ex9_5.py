song = """Are you sleeping, atr you sleeping, Brother John, Brother John?
Morning bells are ringing, morning bells are ringing.
Ding ding dong, Ding ding dong."""
mydict = {}

songLower = song.lower()

for ch in songLower:
    if ch in ".,?":
        songLower = songLower.replace(ch,'')

songList = songLower.split()

for wd in songList:
    if wd in mydict:
        mydict[wd] += 1
    else:
        mydict[wd] = 1
        
maxCount = max(mydict.values())
for key , count in mydict.items():
    if count == maxCount:
        print("字串 %s 出現最多次共出現 %d 次" % (key, count))