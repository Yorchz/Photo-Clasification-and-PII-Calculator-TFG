class QueryManager:
    """Manages queries for data retrieval."""

    _queries = {
        "Subject": {"title": "Subject_categorization"},
        "Activity": {"title": "Represented_activities_categorization"},
        "Context": {"title": "Context_categorization"},
    }

    @staticmethod
    def get_query(key: str) -> dict:
        query = QueryManager._queries.get(key)
        if query:
            return query
        else:
            raise ValueError(f"Query not found for the given key: {key}")
