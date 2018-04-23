
# TASK 1
# You're running a poll to find out your friends' favourite dessert 
# and decide to write a program to help you keep track of all the suggestions and who voted for each.
# Your program should keep reading in lines (until an empty line) which contain: 
# the person's name, 
# then a colon (:) 
# then their favourite dessert.
# -- like this: Georgina:apple pie


# Your program should keep reading in lines (until an empty line) which contain the person's name, then a colon (:) then their favourite dessert.


line = input("Name:vote ")
desserts = {}
while line:
  name, dessert = line.split(":")
  if dessert in desserts:
    desserts[dessert].append(name)
  else:
    desserts[dessert] = [name]
  line = input("Name:vote ")
  
for dessert in desserts:
  print(dessert, len(desserts[dessert]),"vote(s):", ' '.join(desserts[dessert])) 

# sorting dictionaries
# dictionaries don't store its elements in any particular order
# but we can sort those elements and loop over them in some order
# we use *sorted()* function
phones = {'Louise':'412', 'Jim': '414', 'Teena':'432'}
print(sorted(phones)) 
for name in sorted(phones): #this sorts elements by *keys*
  print(name, phones[name])


# TASK 2 - find a maximum value in a dictionary of numbers

# example

temperatures = {
  'Stockholm': -5, 'Helsinki': -2,
  'Lund': -1, 'Edinburgh': -1,
  'St Petersburg': -4,
}

max_keys = max_val = None
first = True
for city in temperatures:
  if first or temperatures[city] > max_val:
    max_val = temperatures[city]
    max_keys = [city]
    first = False
  elif temperatures[city] == max_val:
    max_keys.append(city)

if first:
  print('The dictionary is empty')
else:
  print('Maximum:', max_val, ', '.join(max_keys))

# using built-in dictionary functions

temperatures = {
  'Stockholm': -5, 'Helsinki': -2,
  'Lund': -1, 'Edinburgh': -1,
  'St Petersburg': -4,
}

if not temperatures: # notice the negation
  print('The dictionary is empty')
else:
  max_val = max(temperatures.values()) # returns the maximum from dictionary's values
  max_keys = []
  for city in temperatures:
    if temperatures[city] == max_val:
      max_keys.append(city)
  print('Maximum:', max_val, ', '.join(max_keys)) 

# sorting by dictionary values
# One option is to construct another dictionary, mapping from values to keys.
cities = {
  'Stockholm': -5, 'Lund': -1,
  'Edinburgh': -1, 'Helsinki': -2,
  'St Petersburg': -4,
}

temperatures = {}
for city in cities:
  temp = cities[city]
  if temp in temperatures:
    temperatures[temp].append(city)
  else:
    temperatures[temp] = [city]

for temp in sorted(temperatures):
  for city in temperatures[temp]:
    print(temp, city)


# TASK 3

# The aim in this question is to find the main characters in a novel by doing textual analysis. We will hypothesise that the most frequent capitalised words in a novel are likely to be the character names.
# You should write a program to open a file called novel.txt and read in all the words. For this purpose let's assume that words are groups of letters and punctuation separated by spaces.
# Your program should then count the number of times each word appears and print out the top 3 words which start with a capital letter.
# You can experiment on other novels freely available from Project Gutenberg (http://www.gutenberg.org/wiki/Main_Page)
# In this question we treat a word as a group of letters and punctuation separated by spaces. This means that Dr and Dr. would count as different words, as would Grok and Grok,. Correctly normalising these examples to the same word is part of the process of tokenisation, but we're not going to worry about that here
# https://en.wikipedia.org/wiki/Tokenization

words = open("novel.txt").read().split()
count = {}
for word in words:
  if word.istitle():
    if word in count:
      count[word] +=1
    else:
      count[word] = 1
    
invcount = {}
for elem in count:
  if count[elem] in invcount:
    invcount[count[elem]].append(elem)
  else:
    invcount[count[elem]] = [elem]

lista = []
for no in sorted(invcount, reverse=True):
  lista.append(no)

for i in range(3):
 print(lista[i], invcount[lista[i]][0])