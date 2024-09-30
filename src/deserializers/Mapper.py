from src.models.ActivityQuestion import ActivityQuestion
from src.models.ContextQuestion import ContextQuestion
from src.models.SubjectQuestion import SubjectQuestion


class Mapper:
    """Maps keys to classes."""

    _map = {
        "Represented_activities_categorization": ActivityQuestion,
        "Subject_categorization": SubjectQuestion,
        "Context_categorization": ContextQuestion,
    }

    @staticmethod
    def get_class(key: str) -> type:
        return Mapper._map.get(key)
