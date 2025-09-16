import json

fr = open("Hodiny/12.9.2025/effectiveness.json", "r")
data = json.load(fr)
attack_list = {}


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
    return utociaci, braniaci

# def sila_utoku():
#     sila_utociacich = 0
#     for utocnik in utociaci:
#         for branik in braniaci:
#             if len(utocnik) == 2:
#                 sila_utociacich += attack_list[utocnik[0]][branik] * attack_list[utocnik[1]][branik]
#             else:
#                 sila_utociacich += attack_list[utocnik][branik]
#     print(sila_utociacich)



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


attack(2,6,"Psychic Dark,Fire,Ghost Ice,Fairy Electric,Normal Steel,Ghost,Poison Fire,Dark Bug")
#sila_utoku()