# Print all the armstrong numbers in the range of 100 to 1000

def amstrong_num():
    l = []
    for i in range(100, 2001):
        
        temp = i
        num = 0
        n = len(str(i))
        while temp != 0:
            a = temp % 10
            #print("a", a)
            num += a**n
            temp = temp//10
            
        if i == num:
            l.append(i)
    return l
        





    








print(amstrong_num())