def make_pizza(size, *toppings): # przyjmuje parametr pozycyjny size i poźniej dowolną liczbę parametrów, które przypisuje do krotki toppings
    for topping in toppings:
        print(topping)

# Przekazywanie dowolnej, nieznanej wcześniej liczby parametrów typu klucz-wartość

def build_profile(first_name, last_name, **user_info):
    profile = {}
    profile["first name"] = first_name
    profile["last name"] = last_name
    for key, value in user_info.items():
        profile[key] = value
    return profile