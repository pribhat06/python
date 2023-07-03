# User will input (3ages).Find the oldest one
# https://docs.google.com/document/d/1b9z_mhbkKW_o2esMXKx12Yy3wEinxALFvDGtYaTGovQ/edit


def find_oldest(inp1, inp2, inp3):
    if inp1 > inp2 and inp1> inp3:
        print(f"oldest is {inp1}")
    elif inp2>inp3 and inp2>inp1:
        print(f"oldest is {inp2}")
    else:
        print(f"oldest is {inp3}")



# define 3 inputs
inp1 = input("Enter 1st age")
inp2 = input("Enter 2nd age")
inp3 = input("Enter 3rd age")

find_oldest(inp1, inp2, inp3)