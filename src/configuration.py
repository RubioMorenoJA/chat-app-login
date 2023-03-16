import traceback
from yaml import load, Loader
from os import path


CONFIGURATION_FILE = path.abspath('configuration_local.yaml')
# CONFIGURATION_FILE = path.abspath('configuration.yaml')


class Configuration:
    database: dict

    def __init__(self) -> None:
        config = self.__get_configuration()
        if config is None:
            raise RuntimeError("Configuration File could not be read.")
        self.database = config['database']

    def get_database(self) -> dict:
        return self.database

    def __get_configuration(self) -> dict | None:
        configuration: dict | None = None
        try:
            with open(CONFIGURATION_FILE, 'r') as conf_file:
                configuration = load(conf_file, Loader=Loader)
        except IOError as exc:
            print(
                f'IOError: {exc.args}\nTraceback: {traceback.format_exc}\nConfiguration file path: {CONFIGURATION_FILE}'
            )
        return configuration


configuration: Configuration = Configuration()
