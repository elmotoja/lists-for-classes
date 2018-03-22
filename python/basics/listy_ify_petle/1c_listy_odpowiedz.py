# Zad 1

# korzystając z poniższych zmiennych i operacji na liczbach i ciągach znaków oraz wykorzystując rzutowanie typów
a = "5"
b = 4
c = "3"
# wyświetl napis "543"
print(a+str(b)+c)
# oraz liczbę 23
print(int(a)*b+int(c))


# Zad 2

# wykorzystując listę 
li = [5,2,6,1]

# utwórz listę li2, która ma elementy posortowane rosnąco
li2 = sorted(li)
print(li2)
# utwórz listę li3, która ma najpierw 2 ostatnie elementy li a później dwa pierwsze (zrób to w jednej operacji przypisania)
li3 = li[-2:] + li[:2]
print(li3)
# policz i wyświetl sumę elementów listy
print(sum(li))

# Zad 3

# skorzystaj z list (używając tylko operacji na listach i istniejących elementów)
l1 = [5,2,4]
l2 = [8,16,3]

# żeby utworzyć listę
l3 = [8,5,4,16,3]
l5 = l1[:]
l5.remove(2)
l3 = [l2[0]] + l5 + l2[-2:]
print(l3)

# oraz listę
l4 = [248,54]
l4 = [int(str(l1[1]) + str(l1[2]) + str(l2[0])), int(str(l1[0]) + str(l1[2]))]
print(l4)