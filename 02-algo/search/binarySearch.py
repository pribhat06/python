def binanry_search(item_list, item):
    first = 0
    last = len(item_list) - 1
    found = False
    while(first<= last and not found):
        mid = (first + last)//2

        if item_list[mid] == item:
            found = True
        else:
            if item < item_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found




print("************************************")


def bin_search(l, item1):
    first = 0
    last = len(l)-1
    

    while first <= last:
        mid = (last +first)//2

        if l[mid] < item1:
            first = mid + 1
        elif l[mid] > item1:
            last = mid - 1
        else:
            return mid
    return -1

l = [2, 4, 5, 6, 8, 9, 44]
item1 = 9
ret = (bin_search(l, item1))

if ret != -1:
    print("the index is", str(ret))
else:
    print("Not found")






