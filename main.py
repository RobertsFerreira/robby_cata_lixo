from global_enums.enum_locais import LocalWorld, LocalWorldExt
from modules.individual.models.individual import Individual
from modules.population.models.population import Population
from modules.world.models.world import World
from modules.world.controller.world_controller import WorldController

def main():

    try:
        # world = World(size=10, withParede=True)
        worldController = WorldController()
        # world.generateWorld()
        # worldController.saveWorld(world= world)
        worldFile = worldController.getWorldFile()
        worldFile.printWorld()

        # definir tamanho da polução    
        population = Population(size=3)

        population.generatePopulation()

        population.getBestIndividual(worldFile)

    except Exception as e:
        print(e)
    

main()