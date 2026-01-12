import random

class Stvorenie:
    pravidlo = 5 # Pravidlo, ktoré príšerky sú najlepšie

    def __init__(self, generacia = 0):
        self.dna: list[int] = []
        self.stamina: int = 0
        self.generacia = generacia
        if generacia == 0:
            self.dna = [random.randrange(0, 10) for _ in range(10)]
            self.dna.sort(reverse = True)
        self.stamina = self.dna.count(self.pravidlo)
    
    def __str__(self):
        return f"Stvorenie generacie: {self.generacia}\nDNA:    {self.dna}\nStamina: {self.stamina}"
    
    def __add__(self, other):
        bejby = Stvorenie(self.generacia + 1)
        bejby.dna = []
        for poradie_chromozomu in range(len(self.dna)):
            hod_kockou = random.random() # Buď 1 alebo 0
            if hod_kockou < 0.9: # 90% pravdepodobnosť či bejby pridá z dna rodičov
                bejby.dna.append(random.choice([self.dna[poradie_chromozomu], other.dna[poradie_chromozomu]]))
            else:
                bejby.dna.append(random.randrange(0, 10)) # 10% pravdepodobnosť či bude mutácia 
        bejby.stamina = bejby.dna.count(self.pravidlo)
        bejby.dna.sort(reverse = True)
        
        return bejby

kmen = []

for i in range(10):
    kmen.append(Stvorenie())

kmen.sort(key=lambda stvorenie: stvorenie.stamina, reverse=True)

for stvorenie in kmen:
    print(stvorenie)
    print("----------------")

kmen = kmen[:5]

def mnozenie(mnozenie):
    global kmen
    mnozenie += 1
    kmen = kmen[:5]
    for i in range(5):
        kmen.append(kmen[random.randrange(0, 5)] + kmen[random.randrange(0, 5)])
    kmen.sort(key=lambda stvorenie: stvorenie.stamina, reverse=True)
    
    print("!!!!!!!!!!!!!!!!!!!")
    print(f"Toto je množenie číslo {mnozenie}")
    print("!!!!!!!!!!!!!!!!!!!")
    for index, stvorenie in enumerate(kmen, 1):
        print(f"Poradie v kmeni: {index}")
        print(stvorenie)
        print("----------------")

for pocet_mnozeni in range(10000):
    mnozenie(pocet_mnozeni)