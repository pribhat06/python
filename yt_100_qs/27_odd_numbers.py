# find if the list have below 25 odd numbers

def find_odd_num(l):
    
    for i in l:
        #print("i", i)
        if i < 25:
            if i % 2 != 0:
                print(True)
        else:
            print(False)

    



list_1 = [7, 26, 53, 9, 11, 24]
find_odd_num(list_1)

print("*" * 50)
# Write a program to print the odd numbers in a list. numbers will under 25

def odd_num(l):
    new_l = []
    for i in l:
        if i < 25:
            if i % 2 != 0:
                new_l.append(i)

    return(new_l)
        
    

l = [7, 26, 53, 9, 11, 24]
print(odd_num(l))



print("*"* 100)

# 
def first_25_odds():
    l1 = []
    for i in range(1, 26):
        #print("i", i)
        if i % 2 != 0:
            l1.append(i)     
    print(l1)

first_25_odds()