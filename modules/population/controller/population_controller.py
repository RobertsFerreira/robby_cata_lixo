import random
from typing import Tuple

from global_enums.enum_actions import Actions
from modules.individual.models.individual import Individual
from modules.population.models.population import Population
from modules.world.models.world import World

class PopulationController:

    def __init__(self, sizePopulationStart: int, world: World, numberOfGerations: int = 5, mutationRate: float = 0.1):
        self.sizePopulationStart = sizePopulationStart
        self.mutationRate = mutationRate
        self._world = world
        self.population = Population(sizePopulation=sizePopulationStart, world=world)
        self.population.generatePopulation(numActionsIndividual=200,  getSaved=True)
        self.numberOfGerations = numberOfGerations

    def generateGerations(self) -> None:
        try:
            for _ in range(self.numberOfGerations):
                self.population = self.evolution()
        except Exception as e:
            return e

    def evolution(self) -> Exception | Population:
        try:
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
                mid = len(pai.cromossomos) // 2
                filho = Individual(pai.numberPass)
                filho.cromossomos = pai.cromossomos[:mid] + mae.cromossomos[mid:]
                filho.calculateFitness(world=self._world)
                filhos.append(filho)

            self.population.individuals = filhos
            self.mutation(self.mutationRate)

            return self.population  
        except Exception as e:
            return e

    def sortToCrossover(self, fitnessTotal, skipIndice = -1) -> Exception | Individual:
        try:
            roulette = []
            accumulation = 0
            offset = random.randint(0, 100)

            population = self.population.getIndividuals()

            if skipIndice != -1:
                individual = population[skipIndice]
                fitnessTotal -= individual.fitness

            for i, individual in enumerate(population):
                if i == skipIndice:
                    continue

                min = roulette[-1]['max'] if accumulation > 0 else 0
                _percent = (individual.fitness/fitnessTotal) * 100
                percent = round(_percent, 2)
                accumulation += percent
                accumulation = round(accumulation, 2)
                max = accumulation if accumulation < 100 and i != (population.__len__() - 1) else 100

                mapFitness = {
                    'index': i,
                    'min': min,
                    'max': max
                }
                roulette.append(mapFitness)

            for i, individual in enumerate(roulette):
                if individual['min'] <= offset <= individual['max']:
                    return population[individual['index']]
        except Exception as e:
            return e


    def selectWithRoulette(self) -> Exception | Tuple[Individual, Individual]:
        try:
            fitnessTotal = self.population.getTotalFitenss()
            if fitnessTotal == 0:
                raise Exception('Fitness total invalido')
            pai = self.sortToCrossover(fitnessTotal)
            indexPai = self.population.getIndividuals().index(pai)
            mae = self.sortToCrossover(fitnessTotal, skipIndice=indexPai)
            if mae is None:
                mae = pai

            return pai, mae
        except Exception as e:
            return e

    def mutation(self, mutationRate: float) -> Exception | None: 
        try:
            _individuals = self.population.getIndividuals()
            for index, individual in enumerate(_individuals): 
                randomMutation = random.random() 
                if mutationRate > randomMutation:
                    individualCromosso = individual.cromossomos
                    posMutation = random.randint(0, individualCromosso.__len__() - 1)
                    actionMutation = Actions.getAction(random.randint(0, 6))
                    individualCromosso[posMutation] = actionMutation
                    individual.cromossomos = individualCromosso
                    individual.calculateFitness(world=self._world)
                    self.population.individuals[index] = individual
        except Exception as e:
            return e

    def printPopulation(self) -> None:
        print()
        self.population.printPopulation()
        print()
        self.population.getBestIndividual()

    def _comparable(self, individual):
        return individual.fitness