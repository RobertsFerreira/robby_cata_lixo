import os


class HelpFile:
    def createFile(self, pathFile: str, suffix: str) -> None | Exception:
        try:
            dir = pathFile.removesuffix(suffix)
            if not os.path.exists(dir):
                os.makedirs(dir)            
            file = open(pathFile, 'w')
            file.close()
        except Exception as e:
            return e

    def getPorcentSave(self, size: int, position: int) -> float:
        porcent = (position / size) * 100
        return round(porcent, 2)