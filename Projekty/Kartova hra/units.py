# UNITS A ARMY LOGIKA #
class Warrior:
    def __init__(self, health: int = 50, attack: int = 5) -> None:
        self.health: int = health
        self.attack: int = attack
        self.is_alive: bool = True
    
    def hit(self, other) -> None:
        other.odpocitaj_damage(self.attack)

        if other.health <= 0:
            other.is_alive = False
    
    def odpocitaj_damage(self, damage: int) -> int:
        self.health -= damage
        return damage
    
    def __str__(self) -> str:
        return f"Zdravie: {self.health}, Útok: {self.attack}, Žijem: {self.is_alive}, Typ: {self.__class__.__name__}"

class Knight(Warrior):
    def __init__(self, attack: int = 7):
        super().__init__(50, attack)

class Defender(Warrior):

    def __init__(self, health: int = 60, attack: int = 3, defense: int = 2):
        super().__init__(health, attack)
        self.defense: int = defense
    
    def odpocitaj_damage(self, damage: int) -> int:
        if damage > self.defense:
            real_damage = damage - self.defense
        else:
            real_damage = 0
        super().odpocitaj_damage(real_damage)
        return real_damage

class Vampire(Warrior):
    def __init__(self, health: int = 40, attack: int = 4, vampirism: int = 50):
        super().__init__(health, attack)
        self.vampirism: int = vampirism
    
    def hit(self, other) -> None:
        real_damage_dealt = other.odpocitaj_damage(self.attack)
        self.health += real_damage_dealt * self.vampirism // 100

        if other.health <= 0:
            other.is_alive = False
        
class Army:
    def __init__(self):
        self.warriors: list = []
    
    def add_units(self, unit: type, count: int):
        for _ in range(count):
            self.warriors.append(unit())

# Ceny postáv
UNIT_PRICES = {
    Warrior: 20,
    Knight: 30,
    Defender: 35,
    Vampire: 40,
}