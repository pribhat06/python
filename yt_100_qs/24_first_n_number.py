# Write a program to find the sum of first n numbers, where n will be provided by the user. Eg if the user provides n=10 the output should be 55.

def s_num(inp):
    c = 0
    for i in range(inp+1):
        c += i
    return c
        
    


inp = int(input("Enter number"))
print(s_num(inp))