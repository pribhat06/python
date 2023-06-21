def odd_even(num):
    
        if num == 1 or num == 0:
            print("not even or odd ")
        elif num % 2 == 0:
            print("even number")
        else:
            print("Odd number")



inp = int(input("Enter your number"))
odd_even(inp)