def vytazenost_liniek(subor):
    
    with open(subor, "r", encoding = "UTF-8") as fr:
        nacitane_riadky = fr.readlines()
    
    max_kapacita = int(nacitane_riadky[0].strip())
    
    zastavky_zoznam = []
    for riadok in nacitane_riadky[1:]:
        nastupujuci, vystupujuci, nazov_zastavky = riadok.strip().split(" ", 2)
        zastavky_slovnik = {
            "Počet_nastupujúcich": int(nastupujuci),
            "Počet_vystupujúcich": int(vystupujuci),
            "Názov_zástavky": nazov_zastavky
        }
        zastavky_zoznam.append(zastavky_slovnik)
    
    print(f"Počet zástavok na trase: {len(zastavky_zoznam)}")
    
    nazov_zastavok_zoznam = [zaznam["Názov_zástavky"] for zaznam in zastavky_zoznam]
    nazov_zastavok_str = ", ".join(nazov_zastavok_zoznam)
    print(f"Názvy všetkých zastávok: {nazov_zastavok_str}")
    
    priebezny_pocet = 0
    max_preplnenie = 0
    for zastavenie in zastavky_zoznam:
        priebezny_pocet += zastavenie["Počet_nastupujúcich"]
        priebezny_pocet -= zastavenie["Počet_vystupujúcich"]
        if priebezny_pocet > max_kapacita:
            print(f"Na zastávke {zastavenie["Názov_zástavky"]} je autobus preplnený.")
        if priebezny_pocet > max_preplnenie:
            max_preplnenie = priebezny_pocet
    
    print(f"Maximálne bol autobus preplnený o {max_preplnenie - max_kapacita}.")

subor = "Písomky/bus_vytazenost.txt"
vytazenost_liniek(subor)