from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Any, Literal

from django.core.management import BaseCommand
from web3 import Web3

from inject_property import InjectProperty


@dataclass
class Entry:
    case: Literal['go', 'leave']
    date: date
    distance: int
    running_minute: int
    idling_minute: int
    avg_speed: int


class Command(BaseCommand):
    web3: Web3 = InjectProperty(Web3)

    def handle(self, *args: Any, **options: Any) -> str | None:
        print(self.web3)
