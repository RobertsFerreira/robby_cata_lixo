from modules.individual.models.individual import Individual
from modules.world.models.world import World

class Population:
    def __init__(self, sizePopulation: int, world: World):
        self.sizePopulation = sizePopulation
        self.individuals: list[Individual] = []
        self.bestIndividual: Individual = None
        self.averageFitness = 0.0
        self.world = world

    def generatePopulation(self, numActionsIndividual: int = 200) -> None:
        for _ in range(self.sizePopulation):
            # a pensar: Deixar o numero de passos fixo ou receber por parametro
            individual = Individual(numActionsIndividual)
            individual.generateGenes()
            individual.calculateFitness(world=self.world)
            self.individuals.append(individual)

    def getBestIndividual(self) -> Individual:
        for _, individual in enumerate(self.individuals):
            if self.bestIndividual is None:
                self.bestIndividual = individual
            elif individual.fitness() > self.bestIndividual.fitness():
                    self.bestIndividual = individual
        
        index = self.individuals.index(self.bestIndividual)
        
        print(f'Melhor individuo: {index+1} | Fitness: {self.bestIndividual.fitness()}')

        return self.individuals[index]
        
    def getAverageFitness(self) -> float:
        for individual in self.individuals:
            self.averageFitness += individual.fitness
        self.averageFitness /= self.sizePopulation
        return self.averageFitness

    def getTotalFitenss(self) -> float:
        total = 0
        for individual in self.individuals:
            total += individual.fitness
        return total

    def getIndividuals(self) -> list[Individual]:
        return self.individuals

    def getSize(self) -> int:
        return self.sizePopulation