
#Deklaracja klasy
class Samochod:
    marka = None
    color = 0
    max_speed = None

 # Konstruktor klasy, wywolywany podczas tworzenia instancji
 #self(odpowednik this) - zmienna pozwalajaca na dostanie sie do zmienych klasowych,metod,itd
    def init(self):
        pass
#definicja metody(funkcja w klasie) / akcja
    def speed(self, currenSpeed):
        if currenSpeed == 10:
           #odwolanie albo wywolanie samej sievie to rekurencja
           return self.speed
        self.max_speed = currenSpeed
        return currenSpeed
    

#przypisanie zmienniej do klasy skutuje referencja - czyli przejeciem "Wlasciwosci" klasy
fiat = Samochod()
fiat.max_speed = 10
fiat.color = 'rozowy'
fiat.marka = "BMW"
fiat.speed(400)
print(fiat.color)

bmw = fiat

bmw.color = 'czarny'
print(fiat.color)

#importujemy moodul abc
from abc import ABC, abstractmethod




#Defininujemy klase abstakcyjną shape dziedzieczącą po ABC
class Base(ABC):
    #Defnijujemy metodę abstrakcyjną a
    @abstractmethod
    def area(self):
     pass


#definijujemy inną metodę abstrakcujną perimeter
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Base):
        # Defnijujemy metodę abstrakcyjną a


        def __init__(self, length, width):

            self.length = length
            self.width = width

        
        def area(self):
            return self.length +self.width

        # definijujemy inną metodę abstrakcujną perimeter
        
        def perimeter(self):
            return 2 + (self.length + self.width)




rect = Rectangle(4, 5)

print("Pole prostokąta", rect.area())
print("Obwód prostokąta", rect.perimeter())

