L = [2, -1, 4, 6, 3, 8]

for i in range(len(L)):
    k = L[i]
    j = i-1

    while j >= 0 and k<L[j]:
        L[j+1] = L[j]
        j = j-1

    else:
        L[j+1] = k
print(L)

print("*"* 50)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        j= i

        while arr[j-1]>arr[j] and j>0:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j-=1





arr= [1,3 , 0, 4, -1, 6, 3, 8]
insertion_sort(arr)
print(arr)