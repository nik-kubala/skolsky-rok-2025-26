class Vehicle:
    def __init__(self, name, max_speed, milage):
        self.name = name
        self.max_speed = max_speed
        self.milage = milage
    
    def __str__(self):
        return (f"{self.name} {self.max_speed} {self.milage}")
    
    
class Bus(Vehicle):
    def __init__(self, name, max_speed, milage, capacity = 50):
        super().__init__(name, max_speed, milage)
        self.capacity = capacity
    
    
Bmw = Vehicle("BMW", 250, 15000)
Škodovečka = Vehicle("Škoda", 180, 100)
Basobus = Bus("Jožo", 100, 250000)
Jebobus = Bus("Manko", 500, 10000)


