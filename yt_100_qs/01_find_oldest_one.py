# User will input (3ages).Find the oldest one


def find_oldest(inp1, inp2, inp3):
    if inp1 > inp2 and inp1> inp3:
        print(f"largest is {inp1}")
    elif inp2>inp3 and inp2>inp1:
        print(f"largest is {inp2}")
    else:
        print(f"largest is {inp3}")



# define 3 inputs
inp1 = input("Enter 1st age")
inp2 = input("Enter 2nd age")
inp3 = input("Enter 3rd age")

find_oldest(inp1, inp2, inp3)