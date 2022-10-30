store = 'DeepMind購物中心'
products = ['電視','冰箱','洗衣機','電扇','冷氣機']
cart = []
print(store)
print(products,"\n")
while True:
    msg = input("請輸入購買商品(q=quit) : ")
    if msg == 'q' or msg=='Q':
        break
    else:
        if msg in products:
            cart.append(msg)

            print("今天購買商品", cart)