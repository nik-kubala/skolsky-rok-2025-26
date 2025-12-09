from .warrior import Warrior

class Vampire(Warrior):
    def __init__(self, health: int = 40, attack: int = 4, vampirism: int = 50):
        super().__init__(health, attack)
        self.vampirism: int = vampirism
    
    def hit(self, other) -> None:
        real_damage_dealt = other.odpocitaj_damage(self.attack)
        self.health += real_damage_dealt * self.vampirism // 100
    
        if other.health <= 0:
            other.is_alive = False