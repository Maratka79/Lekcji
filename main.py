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