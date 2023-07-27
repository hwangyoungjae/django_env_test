from abc import ABCMeta, abstractmethod
from typing import NoReturn


class IMemberService(metaclass=ABCMeta):
    @abstractmethod
    def save(self) -> NoReturn:
        ...
