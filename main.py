from modules.individual.models.individual import Individual
from modules.population.controller.population_controller import PopulationController
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
        populationController = PopulationController(sizePopulationStart=3, world=worldFile)

        populationController.generateGerations()

    except Exception as e:
        print(e)
    

main()