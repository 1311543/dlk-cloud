from abc import ABC, abstractmethod


class Service(ABC):
    @abstractmethod
    def getService(self) -> None:
        """Add method to be implemented."""
        pass
