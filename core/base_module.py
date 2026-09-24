from abc import ABC, abstractmethod

class BaseModule(ABC):
    @abstractmethod
    def run(self ,target):
        pass
