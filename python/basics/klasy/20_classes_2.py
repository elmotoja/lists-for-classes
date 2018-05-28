class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name, self.cuisine_type)

    def open_restaurant(self):
        print("godziny pracy")


res = Restaurant("addagio", "italian")
res2 = Restaurant("miraggio", "italian")
res3 = Restaurant("la siesta", "mexican")
res.describe_restaurant()
res2.describe_restaurant()
res3.describe_restaurant()

# Zadanie:
# utwórz klasę User i zdefiniuj 2 atrybuty: first_name i last_name, a następnie kilka innych atrybutów opisujących zwykle użytkownika
# zdefiniuj metodę describe_user() która wyświetli jego atrybuty
# zdefiniuj metodę greet_user(), która przywita go jego imieniem i nazwiskiem
# utwórz kilka różnych egzemplarzy klasy User i wywołaj dla nich obie metody 
