import configparser
from .algebra.ac4y_db_adapter_config_parser_algebra import Ac4yDBAdapterConfigParserAlgebra

class Ac4yDBAdapterConfigParser(Ac4yDBAdapterConfigParserAlgebra):

    def parse_config(self):

        config = configparser.ConfigParser()
        config.read(self.CONFIG_STORAGE)

        self.set_host(config[self.CONFIG_SECTION][self.HOST_PROPERTY])
        self.set_port(config[self.CONFIG_SECTION][self.PORT_PROPERTY])
        self.set_user(config[self.CONFIG_SECTION][self.USER_PROPERTY])
        self.set_password(config[self.CONFIG_SECTION][self.PASSWORD_PROPERTY])
        self.set_instance(config[self.CONFIG_SECTION][self.INSTANCE_PROPERTY])

        return self

