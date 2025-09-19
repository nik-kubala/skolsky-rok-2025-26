def faktorial(n:int) -> int:
    vysledok = 1
    for index in range(n, n + 1):
        vysledok *= index
    return vysledok
#print(faktorial(10))

#du sucin pomocou rekurzie

def sucet(a, b):
    if b == 0:
        return a
    else:
        return 1 + sucet (a, b - 1)
#print(sucet(3, 4))

def sucin(a, b):
    if b == 1:
        return a
    else:
        return a + sucin(a, b - 1)
#print(sucin(3, 4))

def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)
#print(fibo(3))

dajaky_zoznam = [[[9, 1], 4], 7, [2, [3, [6, 5]], 8], [1], [[4], [[2]]]]
vysledok = []
def zoznamovka(zoznam):
    global vysledok
    for item in zoznam:
        if type(item) == int:
            vysledok.append(item)
        else:
            zoznamovka(item)
# zoznamovka(dajaky_zoznam)
# print(vysledok)