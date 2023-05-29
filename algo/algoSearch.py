def get_idx_linear_search(l, v):
  num = []
  
  for i in range(len(l)):
    if v == l[i]:
      num.append(i)
  
  if len(num) == 0: return None
  return num

  
  
def get_idx_binary_search(l, v):
  pass




l = [6, 7, 8, 8, 9, 6, 0]

op = get_idx_linear_search(l, 0)
print(op)