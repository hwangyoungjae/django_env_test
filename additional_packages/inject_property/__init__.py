from __future__ import annotations

from typing import TypeVar, Generic, Type, Any

import inject

T = TypeVar('T')


class InjectProperty(Generic[T]):

    def __init__(self, di_cls: Type[T], name: str = '') -> None:
        super().__init__()
        self.di_cls = di_cls
        self.name = name

    def _get_key(self) -> str:
        return f"{self.di_cls.__name__}_{self.name}"

    def __get__(self, instance: Any, owner: Any) -> T:
        di_instance = getattr(instance, self._get_key(), None)
        if di_instance is None:
            di_instance = inject.get_injector().get_instance(self.di_cls)
            setattr(instance, self._get_key(), di_instance)
        return di_instance

    def __set__(self, instance: Any, di_instance: T):
        setattr(instance, self._get_key(), di_instance)
