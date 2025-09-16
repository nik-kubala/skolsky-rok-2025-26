import json

fr = open("Hodiny/12.9.2025/effectiveness.json", "r")
data = json.load(fr)
attack_list = {}

def hodnota_utoku(nieco:str) -> float:
    if nieco == "super effective":
        return 2
    if nieco == "normal effective":
        return 1
    if nieco == "not very effective":
        return 0.5
    else:
        return 0

for effektivita_str, attacker_slov in data.items():
    ciselko = hodnota_utoku(effektivita_str)
    for attacker, defenders_list in attacker_slov.items():
        if attacker not in attack_list:
            attack_list[attacker] = {}
        for defender in defenders_list:
            attack_list[attacker][defender] = ciselko

def vypocet_sily(utocnik, obranca):
    if len(utocnik) == 2:                           
        if len(obranca) == 2:                                       #ak sa utocnik rovna 2 a obranca 2
            temp = []
            for pokemon_utociaci in utocnik:
                temp.append(attack_list[pokemon_utociaci][obranca[0]] * attack_list[pokemon_utociaci][obranca[1]])
            sila_utociacich += max(temp)
        else:                                                       #ak sa utocnik rovna 2 a obranca 1
            temp = []
            for pokemon_utociaci in utocnik:
                temp.append(attack_list[pokemon_utociaci][obranca[0]])
            sila_utociacich += temp[0] * temp[1]
    else:
        if len(obranca) == 2:                                       #ak sa utocnik rovna 1 a obranca 2
            sila_utociacich += attack_list[utocnik][obranca[0]] * attack_list[utocnik][obranca[1]]
        else:                                                       #ak sa utocnik rovna 1 a obranca 1
            sila_utociacich += attack_list[utocnik][obranca[0]]
    return sila_utociacich

utociaci = []
braniaci = []
def attack(N1:int, N2:int, list_pokemonov:str):
    global utociaci
    global braniaci
    temp = list_pokemonov.split(",")
    for index, pokemon in enumerate(temp):              #jednoduchsie pouzit utociaci = temp[N1:]
        if index in range(0, N1):                       #                    braniaci = temp[:N1]
            utociaci.append(pokemon.split())
        else:
            braniaci.append(pokemon.split())

    for utocnik in utociaci:
        for branik in braniaci:
            vypocet_sily(utocnik, branik)
    print(vypocet_sily)

attack(2,6,"Psychic Dark,Fire,Ghost Ice,Fairy Electric,Normal Steel,Ghost,Poison Fire,Dark Bug")
#sila_utoku()
# print(attack_list["Water"]["Ground"])
# print(attack_list["Water"]["Rock"])