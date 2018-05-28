
osoby = {}
imiona = []
mca_zamieszkania = []
mca_studiow = []

imie = input("imie")
mce_zam = input("miejsce zamieszkania")
mce_stud = input("miejsce studiów")

imiona.append(imie)
mca_zamieszkania.append(mce_zam)
mca_studiow.append(mce_stud)

osoba = Osoba(imie, mce_zam, mce_stud)
lista_osoby.append(osoba)
slownik_osoby[osoba.imie] = osoba

for osoba in lista_osoby:
    if osoba.imie == "Zbigniew":
        miejsce = osoba.mce_zam




osoby[imie] = [mce_zam, mce_stud]

print(slownik_osoby["Zbigniew"].mce_zam)
print(osoby["Zbigniew"][0])

for imie in imiona:
    if imie == "Zbigniew":
    miejsce = mca_zamieszkania[imiona.index(imie)]

print("Zbigniew mieszka w " + miejsce)

print(okresl_odleglosc_miedzy_miastami(line2, line3))



class Osoba():
    def __init__(self, wiek, imie):
        self.wiek = wiek
        self.imie = imie
        
    def czy_pelnoletnia(self):
        if self.wiek>=18:
            return True
        else:
            return False

line = input("wiek")
zbigniew = Osoba(int(line), "Zbigniew")
print(zbigniew.wiek)
if zbigniew.czy_pelnoletnia():
    print("pełnoletnia")

ola = Osoba(22, "Ola")
genowefa = Osoba(70, "Genowefa")