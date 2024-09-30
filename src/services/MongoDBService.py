from src.data_access.mongodb.MongoDBConnection import MongoDBConnection
from src.data_access.mongodb.MongoDBLoader import MongoDBLoader
from src.data_access.mongodb.MongoDBUploader import MongoDBUploader


class MongoDBService:
    """Service to manage MongoDB operations."""

    def __init__(self, config):
        self.connection = MongoDBConnection(config['host'], config['port'])
        self.client = self.connection.connect()
        self.loader = MongoDBLoader(self.client, config['db_name'])
        self.uploader = MongoDBUploader(self.client, config['db_name'])

    def close(self):
        self.connection.close()

    def get_loader(self):
        return self.loader

    def get_uploader(self):
        return self.uploader
