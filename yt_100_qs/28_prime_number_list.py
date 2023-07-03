# Write a program to print whether a given number is prime number or not   
    
def prime_num(l):
    new_l = []
    for num in l:
        if num == 0 and num == 1:
            continue
        for i in range (2, num//2 + 1):
            print("i :", i, "num :", num)
            if num % i == 0:
                break

        else:
            new_l.append(num)
    return new_l


            



l = [1, 2, 7, 9, 3, 107, 21]
print(prime_num(l))