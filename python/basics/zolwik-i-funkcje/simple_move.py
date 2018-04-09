def salata_pod_nogami(zolwik, ograniczenia_planszy):
    return

def przed_nosem_nie_ma_sciany(zolwik, pozycja_salaty):
    return

def idz_do_gory(zolwik):
    zolwik[1] +=1
    return zolwik

def wykonaj_manewr_obrotu(zolwik, ostatni_obrot):
    return

def ruch_zolwia(zolwik, pozycja_salaty, ostatni_obrot, ograniczenia_planszy):
    while przed_nosem_nie_ma_sciany(zolwik, ograniczenia_planszy):
        if salata_pod_nogami(zolwik, pozycja_salaty):
            return "salata zjedzona"
        zolwik = idz_do_gory(zolwik)

    wykonaj_manewr_obrotu(zolwik, ostatni_obrot)



zolwik = [0,0]
pozycja_salaty = [2,1]
ostatni_obrot = 'lewo'
ograniczenia_planszy = [3,2]

print(ruch_zolwia(zolwik, pozycja_salaty, ostatni_obrot, ograniczenia_planszy))