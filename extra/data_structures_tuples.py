# So far, we have learnt about lists and dictionaries, and have learnt that lists are useful when the ordering of values is important, and that dictionaries are especially useful for storing key, value pairs. 

# tuples

# Tuples are a data structure in Python which are more or less a read-only list. 
# That is, like strings, tuples are immutable. 
# All of the standard read-only operations that you can perform on a list can be performed on a tuple, including finding its length, slicing, indexing, and unpacking.
# Tuples are notated just like lists, except that the items of the tuple are enclosed in parenthesis instead of square brackets.

times = (43, 45, 49, 52, 55)

# You can convert any sequence type to a tuple using the **tuple** function. 
times1 = [43, 45, 49, 52, 55]
times2 = tuple(times1)

# There is a gotcha to be aware of when creating tuples containing a single element. 
# Python interprets an object surrounded by a single set of parenthesis as grouping parenthesis and just discards them. 
# To create a single element tuple, a trailing comma is needed. 
# The following example demonstrates this:

x = ()         # empty tuple
print(type(x), x)
x = (9, 4, 1)  # 3 element tuple
print(type(x), x)
x = (9,)       # 1 element tuple
print(type(x), x)
x = (9)        # the integer 9
print(type(x), x)

# Because tuples are immutable, an exception is raised if you try to perform a modification operation upon them.
# If you want to modify an element of a tuple, you will need to construct a new tuple and assign the result back to the same variable.

times = (43, 45, 49, 52, 55)
times = times[:2] + (10,) + times[3:]
print(times)

# comparing tuples
# Like most other builtin Python data types, tuples can be compared using the standard comparison operators (<, >, etc).
# Tuples are compared element-wise
# 
# This means that the first item from both tuples are compared. 
# If their values are not equal, then the appropriate tuple is returned. 
# If they are equal, then the second element from both tuples is compared, and this process is repeated.
# 
# A consequence of this is that tuples can only be compared if their pairwise items have the same types. Attempting to compare two objects of different types raises a TypeError


# dictionaries cd... (hashable and unhashable keys)
# It is not uncommon to want to add a collection of items as an element to a set, or use a list as a key in a dictionary. For example, imagine we wanted to keep track of how many times each letter appeared on each line of a file. Ideally, what we'd like to have is a dictionary whose key is the pair of current line number and current word, and whose value then is the frequency of that line/word pair. 
# but a list is not hashable (it is mostly about being mutable)
# this is always the case if we would want to use the dictionary as a function with multiple arguments

# The key in this dictionary does not need to be modifiable however. That is, we never need to resize or modify an item of the key list! This is a perfect case of where **tuples** come in handy.

# example
# In linguistics, a bigram is a pair of adjacent words in a sentence. 
# The sentence The big red ball has three bigrams: The big, big red, and red ball.

line = input("Line: ")
bigrams = {}
while line:
  words = line.split()
  for i in range(0,len(words)-2):
    key = (words[i].lower(),words[i+1].lower())
    if key in bigrams:
      bigrams[key] +=1
    else:
      bigrams[key] =1
  line = input("Line: ")
  
for key in bigrams:
  print(key[0]+" "+key[1]+":",bigrams[key])