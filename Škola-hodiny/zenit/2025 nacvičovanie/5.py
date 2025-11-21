inp = input()

def opica():
    try:
        otvaracie = "([{"
        zatvaracie = ")]}"
        zoznam = []
        for znak in inp:
            if znak in otvaracie:
                zoznam.append(znak)
            else:
                ind = zatvaracie.index(znak)
                if otvaracie[ind] != zoznam[-1]:
                    return False
                else:
                    zoznam.pop(-1)
        if len(zoznam) == 0:
            return True
        else:
            return False
    except IndexError:
        return False

if opica():
    print("ano")
else:
    print("nie")