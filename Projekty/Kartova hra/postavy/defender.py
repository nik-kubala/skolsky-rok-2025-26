from .warrior import Warrior

class Defender(Warrior):
    def __init__(self, health: int = 60, attack: int = 3, defense: int = 2):
        super().__init__(health, attack)
        self.defense: int = defense
    
    def odpocitaj_damage(self, damage: int) -> int:
        real_damage = 0
        if damage > self.defense:
            real_damage = damage - self.defense
        super().odpocitaj_damage(real_damage)
        return real_damage