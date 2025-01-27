from abc import abstractmethod, ABC


class ModelHandler(ABC):

    @abstractmethod
    def generate(self, image, prompt):
        """Abstract method to process the request."""
        pass