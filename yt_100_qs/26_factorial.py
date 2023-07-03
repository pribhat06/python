# Write a program that can find the factorial of a given number provided by the user.
def factorial(num):
    for i in range(0, num+1):
        if num == 0:
            return 1
        else:
            c = num*factorial(num-1)
    return c


print(factorial(3))