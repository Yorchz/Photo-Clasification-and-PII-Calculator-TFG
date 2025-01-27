from src.deserializers.Mapper import Mapper


class Factory:

    @staticmethod
    def initialize_class(key: str) -> type:
        _class = Mapper.get_class(key)
        if _class:
            return _class
        else:
            raise ValueError(f"Class not found for the given key: {key}")
