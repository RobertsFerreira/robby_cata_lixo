import traceback
from modules.individual.models.individual import Individual
from modules.population.controller.population_controller import PopulationController
from modules.population.models.population import Population
from modules.world.models.world import World
from modules.world.controller.world_controller import WorldController

def main():

    #TODO: Ler o arquivo de configuração

    try:
        # world = World(size=10, withParede=True)
        worldController = WorldController()
        # world.generateWorld()
        # worldController.saveWorld(world= world)
        worldFile = worldController.getWorldFile()
        print()
        print('        World       ')
        print()
        print('-----------------------------------------')
        print()
        worldFile.printWorld()
        print()
        print('-----------------------------------------')

        # definir tamanho da polução    
        populationController = PopulationController(sizePopulationStart=50, numberOfGerations=20, world=worldFile)

        populationController.generateGerations()

        populationController.printPopulation()

    except Exception as e:
        print(e)
        print(traceback.format_exc())
    
main()