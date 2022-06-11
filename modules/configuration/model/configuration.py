from typing_extensions import Self

class Configuration:
    def __init__(self, sizePopulation: int, numberOfGerations: int, mutationRate: float, numActionsIndividual: int, saveGeneration: bool, getSaved: bool, pathFileIndividual: str, sizeWorld: int, pathFileWorld: str, withParede: bool, saveWorld: bool, getSavedWorld: bool, generateWorld: bool, printWorld: bool, negativeFitness: bool):
        self.sizePopulation = sizePopulation
        self.numberOfGerations = numberOfGerations
        self.mutationRate = mutationRate
        self.numActionsIndividual = numActionsIndividual
        self.saveGeneration = saveGeneration
        self.getSaved = getSaved
        self.pathFileIndividual = pathFileIndividual
        self.sizeWorld = sizeWorld
        self.pathFileWorld = pathFileWorld
        self.withParede = withParede
        self.saveWorld = saveWorld
        self.getSavedWorld = getSavedWorld
        self.generateWorld = generateWorld
        self.printWorld = printWorld
        self.negativeFitness = negativeFitness
                
    def getSizePopulation(self) -> int:
        return self.sizePopulation

    def getNumberOfGerations(self) -> int:
        return self.numberOfGerations
    
    def getMutationRate(self) -> float:
        return self.mutationRate
        
    def getNumActionsIndividual(self) -> int:
        return self.numActionsIndividual

    def getSaveGeneration(self) -> bool:
        return self.saveGeneration
    
    def getGetSaved(self) -> bool:
        return self.getSaved
    
    def getPathFileIndividual(self) -> str:
        return self.pathFileIndividual
    
    def getSizeWorld(self) -> int:
        return self.sizeWorld

    def getPathFileWorld(self) -> str:
        return self.pathFileWorld
    
    def getWithParede(self) -> bool:
        return self.withParede
    
    def getSaveWorld(self) -> bool:
        return self.saveWorld

    def getGetSavedWorld(self) -> bool:
        return self.getSavedWorld

    def getGenerateWorld(self) -> bool:
        return self.generateWorld

    def getPrintWorld(self) -> bool:
        return self.printWorld

    def getNegativeFitness(self) -> bool:
        return self.negativeFitness
    
    @staticmethod
    def getDefaultConfiguration() -> Self:
        return Configuration(
            sizePopulation=20,
            numberOfGerations=20,
            mutationRate=0.13,
            numActionsIndividual=200,
            saveGeneration=False,
            getSaved=False,
            pathFileIndividual="modules/individual/repository/individual.txt",
            sizeWorld=10,
            pathFileWorld="modules/world/repository/world.txt",
            withParede=True,
            saveWorld=False,
            getSavedWorld=False,
            generateWorld=True,
            printWorld=False,
            negativeFitness=False
        )


    @staticmethod
    def fromJson(json) -> Self:
       return Configuration(
            sizePopulation=json['sizePopulation'],
            numberOfGerations=json['numberOfGerations'],
            mutationRate=json['mutationRate'],
            numActionsIndividual=json['numActionsIndividual'],
            saveGeneration=json['saveGeneration'],
            getSaved=json['getSaved'],
            pathFileIndividual=json['pathFileIndividual'],
            sizeWorld=json['sizeWorld'],
            pathFileWorld=json['pathFileWorld'],
            withParede=json['withParede'],
            saveWorld=json['saveWorld'],
            getSavedWorld=json['getSavedWorld'],
            generateWorld=json['generateWorld'],
            printWorld=json['printWorld'],
            negativeFitness=json['negativeFitness']
       )

    def toJson(self) -> dict:
        return {
            'sizePopulation': self.sizePopulation,
            'numberOfGerations': self.numberOfGerations,
            'mutationRate': self.mutationRate,
            'numActionsIndividual': self.numActionsIndividual,
            'saveGeneration': self.saveGeneration,
            'getSaved': self.getSaved,
            'pathFileIndividual': self.pathFileIndividual,
            'sizeWorld': self.sizeWorld,
            'pathFileWorld': self.pathFileWorld,
            'withParede': self.withParede,
            'saveWorld': self.saveWorld,
            'getSavedWorld': self.getSavedWorld,
            'generateWorld': self.generateWorld,
            'printWorld': self.printWorld,
            'negativeFitness': self.negativeFitness
        }
