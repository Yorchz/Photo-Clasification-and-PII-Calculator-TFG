from src.questions.ActivityQuestion import ActivityQuestion
from src.questions.ContextQuestion import ContextQuestion
from src.questions.SubjectQuestion import SubjectQuestion


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
