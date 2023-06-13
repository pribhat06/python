def linear_search(arr, item):
  ret = []
  for i in range(len(arr)):
    if arr[i] == item:
      ret.append(i)
  return ret

l = [2, 3, 7, 5, 7, 9, 10]
item = 7
print(linear_search(l, item))

