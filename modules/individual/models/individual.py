import random

from global_enums.enum_actions import Actions
from global_enums.enum_locais import LocalWorld
from modules.world.models.world import World

POS_INICIAL = 1

class Individual:
    def __init__(self, numberPass = 5):
        self.numberPass = numberPass
        self.fitness = 0
        self.cromossomo: list[Actions] = []
    
    def generateGenes(self):
        for _ in range(self.numberPass):
            gene = random.randint(0, 6)
            action = Actions.getAction(gene)
            self.cromossomo.append(action)
    
    def printGenes(self):
        for i in range(self.cromossomo.__len__()):
            print(self.cromossomo[i].toString())

    def getFitness(self):
        return self.fitness

    def calculateFitness(self, world: World):
        posiInWorldx = POS_INICIAL
        posiInWorldy = POS_INICIAL
        _world = world.getWorld()
        for i in range(self.cromossomo.__len__()):
            print(self.cromossomo[i].toString())
            if self.cromossomo[i] == Actions.MoveAleatorio:
                gene = random.randint(0,3)
                action = Actions.getAction(gene)
                self.cromossomo[i] = action
                print(f'{self.cromossomo[i].toString().replace("Moveu", "")}')

            if self.cromossomo[i] == Actions.MoveNorte:
                if self.isParede(posiInWorldx - 1, posiInWorldy, _world):
                    self.fitness -= 5
                else:
                    posiInWorldx -= 1
            elif self.cromossomo[i] == Actions.MoveSul:
                if self.isParede(posiInWorldx + 1, posiInWorldy, _world ):
                    self.fitness -= 5
                else:
                    posiInWorldx += 1
            elif self.cromossomo[i] == Actions.MoveLeste:
                if self.isParede(posiInWorldx, posiInWorldy + 1, _world):
                    self.fitness -= 5
                else:
                    posiInWorldy += 1
            elif self.cromossomo[i] == Actions.MoveOeste:
                if self.isParede(posiInWorldx, posiInWorldy - 1, _world ):
                    self.fitness -= 5
                else:
                    posiInWorldy -= 1                
            elif self.cromossomo[i] == Actions.FicaParado:
                self.fitness += 0
            elif self.cromossomo[i] == Actions.PegaLata:
                if _world[posiInWorldx][posiInWorldy] == LocalWorld.Lata.value:
                    self.fitness += 10
                else:
                    print(f'Mas o {LocalWorld.Vazio.toString()}')
                    self.fitness -= 1

    def isParede(self, posiInWorldx, posiInWorldy, world: list[int]):
        if world[posiInWorldx][posiInWorldy] == LocalWorld.Parede.value:
            print(f'{LocalWorld.Parede.toString()}')
            return True
        else:
            return False