import os
from ..models.world import World

class WorldController:
    
    _PATHFILE = 'modules/world/repository/world.txt'

    def _createWorldFile(self) -> None | Exception:
        try:
            dir = self._PATHFILE.removesuffix('world.txt')
            if not os.path.exists(dir):
                os.makedirs(dir)            
            file = open(self._PATHFILE, 'w')
            file.close()
        except Exception as e:
            return e

    def saveWorld(self, world: World) -> None | Exception:
        try:
            print('Salvando mundo...')
            if not os.path.exists(self._PATHFILE):
                self._createWorldFile()            
            file = open(self._PATHFILE, 'w')
            world.toFile(file=file)
            file.close()
            print('Mundo salvo com sucesso')
        except Exception as e:
            return e
                    

    def getWorldFile(self) -> World | Exception:
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