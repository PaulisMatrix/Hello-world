from abc import ABC, abstractmethod


class Operations(ABC):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__()

    @abstractmethod
    def set(self, data, *args, **kwargs):
        """sets the key"""
        pass

    @abstractmethod
    def get(self, field, *args, **kwargs):
        """gets the value corresponding to the key and field"""
        pass

    @abstractmethod
    def expire_at(self, when, *args, **kwargs):
        """expires the key(not possible to expire child keys(field value pairs)) given a unix timestamp"""
        pass
