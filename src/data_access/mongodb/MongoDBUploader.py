class MongoDBUploader:
    """Uploader for MongoDB data."""

    def __init__(self, client, db_name: str):
        self.client = client
        self.db_name = db_name

    def upload_data(self, data: dict):
        collection_name = 'categorization_questions'
        query = {"title": data["title"]}
        collection = self.client[self.db_name][collection_name]
        collection.replace_one(query, data, upsert=True)
