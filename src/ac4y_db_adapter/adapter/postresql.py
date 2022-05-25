import configparser
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

class PostgresqlPersistence(object):

    CONFIG_STORAGE = "config.ini"
    CONFIG_SECTION = "postgres"

    URL = "url"
    ECHO = "echo"

    def __init__(self):

        self.engine = self.get_set_engine_by_section(self.CONFIG_SECTION)
        self.session = self.get_set_session()

    def get_set_engine_by_section(self, section):

        config = configparser.ConfigParser()
        config.read(self.CONFIG_STORAGE)

        echo = False

        try:
            echo = config[section][self.ECHO] == 'True'
        except:
            echo = False

        self.engine = create_engine(
            config[section][self.URL]
            , echo=echo
            , future=True)

        return self.engine

    def get_set_engine(self):
        return self.get_set_engine_by_section(self.CONFIG_SECTION)

    def get_engine(self):
        return self.engine

    def get_set_session(self):

        self.session = Session(self.get_engine())
        return self.session

    def get_session(self):
        return self.session