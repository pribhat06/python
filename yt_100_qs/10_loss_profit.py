def loss_profit(cost_price , sell_price):
    if cost_price == sell_price:
        print("No profit no loss")
    elif cost_price < sell_price:
        print("it's a profit")
    else:
        print("It's a loss")



cost_price = int(input("Enter cost price"))
sell_price = int(input("Enter sell price"))

loss_profit(cost_price , sell_price)