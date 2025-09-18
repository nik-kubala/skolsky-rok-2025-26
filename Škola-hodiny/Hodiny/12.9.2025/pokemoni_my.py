import json

fr = open("Hodiny/12.9.2025/effectiveness.json", "r")
data = json.load(fr)
attack_list = {}

# Pomocná funkcia na preklad textovej efektivity na číselnú hodnotu.
def hodnota_utoku(nieco:str) -> float:
    if nieco == "super effective":
        return 2
    if nieco == "normal effective":
        return 1
    if nieco == "not very effective":
        return 0.5
    else:
        return 0

# Spracovanie načítaného JSON-u do prehľadnejšej štruktúry: attack_list[utocnik][obranca] = sila
for effektivita_str, attacker_slov in data.items():
    ciselko = hodnota_utoku(effektivita_str)
    for attacker, defenders_list in attacker_slov.items():
        if attacker not in attack_list:
            attack_list[attacker] = {}
        for defender in defenders_list:
            attack_list[attacker][defender] = ciselko

# Vypočíta silu jedného súboja podľa počtu typov útočníka a obrancu.
def vypocet_sily(utocnik, obranca):
    # Prípad, keď útočí dvoj-typový pokémon.
    if len(utocnik) == 2:                           
        # Útok 2 vs 2: slabosti obrancu sa násobia, útočník použije lepší typ.
        if len(obranca) == 2:
            temp = []
            for pokemon_utociaci in utocnik:
                temp.append(attack_list[pokemon_utociaci][obranca[0]] * attack_list[pokemon_utociaci][obranca[1]])
            return max(temp)
        # Útok 2 vs 1: útočník použije lepší z dvoch typov.
        else:
            temp = []
            for pokemon_utociaci in utocnik:
                temp.append(attack_list[pokemon_utociaci][obranca[0]])
            return max(temp)
    # Prípad, keď útočí jedno-typový pokémon.
    else:
        # Útok 1 vs 2: efektivita proti obom typom obrancu sa násobí.
        if len(obranca) == 2:
            return attack_list[utocnik[0]][obranca[0]] * attack_list[utocnik[0]][obranca[1]]
        # Útok 1 vs 1: priamy zápis sily.
        else:
            return attack_list[utocnik[0]][obranca[0]]

# Porovná dve sily a vráti reťazec s výsledkom.
def vitaz(N1:int, N2:int) -> str:
    if N1 > N2:
        return "ME"
    elif N1 < N2:
        return "FOE"
    else:
        return "EQUAL"

# Hlavná funkcia, ktorá rozdelí tímy a simuluje súboj.
def attack(N1:int, N2:int, list_pokemonov:str):
    utociaci = []
    braniaci = []
    # Rozdelenie vstupného reťazca na zoznamy tímov.
    temp = list_pokemonov.split(",")
    for index, pokemon in enumerate(temp):
        if index in range(0, N1):
            utociaci.append(pokemon.split())            #jednoduchsie pouzit utociaci = temp[N1:]
        else:                                           #                    braniaci = temp[:N1]
            braniaci.append(pokemon.split())

    celkova_sila_N1 = 0
    celkova_sila_N2 = 0
    # Simulácia obojsmerného súboja: tím1 útočí na tím2 A zároveň tím2 na tím1.
    for utocnik in utociaci:
        for branik in braniaci:
            celkova_sila_N1 += vypocet_sily(utocnik, branik)
            celkova_sila_N2 += vypocet_sily(branik, utocnik)

    # Funkcia vráti výsledky ako trojicu hodnôt (tuple).
    return celkova_sila_N1, celkova_sila_N2, vitaz(celkova_sila_N1, celkova_sila_N2)

# Zavolanie funkcie a "rozbalenie" jej výsledkov do 3 samostatných premenných.
sila_N1, sila_N2, vysledok = attack(2,6,"Psychic Dark,Fire,Ghost Ice,Fairy Electric,Normal Steel,Ghost,Poison Fire,Dark Bug")

print(f"{sila_N1}, {sila_N2}, {vysledok}")