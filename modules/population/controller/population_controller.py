import random
from typing import Tuple

from global_enums.enum_actions import Actions
from modules.individual.models.individual import Individual
from modules.population.models.population import Population
from modules.world.models.world import World

class PopulationController:

    def __init__(self, sizePopulationStart: int, world: World, numberOfGerations: int = 5, mutationRate: float = 0.05):
        self.sizePopulationStart = sizePopulationStart
        self.mutationRate = mutationRate
        self.population = Population(sizePopulation=sizePopulationStart, world=world)
        self.population.generatePopulation(numActionsIndividual=7, getSaved=True)
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
            raise Exception('Não há individuos aptos para reprodução')

        self.population.individuals = pais

        filhos = []

        while(len(filhos) < self.sizePopulationStart):
            pai, mae = self.selectWithRoulette()
            # if mae.cromossomo is empty or pai.cromossomo is empty:
            #     Exception('Erro ao selecionar individuos para reprodução')
            mid = len(pai.cromossomos) // 2
            filho = pai.cromossomos[:mid] + mae.cromossomos[mid:]
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
            fitnessTotal -= individual.fitness
        
        for i, individual in enumerate(population):
            if i == skipIndice:
                continue

            # if roulette[-1] >= randomValue:
            #     return individual

            min = roulette[-1]['max'] if accumulation > 0 else 0
            accumulation += round((individual.fitness/fitnessTotal), 2)
            max = accumulation if accumulation < 1 else 1

            mapFitness = {
                'index': i,
                'min': min,
                'max': max
            }
            roulette.append(mapFitness)

        for i, individual in enumerate(roulette):
            if individual['min'] <= offset <= individual['max']:
                return population[individual['index']]

    def selectWithRoulette(self) -> None | Tuple[Individual, Individual]:
        fitnessTotal = self.population.getTotalFitenss()
        if fitnessTotal == 0:
            raise Exception('Fitness total invalido')
        pai = self.sortToCrossover(fitnessTotal)
        indexPai = self.population.getIndividuals().index(pai)
        mae = self.sortToCrossover(fitnessTotal, skipIndice=indexPai)

        return pai, mae

    def mutation(self, mutationRate: float) -> None: 
        randomMutation = random.random() 
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
    