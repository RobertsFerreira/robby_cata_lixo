import os


class HelpFile:
    def createFile(pathFile, suffix) -> None | Exception:
        try:
            dir = pathFile.removesuffix(suffix)
            if not os.path.exists(dir):
                os.makedirs(dir)            
            file = open(pathFile, 'w')
            file.close()
        except Exception as e:
            return e