def init_world(size):
    world = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(' ')
        world.append(row)
    return world

def print_world(world):
    for row in world:
        print(row)

# direction - g/d/l/p - wskazuje kierunek poruszania żółwia
# poz_i - aktualna pozycja żółwia w "osi i" 
# poz_j - aktualna pozycja żółwia w "osi j"
# world - referencja na świat, w którym porusza się żółw 
# trace:boolean (True/False) - czy żółw pozostawia ślad czy nie
def move_tutle(direction, poz_i, poz_j ,world, trace):
    if not trace:
        world[poz_i][poz_j] = ' '

    if direction == 'g':
        poz_i -= 1
    elif direction == 'd':
        poz_i += 1
    elif direction == 'p':
        poz_j +=1
    elif direction == 'l':
        poz_j -= 1
    
    world[poz_i][poz_j] = 'z'
    print_world(world)

    return poz_i, poz_j


def init_turtle_in_world(world):
    poz_i = 0
    poz_j = 0
    world[poz_i][poz_j] = 'z'
    return poz_i,poz_j

# program
size = int(input("Podaj rozmiar świata: "))
world = init_world(size)
poz_i, poz_j = init_turtle_in_world(world)
line = input("Ruch w stronę (g - góra ,d - dół,l - lewo,p - prawo): ")
while line:
    poz_i, poz_j = move_tutle(line, poz_i, poz_j, world, True)
    line = input("Ruch w stronę (g - góra, d - dół, l - lewo, p - prawo): ")