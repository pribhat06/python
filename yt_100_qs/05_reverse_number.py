# Write a program that will reverse a four digit number.
# Also it checks whether the reverse is true.


def reverse_num(num):
    rev_num = 0
    while num != 0:
        a = num % 10
        rev_num = rev_num*10 + a
        num = num//10
    print( str(rev_num))

    

        


num = int(input("Enter number to reverse"))
reverse_num(num)
