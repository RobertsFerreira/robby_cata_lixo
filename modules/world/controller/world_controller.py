import os
from instances_global.instances import Instance

from modules.helpers.help_file import HelpFile
from ..models.world import World

class WorldController:
    
    config = Instance.config()

    pathFileWorld = config.getPathFileWorld()
    
    def saveWorld(self, world: World) -> Exception | None:
        try:
            print('Salvando mundo...')
            if not os.path.exists(self.pathFileWorld):
                HelpFile.createFile(pathFile=self.pathFileWorld, suffix='world.txt')            
            file = open(self.pathFileWorld, 'w')
            world.toFile(file=file)
            file.close()
            print('Mundo salvo com sucesso')
        except Exception as e:
            return e
                    

    def getWorldFile(self) -> Exception | World:
        try:
            if os.path.exists(self.pathFileWorld):
                file = open(self.pathFileWorld, 'r')
                linhas = file.readlines()
                world = World.fromFile(linhas=linhas)
                file.close()
                return world
            else:
                raise Exception('Arquivo não encontrado')
        except Exception as e:
            return e