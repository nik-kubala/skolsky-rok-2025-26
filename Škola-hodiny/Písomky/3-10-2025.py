def skok(vstup):
    with open(vstup, "r", encoding = "UTF-8") as fr:
        nacitane_riadky = fr.readlines()
    
    zoznam = []
    for riadok in nacitane_riadky:
        meno, krajina, s1, s2, s3, s4, s5 = riadok.split()
        temp_slovnik = {
            "meno": meno,
            "krajina": krajina,
            "naj_skok": int(max(s1, s2, s3, s4, s5))
        }
        zoznam.append(temp_slovnik)
    
    krajiny_pocet = {}
    for riadok in zoznam:
        if riadok["krajina"] not in krajiny_pocet:
            krajiny_pocet[riadok["krajina"]] = 1
        else:
            krajiny_pocet[riadok["krajina"]] += 1
    
    zoznam_krajin_str = (", ").join(list(krajiny_pocet.keys()))
    print(f"Zúčastnené krajiny: {zoznam_krajin_str}.")
    for krajina, pocet in krajiny_pocet.items():
        print(f"Z krajiny {krajina} sa zúčasnilo {pocet} športovcov.")
    
    max_skok = max(zoznam, key = lambda zaznam: zaznam["naj_skok"])
    for sutaziaci in zoznam:
        if sutaziaci["naj_skok"] == max_skok["naj_skok"]:
            print(f"Najlepší skokan je {sutaziaci["meno"]} so skokom dlhým {sutaziaci["naj_skok"]} cm.")
    
    
vstup = "Písomky/skok_do_dialky.txt"
skok(vstup)