bookclub = ("John", "Peter", "Curry", "Mike", "Kevin")
print("讀書會成員")
for people in bookclub:
    print(people)
list_club = list(bookclub)
list_club.append("Mary")
list_club.append("Tom")
list_club.append("Carlo")
bookclub = ("John", "Peter", "Curry", "Mike", "Kevin", "Mary", "Tom", "Carlo")
print("新讀書會成員")
for people in bookclub:
    print(people)