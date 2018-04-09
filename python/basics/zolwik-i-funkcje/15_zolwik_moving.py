world = []
size = int(input("Podaj rozmiar świata: "))

for i in range(size):
    row = []
    for j in range(size):
        row.append(str(i) + str(j))
    world.append(row)

for row in world:
    print(row)

line = input("Ruch w stronę (g - góra ,d - dół,l - lewo,p - prawo): ")

for i in range(size):
    for j in range(size):
        world[i][j] = ' '

poz_i = 0
poz_j = 0
world[poz_i][poz_j] = 'z'

while line:
    if line == 'g':
        poz_i -= 1
    elif line == 'd':
        poz_i += 1
    elif line == 'p':
        poz_j +=1
    elif line == 'l':
        poz_j -= 1
    world[poz_i][poz_j] = 'z'
    for row in world:
        print(row)
    line = input("Ruch w stronę (g - góra ,d - dół,l - lewo,p - prawo): ")