def triangle(a, b, c):
    if a + b+ c == 180:
        print("it's a triangle")
    else:
        print("it's not a triangle")



inp1 = int(input("Enter 1st angle"))
inp2= int(input("Enter 2nd angle"))
inp3 = int(input("Enter 3rd angle"))
triangle(inp1, inp2, inp3)