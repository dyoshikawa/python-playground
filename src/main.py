import unittest
from unittest.mock import patch, MagicMock
from abc import ABCMeta, abstractmethod


class SampleUseCase(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        raise NotImplementedError()


class SampleUseCaseImpl(SampleUseCase):
    def execute(self) -> str:
        return "hello"


if __name__ == "__main__":
    unittest.main()
