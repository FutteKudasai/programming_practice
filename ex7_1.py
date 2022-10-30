files = ['da1.jpg','da2.png','da3.gif','da4.gif','da5.jpg','da6.jpg','da7.gif']
jpg = []
png = []
gif = []
for file in files:
    if file.endswith('.jpg'):
        jpg.append(file)
    if file.endswith('.png'):
        png.append(file)
    if file.endswith('.gif'):
        gif.append(file)
print("jpg檔案串列",jpg)
print("png檔案串列",png)
print("gif檔案串列",gif)