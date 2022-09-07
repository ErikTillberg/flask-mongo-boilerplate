server_name = 'localhost'
server_port = '5050'


class BaseConfig:
    """Base Config Class"""

    SERVER_NAME = server_name + ':' + server_port
    MONGODB_HOST = 'localhost:27017'

