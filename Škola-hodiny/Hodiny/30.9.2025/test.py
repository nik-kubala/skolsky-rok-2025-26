velkost_sachovnice = 8
sachovnica_list = [([0] * 8) for i in range(velkost_sachovnice)]

sachovnica_list[2][6] = 1
for riadok in sachovnica_list:
    print(riadok)

def check(x:int, y:int):
    for index in range(velkost_sachovnice):
        if sachovnica_list[y][index] == 1 or sachovnica_list[index][x] == 1: #1. riadok kde je kráľovná 2. stĺpec
            return False
        