import random

from global_enums.enum_actions import Actions
from global_enums.enum_locais import LocalWorld
from modules.world.models.world import World

POS_INICIAL = 1

class Individual:
    def __init__(self, numberPass = 5, fitness: int = 0, cromossomos: list[Actions] = []):
        self.numberPass = numberPass
        self.fitness = fitness
        self.cromossomos: list[Actions] = cromossomos
    
    def generateGenes(self) -> None:
        for _ in range(self.numberPass):
            gene = random.randint(0, 6)
            action = Actions.getAction(gene)
            self.cromossomos.append(action)
    
    def printGenes(self) -> None:
        for i in range(self.cromossomos.__len__()):
            print(self.cromossomos[i].toString())

    def toMap(self):
        individualMap = {
                            'cromossomos': [cromossomo.value for cromossomo in self.cromossomos], 
                            'fitness': self.fitness, 
                            'numberPass': self.numberPass,
                        }
        return individualMap

    def fromMap(individualMap):
        return Individual(numberPass=individualMap['numberPass'], 
        fitness=individualMap['fitness'],
        cromossomos=[Actions.getAction(gene) for gene in individualMap['cromossomos']],
        )

    def calculateFitness(self, world: World) -> None:
        posiInWorldx = POS_INICIAL
        posiInWorldy = POS_INICIAL
        _world = world.getWorld()
        for i in range(self.cromossomos.__len__()):
            print(self.cromossomos[i].toString())
            if self.cromossomos[i] == Actions.MoveAleatorio:
                gene = random.randint(0,3)
                action = Actions.getAction(gene)
                self.cromossomos[i] = action
                print(f'{self.cromossomos[i].toString().replace("Moveu", "")}')

            if self.cromossomos[i] == Actions.MoveNorte:
                if self.isParede(posiInWorldx - 1, posiInWorldy, _world):
                    self.fitness -= 5
                else:
                    posiInWorldx -= 1
            elif self.cromossomos[i] == Actions.MoveSul:
                if self.isParede(posiInWorldx + 1, posiInWorldy, _world ):
                    self.fitness -= 5
                else:
                    posiInWorldx += 1
            elif self.cromossomos[i] == Actions.MoveLeste:
                if self.isParede(posiInWorldx, posiInWorldy + 1, _world):
                    self.fitness -= 5
                else:
                    posiInWorldy += 1
            elif self.cromossomos[i] == Actions.MoveOeste:
                if self.isParede(posiInWorldx, posiInWorldy - 1, _world ):
                    self.fitness -= 5
                else:
                    posiInWorldy -= 1                
            elif self.cromossomos[i] == Actions.FicaParado:
                self.fitness += 0
            elif self.cromossomos[i] == Actions.PegaLata:
                if _world[posiInWorldx][posiInWorldy] == LocalWorld.Lata.value:
                    self.fitness += 10
                else:
                    print(f'Mas o {LocalWorld.Vazio.toString()}')
                    self.fitness -= 1

    def isParede(self, posiInWorldx, posiInWorldy, world: list[int]) -> bool:
        if world[posiInWorldx][posiInWorldy] == LocalWorld.Parede.value:
            print(f'{LocalWorld.Parede.toString()}')
            return True
        else:
            return False