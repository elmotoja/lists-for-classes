wiek = int(input("podaj wiek: "))
wiek_emerytalny = 75
if wiek >= wiek_emerytalny:
    print("Jesteś w wieku emerytalnym")
    print("cokolwiek")
else:
    print("Nie jesteś w wieku emerytalnym\nPozostało Ci " + str(wiek_emerytalny - wiek) + " lat")
print("")