from abc import abstractmethod, ABC


class ModelHandler(ABC):
    """Abstract base class for handling models."""

    @abstractmethod
    def generate(self, image, prompt):
        """Abstract method to process the request."""
        pass