from enum import Enum

class LocalWorld(Enum):
    Vazio=0
    Lata=1 
    Parede=2

    def toString(self):
        if self == LocalWorld.Vazio:
            return "Local está Vazio"
        elif self == LocalWorld.Lata:
            return "Há uma Lata neste local"
        elif self == LocalWorld.Parede:
            return "Há uma Parede à frente"
        else:
            Exception("Valor não identificado")
    
    def getLocal(index):
        if index == 0:
            return LocalWorld.Vazio
        elif index == 1:
            return LocalWorld.Lata
        elif index == 2:
            return LocalWorld.Parede
        else:
            Exception("Valor não identificado")