class MongoDBLoader:
    """Loader for MongoDB operations."""

    def __init__(self, client, db_name: str):
        self.client = client
        self.db_name = db_name

    def _get_collection(self, collection_name: str):
        return self.client[self.db_name][collection_name]

    def get_document(self, collection_name: str, query: dict) -> dict:
        return self._get_collection(collection_name).find_one(query)
