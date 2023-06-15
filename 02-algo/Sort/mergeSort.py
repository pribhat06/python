def merge_sorted(arr1, arr2):
    i = j = 0
    merged = []
    while i<len(arr1) and j<len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
        else:
            arr2[j] < arr1[i]
            merged.append(arr2[j])
    while i < len(arr1):
        merged.append(arr1(i))
        i+=1
    while j < len(arr2):
        merged.append(arr2[j])
        i+=1
    return merged


arr1 = [2, 4, 6]
arr2= [8, 9, 10, 11, 12]


print(merge_sorted(arr1, arr2))
print("*************")

