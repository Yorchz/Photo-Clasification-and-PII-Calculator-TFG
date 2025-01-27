class QueryManager:

    _queries = {
        "Subject_categorization": {"title": "Subject_categorization"},
        "Represented_activities_categorization": {"title": "Represented_activities_categorization"},
        "Context_categorization": {"title": "Context_categorization"},
    }

    @staticmethod
    def get_query(key: str) -> dict:
        query = QueryManager._queries.get(key)
        if query:
            return query
        else:
            raise ValueError(f"Query not found for the given key: {key}")
