from abc import ABCMeta, abstractmethod


class SavingParams:
    def __init__(self, *, id: str, name: str):
        self.id = id
        self.name = name


class UserRepository(metaclass=ABCMeta):
    @abstractmethod
    def save(self, params: SavingParams):
        raise NotImplementedError()
