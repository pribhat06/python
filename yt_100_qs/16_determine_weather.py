 #Write a program that will determine weather when the value of temperature and humidity is provided by the user.
# TEMPERATURE(C)      HUMIDITY(%)      WEATHER

#       >= 30                             >=90                Hot and Humid
#       >= 30                             < 90                 Hot
#       <30                                >= 90               Cool and Humid
#       <30                                 <90                 Cool



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