from abc import ABCMeta, abstractmethod
from database import Database

# Using abc, we force that everything that inherits from Saveable
# has to have the methods we need.
class Saveable(metaclass=ABCMeta):
    def save(self):
        Database.insert(self.to_dict())

    @abstractmethod
    def to_dict(self): ...
