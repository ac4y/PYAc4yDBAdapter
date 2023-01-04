from ac4y_object.domain.pattern.ac4y_object_own_init import Ac4yObjectOwnInit

class Ac4yDBAdapterConfigParserAlgebra(Ac4yObjectOwnInit):

    CONFIG_STORAGE = "config.ini"
    CONFIG_SECTION = "db"

    USER_PROPERTY = 'user'
    PASSWORD_PROPERTY = 'password'
    HOST_PROPERTY = 'host'
    PORT_PROPERTY = 'port'
    INSTANCE_PROPERTY = 'instance'

    def get_user(self):
        return self.user

    def set_user(self, user):
        self.user = user


    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password


    def get_host(self):
        return self.host

    def set_host(self, host):
        self.host = host


    def get_port(self):
        return self.port

    def set_port(self, port):
        self.port = port


    def get_instance(self):
        return self.instance

    def set_instance(self, instance):
        self.instance = instance






