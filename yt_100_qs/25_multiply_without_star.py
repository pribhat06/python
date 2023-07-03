# Write a program that can multiply 2 numbers provided by the user without using the * operator
def multiply_without_operator(num, num2):
    sum = 0 
    for i in range(num2):
        #print("num", num)
        sum += num
    return f" {num} * {num2} is = {sum}"



num = 10
num2 = 2
print(multiply_without_operator(num, num2))