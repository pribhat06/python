# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5 between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
# Hints: Consider using range(#begin, #end) method

'''class Solution:
  def div_non_div_num(self):
    l = []
    for i in range(2000 , 3201): 
      if i%7 == 0 and i%5 != 0: 
        l.append(i)
    return l
                     
obj1 = Solution()
ret = obj1.div_non_div_num()
print(", ".join(str(i) for i in ret))'''


# Question
# Write a program which can compute the factorial of a given number.
# Input: 8
# Output: 40320


'''def factorial(n):
  if (n==0 or n==1):
    return 1
  else:
    return n * factorial(n-1)
  

print(factorial(3))
print(factorial(9))

def factorial(n):
  if (n==0): return 1
  return n * factorial(n-1)
  

print(factorial(2))
print(factorial(5))'''


#fibonacci series 
# The Fibonacci numbers are the numbers in the following integer sequence.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
# In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation 

# f0 = 0
# f1= 1
# f2 = f0 +f1
# f3 = f2+f1
# fn = f(n-1) + f(n-2)


'''def fib(n):
  if (n<= 0):
    return 0
  elif(n ==1 or n ==2):
    return 1
  else:
    return fib(n - 1) + fib(n-2)


print(fib(8))'''

    
# With a given integral number n, write a program to generate a dictionary that contains (i, i*i).
# Input: 8
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

'''class Key_Value:
    def input_k_v(self):
        n = int(input("Print your number!"))
        d = {}
        for x in range(1, n+1):
            d[x] = x**x
        print(d)
    
    
    
obj1 = Key_Value()
ans = obj1.input_k_v()'''



# Question
# Write a program which accepts a sequence of comma-separated numbers from the console and generates a list and a tuple which contains every number.
# Input: 34,67,55,33,12,98
# Output:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

'''class Sequence:
    def new_list_tuple(self):
        n = (input("Print your Sequence here!"))
        l = n.split(",")
        t = tuple(l)
        print(l)
        print(t)
    
obj1 = Sequence()
ans = obj1.new_list_tuple()'''

# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# If no console input is provided, display a default msg : Please provide a Console Input.
# Input: This is an input string.
# Output: THIS IS AN INPUT STRING.
# Hints: Use __init__ method to construct some parameters.


'''class InOutString(Object):
    def __init__(self):
        self.s = ""
    def getString(self):
        print(input("type here!"))
        
    def printString(self):
        

strObj = InOutString()
strObj.getString()
strObj.printString()'''

        
        
# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world
# Hints: In case of input data being supplied to the question, it should be assumed to be a console input.
        
class SortedWord:
    def sorted_list(l):
        str = input ("Enter your word_list")
        words = [word.lower() for word in str.split()]
        words.sort()
        for word in words:
            print(word)

    def upper_line(l):
        str = input("Enter the line")
        main = str.upper()
        print(main)


    
    
          
        
obj1 = SortedWord()
obj1.sorted_list()
obj1.upper_line()



# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT











        
              




    

