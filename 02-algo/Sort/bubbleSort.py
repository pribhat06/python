def bubble_sort(arr):
    #loop through the passess
    for i in range(len(arr)-1):
        #loop through all the passes and find the pairs in a pass
        for j in range(len(arr)-1 -i): # substracting i cz the final pass is already in the nth index
            #condision to check if 1st eliment greater then 2nd
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr
    

arr = [78, 6, 677, 12, 54, 43]
print(bubble_sort(arr))

brr = ["agy", "agys", "aaa", "hsuy"]
print(bubble_sort(brr))

print("**************ADAPTIVE BUBBLE SORT*********************")


def p_bubble_sort(arr):
    
    for i in range(len(arr)-1):
        flag = 0 #take a variable to compare if any swap happens
        for j in range(len(arr)-1 -i): 
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = 1 # if swap happens, then assign flag to 1
        
        if flag == 0: # if no swap happened in pass, then break the loop
            break

    return arr



partial_sorted_arr = [34, 21, 54, 2, 3, 5]
print(p_bubble_sort(partial_sorted_arr))

