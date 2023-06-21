def weather(t, h):
    if t >= 30 and h >= 90:
        print("Hot and Humid")
    elif t >= 30 and h < 90:
        print("Hot")
    elif t < 30 and h >= 90:
        print("Cool and Humid")
    else:
        print("cool")






temeratures = int(input("Enter the temperature"))
humidity = int(input("Enter the humidity"))

weather(temeratures, humidity)