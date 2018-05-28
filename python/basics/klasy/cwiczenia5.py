import random

class Die():

    def __init__(self, sides = 6):
        self.sides = sides

    def roll_die(self):
        return random.randint(0, self.sides)

die = Die()
line = True
while line:
    line = input("Jeśli mam rzucić kostką wpisz cokolwiek: ")

throw = True
no_of_throws = 0
while throw:
    throw = die.roll_die()
    print(throw)
    no_of_throws += 1

print("Liczba rzutów: ", no_of_throws)