def init_world(size):
    world = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(str(i) + str(j))
        world.append(row)
    return world

def clear_world(world):
    for i in range(size):
        for j in range(size):
            world[i][j] = ' '

def print_world(world):
    for row in world:
        print(row)

def move_tutle(direction, poz_i, poz_j):
    if direction == 'g':
        poz_i -= 1
    elif direction == 'd':
        poz_i += 1
    elif direction == 'p':
        poz_j +=1
    elif direction == 'l':
        poz_j -= 1
    return poz_i, poz_j



#start
size = int(input("Podaj rozmiar świata: "))

# populate world
world = init_world(size)

print_world(world)

line = input("Ruch w stronę (g - góra ,d - dół,l - lewo,p - prawo): ")

clear_world(world)

# init tutle in world
poz_i = 0
poz_j = 0
world[poz_i][poz_j] = 'z'

# actual program for turtle movement 
while line:
    poz_i, poz_j = move_tutle(line, poz_i, poz_j) # does it actually move the turle?
    world[poz_i][poz_j] = 'z' # ... or only now the tutrle is moved in the world
    print_world(world)
    line = input("Ruch w stronę (g - góra, d - dół, l - lewo, p - prawo): ")
