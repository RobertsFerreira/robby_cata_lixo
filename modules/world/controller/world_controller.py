import os

from modules.helpers.help_file import HelpFile
from ..models.world import World

class WorldController:
    
    _PATHFILE = 'modules/world/repository/world.txt'

    def saveWorld(self, world: World) -> Exception | None:
        try:
            print('Salvando mundo...')
            if not os.path.exists(self._PATHFILE):
                HelpFile.createFile(pathFile=self._PATHFILE, suffix='world.txt')            
            file = open(self._PATHFILE, 'w')
            world.toFile(file=file)
            file.close()
            print('Mundo salvo com sucesso')
        except Exception as e:
            return e
                    

    def getWorldFile(self) -> Exception | World:
        try:
            if os.path.exists(self._PATHFILE):
                file = open(self._PATHFILE, 'r')
                linhas = file.readlines()
                world = World.fromFile(linhas=linhas)
                file.close()
                return world
            else:
                raise Exception('Arquivo não encontrado')
        except Exception as e:
            return e