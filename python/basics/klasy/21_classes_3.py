# praca z klasami
# kiedy już przygotujesz definicje klas, to większość czasu w kodzie będziesz spędzać z ich instancjami/obiektami

# przygotowanie metodwyświetlających lub modyfikujących atrybuty (zamiast modyfikować je bezpośrednio) 

# wyświetlanie

class Car():
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_descriptive_name(self):
        full_name = self.make + ' ' + self.model
        return full_name.title()


# dodajmy atrybut którego wartość zmienia się w czasie

class Car2():
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.meter = 0 # zauważmy, że nie będziemy musieli podawać wartości przy konstrukcji - atrybutowi nadana zostanie wartość domyślna

    def get_descriptive_name(self):
        full_name = self.make + ' ' + self.model
        return full_name.title()

    def read_meter(self):
        print("Ten samochód ma przejechane", self.meter, "km")

    def update_meter(self, new_value):
        self.meter = new_value

    def update_meter_smart(self, new_value):
        """ modyfikacja licznika ze specjalną logiką """
        if new_value < self.meter:
            print("Nie można cofnąć licznika")
        else:
            self.meter = new_value

    def drive(self, range):
        """ modyfikacja licznika pośrednio - uwzględniając logikę ruchu auta """
        self.meter += range


car = Car2("Audi", "A4")
car.read_meter()

# modyfikacja bezpośrednia atrybutu
car.meter = 50
car.read_meter()

# modyfikacja przez metodę
car.update_meter(50)
car.read_meter()

# modyfikacja przez metodą bezpiecznie modyfikującą licznik - uniemożliwia jego cofnięcie
car.update_meter_smart(50)
car.update_meter_smart(150)
car.read_meter()

# modyfikacja licznika pośrednio - przez poruszanie auta o pewną liczbę km - nie musimy nic wiedzieć o tym jak działa licznik
car.drive(50)
car.read_meter()