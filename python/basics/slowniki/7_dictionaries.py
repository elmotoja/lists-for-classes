# Dictionaries are a type of data structure in Python that store key: value pairs.
sounds = {'dog': 'a barker', 'cat': 'a meower', 'bird': 'a tweeter'}
print(sounds)

# empty dictionary
dictionary_variable = {}

# Dictionaries are unordered

# Accessing items in a dictionary - dict_variable[key] -> value
print(sounds['dog'])

# Checking if a key is in a dictionary - "in" operator
if 'cat' in sounds:
  print('cat is in the dictionary')

# iterating over dictionary:
for animal in sounds:
  print('a', animal, 'is', sounds[animal])

# in general - in for loop we iterate over dictionary keys - it is good to remember
dictionary = {}
for key in dictionary:
  print(key, dictionary[key])

# Adding and modifying dictionary items
sounds = {'dog': 'a barker', 'cat': 'a meower', 'bird': 'a tweeter'}
animal = 'cat'
sounds['klucz'] = "wartość"
print('A', animal, 'is', sounds[animal])

# Change the cat definition:
sounds['cat'] = 'a purrer'
print('A', animal, 'is now', sounds[animal])

# Add a new definition for mouse:
sounds['mouse'] = 'a squeaker'
animal = 'mouse'
print('A', animal, 'is', sounds[animal])

print('Final dictionary contents:')
print(sounds)

# example - creating dictionary from input
phonebook = {}

line = input('Name and number: ')
while line:
  name, number = line.split() # multiple assignment
  phonebook[name] = number
  line = input('Name and number: ')

print(phonebook)

# prep for next paragraph
d = {} #dictionary
key = 'some key'

# "use a default value if the key is not in the dictionary" pattern is so common, dictionaries provide the get method to do this:
val = d.get(key, 'default')

# so instead :
val = 'default'
if key in d:
   val = d[key]

# you can use:
val = 'default'
if key in d:
  val = d.get(key, 'default')

# example:
sounds = {'dog': 'barks', 'cat': 'meows', 'bird': 'tweets'}

animal = input('Animal: ')
while animal:
  sound = sounds.get(animal, 'makes noise')
  print('A', animal, sound)
  animal = input('Animal: ')

# If you want to copy the key-value pairs from one dictionary to another, Python provides the update method:
d1 = {'a': 1, 'b': 5}
d2 = {'a': 4, 'c': 6}
d1.update(d2)
print(d1)

