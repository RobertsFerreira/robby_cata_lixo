import random
from global_enums.enum_actions import Actions
from modules.individual.models.individual import Individual
from modules.population.models.population import Population
from modules.world.models.world import World

class PopulationController:

    def __init__(self, sizePopulationStart: int, world: World, numberOfGerations: int = 5, mutationRate: float = 0.05):
        self.sizePopulationStart = sizePopulationStart
        self.mutationRate = mutationRate
        self.population = Population(sizePopulation=sizePopulationStart, world=world)
        self.population.generatePopulation(numActionsIndividual=3)
        self.numberOfGerations = numberOfGerations

    def generateGerations(self) -> None:
        for _ in range(self.numberOfGerations):
            self.population = self.evolution()

    def evolution(self) -> Population:
        pais = []

        for individual in self.population.getIndividuals():
            if individual.fitness >= 0:
                pais.append(individual)
        pais.sort(reverse=True, key=self._comparable)

        if pais.__len__() == 0:
            Exception('Não há individuos aptos para reprodução')

        self.population.individuals = pais

        filhos = []

        while(len(filhos) < self.sizePopulationStart):
            pai, mae = self.selectWithRoulette()
            mid = len(pai.cromossomo) // 2
            filho = pai.cromossomo[:mid] + mae.cromossomo[mid:]
            filhos.append(filho)

        self.population.individuals = filhos
        self.mutation(self.mutationRate)

        return self.population        

    def sortToCrossover(self, fitnessTotal, skipIndice = -1) -> Individual:
        roulette = []
        accumulation = 0
        offset = random.random()

        population = self.population.getIndividuals()

        if skipIndice != -1:
            individual = population[skipIndice]
            individual.calculateFitness()
            fitnessTotal -= individual.fitness
        
        for i, individual in enumerate(population):
            if i == skipIndice:
                continue
            accumulation = individual.fitnessmaps 
            #  [
    # {
    #         'index': 1,
    #         'value': 'a'
    #     },
        
    # ]
    #        #alterar mapa
            # roulette.append(maps)
            roulette.append([i, accumulation / fitnessTotal])

            # if roulette[-1] >= randomValue:
            #     return individual

        limitInferior = 0 if offset - 0.1 < 0 else offset - 0.1
        limitSuperior = 1 if offset + 0.1 > 1 else offset + 0.1

        for i, value in enumerate(roulette):
            if limitInferior >= value and value <= limitSuperior:
                index = roulette[i][0]
                return population[index]

    def selectWithRoulette(self):
        fitnessTotal = self.population.getTotalFitenss()
        pai = self.sortToCrossover(fitnessTotal)
        mae = self.sortToCrossover(fitnessTotal, skipIndice=pai)

        return pai, mae

    def mutation(self, mutationRate: float) -> None: 
        randomMutation = random() 
        for individual in self.population.getIndividuals():
            if mutationRate > randomMutation:
                individualCromosso = individual.cromossomo
                posMutation = random.randint(0, individualCromosso.__len__() - 1)
                actionMutation = Actions.getAction(random.randint(0, 6))
                individualCromosso[posMutation] = actionMutation
                individual.cromossomo = individualCromosso
                self.population.individuals = individual

    def _comparable(self, individual):
        return individual.fitness