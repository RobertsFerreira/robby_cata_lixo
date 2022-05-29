from modules.individual.models.individual import Individual

class Population:
    def __init__(self, size):
        self.size = size
        self.individuals: list[Individual] = []
        self.bestIndividual: Individual = None
        self.averageFitness = 0.0

    def generatePopulation(self, numActionsIndividual = 200):
        for _ in range(self.size):
            # a pensar: Deixar o numero de passos fixo ou receber por parametro
            individual = Individual(numActionsIndividual)
            individual.generateGenes()
            self.individuals.append(individual)

    def getBestIndividual(self, world):
        for _, individual in enumerate(self.individuals):
            if self.bestIndividual is None:
                self.bestIndividual = individual
            elif individual.getFitness() > self.bestIndividual.getFitness():
                    self.bestIndividual = individual
        
        index = self.individuals.index(self.bestIndividual)

        print(f'Melhor individuo: {index+1} | Fitness: {self.bestIndividual.getFitness()}')

    def getAverageFitness(self):
        return self.averageFitness

    def getIndividuals(self):
        return self.individuals

    def getSize(self):
        return self.size