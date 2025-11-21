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
        super().__init__(50, attack)        # volanie konštruktora z predchádzajúcej triedy
        self.is_alive: bool = True

class Defender(Warrior):

    def __init__(self, health: int = 60, attack: int = 3, defense: int = 2):
        super().__init__(health, attack)
        self.defense: int = defense
    
    def odpocitaj_damage(self, damage: int) -> int:
        if damage > self.defense:
            real_damage = damage - self.defense
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
        for i in range(count):
            self.warriors.append(unit())

class Battle:
    
    def fight1v1(self, warrior1: Warrior, warrior2: Warrior) -> bool:
        while warrior1.is_alive:
            
            warrior1.hit(warrior2)
        
            print(f"Dostáva bomby warrior2: {warrior2}")
            
            if not warrior2.is_alive:
                return True
            else:
                warrior2.hit(warrior1)
                print(f"Dostáva bomby warrior1: {warrior1}")
        
        return False
    
    def fight(self, army1: Army, army2: Army) -> bool:
        while len(army1.warriors) > 0 and len(army2.warriors) > 0:
            if self.fight1v1(army1.warriors[0], army2.warriors[0]):
                army2.warriors.pop(0)
                print("Zomrel gadžo z army2")
            else:
                army1.warriors.pop(0)
                print("Zomrel gadžo z army1")
        
        if len(army1.warriors) > 0:
            print("VYHRAL ARMY 1")
            return True
        else:
            print("VYHRAL ARMY 2")
            return False




# battle tests
my_army = Army()
my_army.add_units(Defender, 2)
my_army.add_units(Vampire, 2)
my_army.add_units(Warrior, 1)

enemy_army = Army()
enemy_army.add_units(Warrior, 2)
enemy_army.add_units(Defender, 2)
enemy_army.add_units(Vampire, 3)

army_3 = Army()
army_3.add_units(Warrior, 1)
army_3.add_units(Defender, 4)

army_4 = Army()
army_4.add_units(Vampire, 3)
army_4.add_units(Warrior, 2)

battle = Battle()

assert battle.fight(my_army, enemy_army) == False
assert battle.fight(army_3, army_4) == True
print("Coding complete? Let's try tests!")