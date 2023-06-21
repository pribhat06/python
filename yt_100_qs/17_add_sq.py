#Write a program that will take three digits from the user and add the square of each digit.


def sq(inp1, inp2, inp3):
    c = (inp1 **2)+(inp2 **2)+(inp3 **2)
    return c



inp1 = int(input("Enter your inp1"))
inp2 = int(input("Enter your inp2"))
inp3 = int(input("Enter your inp3"))
print(sq(inp1, inp2, inp3))