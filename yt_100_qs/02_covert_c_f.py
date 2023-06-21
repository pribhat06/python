# Write a program that will convert celsius value to fahrenheit


def convert_c_f(c):
    f = ( c * 1.8) + 32
    return f
    

c = 21
print(convert_c_f(c))