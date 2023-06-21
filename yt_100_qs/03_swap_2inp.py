# User will input (2numbers).Write a program to swap the numbers
def swap_num(inp1, inp2):  
    s = inp1, inp2 = inp2, inp1
    return f"swapped numbers are {s}"
    




inp1 = int(input("Enter 1st number"))
inp2 = int(input("Enter 2nd number"))
print(swap_num(inp1, inp2))