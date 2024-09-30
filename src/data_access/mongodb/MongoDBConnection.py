import pymongo


class MongoDBConnection:
    """Manages MongoDB connections using host and port."""

    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.client = None

    def connect(self):
        if not self.client:
            self.client = pymongo.MongoClient(host=self.host, port=self.port)
        return self.client

    def close(self):
        if self.client:
            self.client.close()
            self.client = None
