# greatest and smallest number list

'''def chk_empty_list(l):
  if len(l) == 0:
    print("!! ERROR : List is empty")
    return True


def get_largest_smallest(l):
  if chk_empty_list(l): return None, None
  
  large = l[0]
  small = l[0]

  for i in l:
    if i > large:
      large = i
    elif i < small:
      small = i

  return large, small


def get_sum(l):
  pass


def get_avg(l):
  if chk_empty_list(l): return None
  
  return get_sum(l)/len(l)
  
    
l = [2, 2, 8, 76, 564, 626, 28, 42, 9]  
l1= []

avg = get_largest_smallest(l1)
print(avg)




  



l1 = [2, 2, 8, 76, 564, 626, 28, 42, 9]
l2 = []
l3 = [-1]
l4 = [0, 0, 0]'''

#lrg, sml = get_largest_smallest(l2)
#print(lrg, sml)



# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# non-integer elems

# l = [12, "abc", 19j, 42, "81"]


'''def non_int_elem(l):
    pass

l = [1, "81", "abc", "31l", 54]

int_num = []
non_int_num = []
num =  l[0]



for i in l:
    if i == int(i):
        num = i
    else:
        non_int_num.append(i)'''


a = ['111', 213, 74, '99', 't', '88', '-74', -74]

def detect(list_):
    for element in list_:
        try:
            int(element)
        except ValueError:
            return False
    return True

print(detect(a))
    





        
           
        


    