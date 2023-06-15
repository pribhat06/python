# Consider i is the 1st index of an arr that runs until len(arr)-1,
# also min is the 1st index,
#we have to compare j with min, 
#so j will be the next eliment of min.
#everytime j increments it's index if condition does not match
#after completing 1 pass j will start again from i+1 and run until len(arr)
#if arr[j] < arr[min]
# the min will assign to j
#after completing the loop min will be the lowest in a pass,
#so we will swap the arr[min] with arr[i]
#after completing all passes we will get the sorted arr

def selection_sort(arr):
    #i
    for i in range(len(arr)-1):
        # min index = i index
        min = i
        # start the loop j
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    print(arr)


l = [5, 87, 36, 23, 98, 56]
selection_sort(l)


        
