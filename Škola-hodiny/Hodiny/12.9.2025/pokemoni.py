import json

fr = open("Škola-hodiny/Hodiny/12.9.2025/effectiveness.json", "r")
data = json.load(fr)
attack_list = {}

def attack_number(power:str) -> float:
    if power == "super effective":
        return 2                                  #staci tu if lebo ak sa spusti return, funkcia sa vypne
    if power == "normal effective":
        return 1
    if power == "not very effective":
        return 1/2 
    else:
        return 0

for effectivity in data:
    for attacker in data[effectivity]:
        if attacker not in attack_list:
            attack_list[attacker] = {}
        for defender in data[effectivity][attacker]:
            # if attacker not in attack_list:
            #     attack_list[attacker] = {}
            # else:
            #     attack_list[attacker] 
print(attack_list)
    
#print(data)