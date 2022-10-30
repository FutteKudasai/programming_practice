song = """Are you sleeping, atr you sleeping, Brother John, Brother John?
Morning bells are ringing, morning bells are ringing.
Ding ding dong, Ding ding dong."""
mydict = {}
print("原始歌曲")
print(song)
songLower = song.lower()
print("小寫歌曲")
print(songLower)
for ch in songLower:
    if ch in ".,?":
        songLower = songLower.replace(ch,'')
print("不再有標點符號的歌曲")
print(songLower)
songList = songLower.split()
print("以下是歌曲串列")
print(songList)
for wd in songList:
    if wd in mydict:
        mydict[wd] += 1
    else:
        mydict[wd] = 1
        print("以下是最後執行結果")
        print(mydict)