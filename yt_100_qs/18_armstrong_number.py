# Write a program that will check whether the number is armstrong number or not.

def is_amstrong(num):
    
    temp = num
    n = len(str(num))
    sum = 0
    
    while temp != 0:
        a = temp % 10
        sum = sum + (a ** n)
        temp = temp // 10

    if num == sum:
        print("The given number", num, "is armstrong number")
    else:
        print("The given number", num, "is not armstrong number")



num = 153
is_amstrong(num)