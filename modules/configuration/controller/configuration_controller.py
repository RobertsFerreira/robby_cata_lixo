import json
import os

from modules.configuration.model.configuration import Configuration
from modules.helpers.help_file import HelpFile


class ConfigurationController:

    path = 'assets\config.json'
    helpFile = HelpFile()

    def exists(self):
        if os.path.exists(self.path):
            return True
        else:
            return False
        
    def loadConfiguration(self) -> Configuration:

        if not self.exists():
            self.helpFile.createFile(pathFile=self.path, suffix='config.json')            
            file = open(self.path, 'w')
            configDefault = Configuration.getDefaultConfiguration()
            file.write(json.dumps(configDefault.toJson(), indent=4))
            file.close()
            

        with open(self.path) as jsonFile:
            jsonData = json.load(jsonFile)

        config = Configuration.fromJson(jsonData)

        return config