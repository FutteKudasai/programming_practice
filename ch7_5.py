files = ["da1.c", "da2.py", "da3.py", "da4.java"]
py = []
for file in files:
    if(file.endswith(".py")):
        py.append(file)
print(py)