from cwiczenia import Restaurant

class IceCreamStand(Restaurant):
    
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def print_flavors(self):
        for flavor in self.flavors:
            print(flavor)


stand = IceCreamStand('X', 'Y', ['vanilla', 'chocolate', 'strawberry'])
stand.print_flavors()