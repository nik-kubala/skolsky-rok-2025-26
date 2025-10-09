rozmer = 5
sachovnica = [[0] * rozmer for i in range(rozmer)]

def konik(x, y, n):
    global sachovnica
    if n == rozmer ** 2 + 1:
        for riadok in sachovnica:
            print(riadok)
        print("---------------")
    else:
        if sachovnica[0][0]:
            sachovnica[0][0] = n
            