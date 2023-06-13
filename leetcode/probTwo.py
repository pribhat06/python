# You start with an array A of size N. 
#Initially all elements of the array A are zero. 
#You will be given K positive integers. Let j be one of these integers,
# you have to add 1 to all A[i], where i ≥ j. Your task is to print the array A after all these K updates are done.
# Note: 1-based indexing is used everywhere in this question.

a = [0, 0, 0]

updates = [1, 1, 2, 3]
j = 1

for j in updates:
    for i in range(j-1, len(a)):
        a[i] += 1

print(a)


