import random
from typing_extensions import Self

from modules.helpers.help_file import HelpFile

class World:
    def __init__(self, size: int, withParede: bool = True, _world: list[int]=[]):
        self.withParede = withParede
        self._world = _world
        self._sizeWorld = (size + 2) if self.withParede else size
        self.helpFile = HelpFile()

    def generateWorld(self) -> None | Exception:
        try:
            self._world = [[] for _ in range(self._sizeWorld)]
            for i in range(0, self._sizeWorld):
                for j in range(0, self._sizeWorld):
                    if (i == 0 or i == self._sizeWorld - 1 or j == 0 or j == self._sizeWorld - 1) and self.withParede:
                        self._world[i].append(2)
                    else:
                        self._world[i].append(random.randint(0, 1))
        except Exception as e:
            return e
        

    def _getSize(self, total: bool = False) -> int:
        return self._sizeWorld if not total else self._sizeWorld * self._sizeWorld

    def getWorld(self) -> list[list[int]]:
        return self._world

    def toFile(self, file) -> Exception | None:
        try:
            posiInWorld = 0
            sizeTotalWorld = self._getSize(total=True)
            for i in range(self._world.__len__()):
                for j in range(self._world[i].__len__()):
                    posiInWorld += 1
                    file.write(str(self._world[i][j]) + ' ')
                    percent = self.helpFile.getPorcentSave(size=sizeTotalWorld, position=posiInWorld)
                    print(f'Progesso: {percent}%')
                file.write('\n')
        except Exception as e:
            return e

    def fromFile(linhas: list[str]) -> Exception | Self:
        try:
            _world = []
            for i in range(linhas.__len__()):
                linha = linhas[i]
                linha = linha.rstrip()
                linha = linha.split(' ')
                _linha = [int(x) for x in linha]
                _world.append(_linha)

            sizeWorldFile = _world.__len__() - 2 if _world[0][0] == 2 else _world.__len__()

            return World(size= sizeWorldFile,  _world=_world )
        except Exception as e:
            return e

    def printWorld(self) -> None:
        if self._world.__len__() == 0:
            raise Exception("Mundo está vazio, gere o mundo primeiro")
        else:
            for i in range(0, self._sizeWorld):
                for j in range(0, self._sizeWorld):
                    print(self._world[i][j], end=" ")
                print()