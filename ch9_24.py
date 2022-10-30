person = {'name':'john'}
print("原先字典內容", person)
age = person.setdefault('age')
print("增加age鍵", person)
print("age = ", age)
sex = person.setdefault("sex", "Male")
print("增加sex鍵", person)
print("sex = ", sex)