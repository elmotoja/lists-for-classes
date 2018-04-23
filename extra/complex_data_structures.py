# list of lists (2 dimensional list)

# "setting up" a list of lists
table = []
for i in range(6):
  row = []
  for j in range(6):
    row.append(0)
  table.append(row)

for row in table:
  print(row)

# sidenote: using "random" *module*:
import random # imports the "random" module
no = random.randrange(5) # gets a random number from specified range (0 to ...)

# mapping dictionary keys to structures more complex that basic data types
# dictionaries can also be used to map to more complicated data structures, such as lists, tuples and even dictionaries! 
places = {'buried treasure': (2, 5), 'frisbee': (1, 1)}
print(places['buried treasure'])
places['frisbee'] = (3, 3)
print(places)

# unpacking tuples
# if we threw the frisbee two more squares to the right, we could update the value like this:
places = {'treasure': (2,5), 'frisbee': (1, 1)}
x, y = places['frisbee']
places['frisbee'] = (x, y + 2)
print(places)


# dictionary of lists
# example

flavours = {}
line = input('name and flavour: ')
while line:
  name, flavour = line.split()
  if flavour not in flavours:
    # add it to our dictionary as a list with one element
    flavours[flavour] = [name]
  else:
    flavours[flavour].append(name)
  line = input('name and flavour: ')

for flavour in flavours:
  print(flavour, ':', ' '.join(flavours[flavour]))

# dictionary of dictionaries
# example - a program that tells who wins the rock-paper-scissors game
RULES = {
  'scissors': {
    'scissors': 'tie',
    'paper': 'scissors',
    'rock': 'rock',
  }, 
  'paper': {
    'scissors': 'scissors',
    'paper': 'tie',
    'rock': 'paper',
  },
  'rock': {
    'scissors': 'rock',
    'paper': 'paper',
    'rock': 'tie',
  },
}

print('scissors v.s. rock is won by:', RULES['scissors']['rock'])

# ... or we could use a complex (tuple) key, and then the same task would be solved like this:
RULES = {
  ('scissors', 'scissors') : 'tie',
  ('scissors', 'paper'): 'scissors',
  ('scissors', 'rock'): 'rock',
  ('paper', 'scissors'): 'scissors',
  ('paper', 'paper'): 'tie',
  ('paper', 'rock'): 'paper',
  ('rock', 'scissors'): 'rock',
  ('rock', 'paper'): 'paper',
  ('rock', 'rock'): 'tie',
}

print('scissors v.s. rock is won by:', RULES[('scissors','rock')]) # notice that this time we use tuple notation in the argument

# removing duplication
# notice that RULES[('rock','scissors')] or RULES[('scissors','rock')] gets us the same result
RULES = {
  ('scissors', 'scissors') : 'tie',
  ('scissors', 'paper'): 'scissors',
  ('scissors', 'rock'): 'rock',
  ('paper', 'paper'): 'tie',
  ('paper', 'rock'): 'paper',
  ('rock', 'rock'): 'tie'
}

hand1 = 'rock'
hand2 = 'scissors'
if (hand1, hand2) in RULES:
  winner = RULES[(hand1, hand2)]
else:
  winner = RULES[(hand2, hand1)]
print(hand1, 'v.s.', hand2, 'won by:', winner) 

# further "simplification"
# if the two hands were the same, the result is always a tie. 

RULES = {
  ('scissors', 'paper'): 'scissors',
  ('paper', 'rock'): 'paper',
  ('rock', 'scissors'): 'rock',
}

hand1 = 'rock'
hand2 = 'scissors'
winner = RULES.get((hand1, hand2), RULES.get((hand2, hand1), 'tie')) # a very interesting shortened notation
print(hand1, 'v.s.', hand2, 'won by:', winner) 

# is the code above really a "simplification" of the previous one - why?? (maintenance, less data, code that describes the thought process and not just gets the data)
