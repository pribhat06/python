# Print first 25 prime numbers
def prime_number():
    new_list = []
    for i in range(2, 25):
        
        for j in range(2, i//2 +1):
            if i % j == 0:
                break
        else:
            new_list.append(i)
    return new_list





print(prime_number())