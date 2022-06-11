import traceback
from instances_global.instances import Instance
from modules.population.controller.population_controller import PopulationController
from modules.world.models.world import World
from modules.world.controller.world_controller import WorldController
from modules.helpers.help_utils import pause

def main():
    
    try:

        config = Instance.config()

        world = World(size=config.getSizeWorld(), withParede=config.getWithParede())
        
        if config.getGenerateWorld():
            world.generateWorld()

        worldController = WorldController()
        
        if config.getSaveWorld():
            worldController.saveWorld(world=world)

        if config.getGetSavedWorld():
            world = worldController.getWorldFile()
            
        print()
        print('        World       ')
        if config.getPrintWorld():
            print()
            print('-----------------------------------------')
            print()
            world.printWorld()
        print()
        print('-----------------------------------------')
  
        populationController = PopulationController(sizePopulationStart=config.getSizePopulation(), numberOfGerations=config.getNumberOfGerations(), world=world)

        populationController.generateGerations()

        populationController.printPopulation()

    except Exception as e:
        print(e)
        print(traceback.format_exc())
    
    pause()

main()