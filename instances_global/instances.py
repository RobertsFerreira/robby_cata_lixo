from modules.configuration.controller.configuration_controller import ConfigurationController

class Instance:

    @staticmethod
    def config():
        configController = ConfigurationController()
        return configController.loadConfiguration()