import random

studenti = [i for i in range(1, int(input("Zadaj počet študentov:")) + 1)]
otazky = [i for i in range(1, int(input("Zadaj počet otázok:")) + 1)]

def miesaj(co,typ_miesania = True):
    velkost = len(co)
    if typ_miesania:                            #nemusim kontrolovst ci je true alebo false, lebo to moze byt len to alebo to
        for pocet in range(velkost**2): 
            i = random.randrange(0, velkost)
            j = random.randrange(0, velkost)
            co[i], co[j] = co[j], co[i]             #Špecialita Pythonu, iný jazyk to nedokáže.
            # temp = co[i]
            # co[i] = co[j]
            # co[j] = temp
    else:  
        parne = [i for i in range(2, len(otazky), 2)]
        neparne = [i for i in range(1, len(otazky), 2)]
        for i in range(0, velkost // 2 - 1):
            co[i * 2] = parne[i]
            co[i * 2 + 1] = neparne[i]

if len(studenti) > len(otazky):
    print("Je málo otázok.")
else:
    miesaj(studenti)
    miesaj(otazky)
    for i in range(len(studenti)):
        print(f"{i + 1}. študent: {studenti[i]}, otázka: {otazky[i]}")