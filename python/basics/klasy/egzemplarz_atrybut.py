# kiedy modelujemy coś pochodzącego ze świata rzeczywistego, to może się okazać, że będziemy dodawać coraz więcej szczegółów do klasy.
# liczba atrybutów i metod będzie rosnąć
# niemniej można będzie też zauważyć, że część z nich w naturalny sposób można wydzielić jako osobną klasę i użyć jako atrybutu w dotychczasowej klasie

# np. dla klasy ElectricCar, jeśli będziemy mieli coraz więcej atrybutów opisujących akumulator, może się okazać, że sensowne będzie wydizelenie klasy Battery

# zastosujmy też przy okazji importowanie modułu w którym mamy już klasę Car

from dziedziczenie import Car

class Battery():

    def __init__(self, battery_size = 70):
        self.battery_size = battery_size

    def describe_battery(self):
        print(self.battery_size)

    # dodajmy nową metodę wykonującą prostą logikę
    def get_range(self):
        if self.battery_size == 80:
            range = 270
        elif self.battery_size == 70:
            range = 240
        return range
    # kiedy będziemy modelować rzeczywiste przypadki zaczniemy się zastanawiać czy metoda get_range powinna znaleźć się w Battery czy może w ElectricCar
    # w tym prostym przypadku może być tutaj, jednak jeśli uzależnimy ją od różnych części samochodu, to sensowne może okazać się jej przeniesienie do klasy ElectricCar
    # kiedy zaczniesz szukać odpowiedzi na tego typu pytania, to znaczy, że wszedłeś na wyższy poziom niż zagadnienie samej składni

class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        # teraz atrybutem będzie nowy obiekt
        self.battery = Battery()

    def fill_gas_tank(self):
        print("To auto nie ma baku")


# każmy utworzyć egzemplarz klasy ElectricCar
car = ElectricCar("Tesla", "Model S", '2016')

# w naszym zamochodzie dostańmy się do jego atrybutu battery, który jest obiektem/egzemplarzem z metodą describe_battery
car.battery.describe_battery()

# może się wydawać, że wykonaliśmy sporo nadmiarowej pracy, ale od tego momentu mamy lepiej uporządkowany kod, który intuicyjnie opisuje rzeczywistość
# oraz wiemy czego się po nim spodziewać, a edytory kodu mogą nam dodatkowo podpowiadać
# oraz możemy rozwijać sam obiekt Battery i wykorzystać go w innym kodzie lub w innej klasie - przez polecenie import