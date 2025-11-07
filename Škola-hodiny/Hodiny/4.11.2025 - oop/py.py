class Dog:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def sound(self):
        print(f"Štek pes {self.__name}")
    
    #setter
    def setName(self, name):
        self.__name = name
    
    #getter
    def getName(self):
        return self.__name

pes1 = Dog("Azor", 10)      # tu sa zavolá konštruktor, ked sa objekt vytvorí, aj v pes2
pes2 = Dog("Max", 2)        #inštancie triedy dog

pes1.sound()
pes2.sound()

print(pes1.getName())
pes1.setName("Jebo")  #malo by to byť zapuzdrené (nedať sa meniť) ale dá sa
print(pes1.getName())