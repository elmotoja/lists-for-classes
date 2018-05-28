""" Próba zamodelowania psa """	
class Pies():
    
    def __init__(self, imie, wiek):
        """ Inicjalizacja atrybutów name i age """
        self.imie = imie
        self.wiek = wiek

    def siad(self):
        print("Pies siedzi")
    
    def przewrot(self):
        print("Pies leży na plecach")


pies = Pies('Ares', 6) # konwencja - duża litera oznacza klasę - tutaj Dog - a mała instancję/egzemplarz klasy - tutaj pies
print(pies)
# dostęp do atrybutów obiektu
print("pies ma na imię", pies.imie, "i ma", pies.wiek, "lat") # odwołanie do atrybutów obiektu/instancji/egzemplarza przez notację kropkową
# wywołanie metod obiektu - pamiętajmy o nawiasach!!! - to odróżnia wywołania metod od dostępu do wartości atrybutów
pies.siad()
pies.przewrot()
# jeśli nazwy atrybutów i metod są wystarczająco czytelne, to możemy łatwiej odczytywać sens kodu

# można wielokrotnie stosować notację z kropką dla kolejnych elementów
pies.imie.upper() # najpierw dostajemy dostęp do atrybutu obiektu pies, który - ponieważ jest ciągiem znaków - może zostać zamieniony na duże litery przez wywołanie metody upper()
# zauważmy na moment, że klasa Dog nie ma metody upper() - jest to metoda wbudowana w język Python, zdefiniowana dla ciągów znaków (kryje się za tym większa tajemnica, ale o tym kiedy indziej)

# możemy utworzyć kolejną instancję klasy pies i mieć wiele takich obiektów niezależnie, każdy z własnymi atrybutami
inny_pies = Pies("Azor", 2)

# nawet jeśli użylibyśmy tego samego imienia dla obu psów, to Python i tak utworzy osobne obiekty
# może to być przydatne jeśli chcielibyśmy przechowywać wiele obiektów na liście lub w słowniku - nawet z takimi samymi nazwami będą rozróżnialne jako inne obiekty
