from abc import ABC, abstractmethod

class BaseProduct(ABC):
    """
    базовый абстрактный класс, родительский для класса Product
    """
    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        """
        это именно класс метод
        """
        pass