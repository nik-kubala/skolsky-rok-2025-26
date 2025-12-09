class Warrior:
    def __init__(self, health: int = 50, attack: int = 5, is_alive: bool = True) -> None:
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