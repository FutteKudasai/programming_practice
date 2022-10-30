cocktail = {
    "Blue Hawaiian" : {"Rum","Sweet Wine","Cream","Pineapple Juice","Lemon Juice"}, 
    "Ginger Mojito" : {"Rum","Ginger","Mint Leaves","Lime Juice","Ginger SodaS"}, 
    "New Yorker" : {"Whiskey","Red Wine","Lemon Juice","Sugar Syrup"}
}

print("含有Lemon Juice的酒：")
for name, formulas in cocktail.items():
    if "Lemon Juice" in formulas:
        print(name)

print("含有Rum但是沒有薑的酒：")
for name, formulas in cocktail.items():
    if "Rum" in formulas and not ("Ginger" in formulas):
        print(name)