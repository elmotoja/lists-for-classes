studenci = [[123456, "Anam Kowalski"], [111111, "Kinga Rusin"]]
studenci_slownik = {123456: "Anam Kowalski", 111111: "Kinga Rusin"}

poszukiwany_nr_indeksu = 111112

for s in studenci:
    # s -> [123456, "Anam Kowalski"]
    if s[0] == poszukiwany_nr_indeksu:
        print(s[1])

if poszukiwany_nr_indeksu in studenci_slownik:
    print(studenci_slownik[poszukiwany_nr_indeksu])
