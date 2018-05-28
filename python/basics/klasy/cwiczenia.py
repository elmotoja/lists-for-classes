class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name , self.cuisine_type)
    
    def open_restaurant(self):
        print("restauracja jest otwarta w godzinach od 9 do 21")

    def set_number_served(self, no):
        self.number_served = no

    def increment_number_served(self, increment):
        self.number_served += increment


restaurant = Restaurant("Da vinci","italian")
restaurant.describe_restaurant()
