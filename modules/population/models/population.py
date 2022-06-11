import json
import os
from instances_global.instances import Instance

from modules.helpers.help_file import HelpFile
from modules.helpers.help_utils import comparable
from modules.individual.models.individual import Individual
from modules.world.models.world import World

class Population:

    #TODO: Adicionar Try/Except nas funcoes e adicionar os tipos de retornos corretos

    def __init__(self, sizePopulation: int, world: World):
        self.sizePopulation = sizePopulation
        self.individuals: list[Individual] = []
        self.bestIndividual: Individual = None
        self.averageFitness = 0.0
        self.world = world
        self.helpFile = HelpFile()
        self.config = Instance.config()

    def generatePopulation(self, numActionsIndividual: int = 200,  getSaved = False, saveGeneration = False) -> None:
        try:
            if getSaved:
                self._getFile(world=self.world)
            else:
                for _ in range(self.sizePopulation):
                    # a pensar: Deixar o numero de passos fixo ou receber por parametro
                    individual = Individual(numActionsIndividual, cromossomos=[])
                    individual.generateGenes()
                    individual.calculateFitness(world=self.world)
                    self.individuals.append(individual)
                if saveGeneration: self._saveFile()
        except Exception as e:
            raise e

    def getBestIndividual(self) -> Individual:
        try:
            for index, individual in enumerate(self.individuals):
                if self.bestIndividual is None:
                    self.bestIndividual = individual
                    _index = index + 1
                elif individual.fitness > self.bestIndividual.fitness:
                    self.bestIndividual = individual
                    _index = index + 1
                
            print(f'Melhor individuo: {_index} | Fitness: {self.bestIndividual.fitness}')
            print(f'Numero de Ações: {self.bestIndividual.numberPass}')
            # print(f'       Ações         ')
            # self.bestIndividual.printGenes()
            print()
        except Exception as e:
            raise e
        
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

    def printPopulation(self):
        self.individuals.sort(reverse=True, key=comparable)
        for index, individual in enumerate(self.individuals):
            print(f'Individuo: {index+1}')
            print(f'Fitnes: {individual.fitness}')
            print(f'Numero de Ações: {individual.numberPass}')
            print()
            print('-----------------------------------------')
            print()

    def _saveFile(self):
        try:
            print('Salvando individuo...')
            if os.path.exists(self.config.getPathFileIndividual()):
                os.remove(self.config.getPathFileIndividual())
            else:
                self.helpFile.createFile(pathFile=self.config.getPathFileIndividual(), suffix='individual.txt')            
            file = open(self.config.getPathFileIndividual(), 'w')
            posIndividual = 0
            for individual in self.individuals:
                posIndividual += 1
                individualFile = individual.toMap()
                file.write(json.dumps(individualFile, indent=4))
                percent = self.helpFile.getPorcentSave(size=self.sizePopulation, position=posIndividual)
                print(f'Progesso: {percent}%')
            file.close()
            print('Individuo salvo com sucesso')
        except Exception as e:
            return e

    def _getFile(self, world):
        try:
            if os.path.exists(self.config.getPathFileIndividual()):
                file = open(self.config.getPathFileIndividual(), 'r')
                linhas = file.readlines()
                file.close()
                _individuals = []
                for linha in linhas:
                    _linha = eval(linha)
                    individual = Individual.fromMap(individualMap=_linha)
                    _individuals.append(individual)
                    
                self.sizePopulation=_individuals.__len__(),
                self.world=world,
                self.individuals=_individuals                
                    
            else:
                raise Exception('Arquivo não encontrado')
        except Exception as e:
            return e