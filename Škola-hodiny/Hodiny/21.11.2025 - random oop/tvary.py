class Tvar():
    def area(self):
        raise NotImplementedError

class Obdlznik(Tvar):
    def __init__(self, sirka, vyska):
        self.sirka = sirka
        self.vyska = vyska
    
    def area(self):
        return self.sirka * self.vyska

class Kruh(Tvar):
    def __init__(self, polomer):
        self.polomer = polomer
    
    def area(self):
        return 3.14 * self.polomer ** 2

class Trojuholnik(Tvar):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def area(self):
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5


troj = Trojuholnik(3, 4, 5)
kruh = Kruh(3)
obdlznik = Obdlznik(1, 2)

objekty = [troj, kruh, obdlznik]

for objekt in objekty:
    print(objekt.area())