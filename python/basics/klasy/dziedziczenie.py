# gdy jedna klasa dziedziczy po innej automatycznie pobiera wszystkie atrybuty i metody z klasy po której dziedziczy (klasy nadrzędnej / superklasy)
# klasa dziedzicząca to inaczej klasa potomna
# klasa potomna może definiować także nowe atrybuty i metody

# gdy tworzymy egzemplarz klasy, to najpierw musimy uzupełnić atrybuty klasy nadrzędnej

# weźmy najpierw klasę Car
class Car():
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.meter = 0 # zauważmy, że nie będziemy musieli podawać wartości przy konstrukcji - atrybutowi nadana zostanie wartość domyślna

    def get_descriptive_name(self):
        full_name = self.make + ' ' + self.model
        return full_name.title()

    def fill_gas_tank(self):
        print("Napełniono bak")

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

# i utwórzmy dziedziczącą po niej klasę ElectricCar

class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)  # tutaj uzupełniamy atrybuty w klasie nadrzędnej - super() wskazuje na klasę nadrzędną
        # już w tym momencie mamy dostęp do tych samych metod i atrybutów co w klasie nadrzędnej - póki co nie czujemy jeszcze przydatności
        # możemy jednak zdefiniować atrybuty właściwe tylko dla samochodu elektrycznego
        self.battery_size = 60

    # oraz metody właściwe tylko tej klasie
    def describe_battery(self):
        print(self.battery_size)

    # możemy też nadpisać (zastąpić) metody z klasy nadrzędnej
    def get_descriptive_name(self):
        full_name = self.make + ' ' + self.model + ' ' + self.battery_size
        return full_name.title()

    # oraz nadpisać takie, które już nie mają sensu - choć warto zastanowić się czy ta metoda w ogóle powinna znaleźć się w klasie nadrzędnej
    def fill_gas_tank(self):
        print("To auto nie ma baku")