class Komplex:
    def __init__(self, real, img):        #imaginarna zložka
        self.real = real
        self.img = img
    
    def abs(self):      #abs je absolutna hodnota
        return (self.real ** 2 + self.img ** 2) ** 0.5
    
    def __add__(self, other):
        return Komplex(self.real + other.real, self.img + other.img)
    
    def __str__(self):
        if self.img >= 0:
            return f"{self.real}+{self.img}i"
        else:
            return f"{self.real} {self.img}i"
    
    def __mul__(self, other):
        # (a+bi) * (c+di) = (ac - bd) + (ad + bc)i
        novy_real = self.real * other.real - self.img * other.img
        novy_img = self.real * other.img + self.img * other.real
        return Komplex(novy_real, novy_img)
    
    def __truediv__(self, other):
        # (a+bi) / (c+di) = ((ac + bd) + (bc - ad)i) / (c^2 + d^2)
        menovatel = other.real ** 2 + other.img ** 2
        novy_real = (self.real * other.real + self.img * other.img) / menovatel
        novy_img = (self.img * other.real - self.real * other.img) / menovatel
        return Komplex(novy_real, novy_img)


k1 = Komplex(3, 5)
k2 = Komplex(2, 1)
k3 = k1 * k2
print(type(k3))