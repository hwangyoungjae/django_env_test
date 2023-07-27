from __future__ import annotations

from typing import Any

from django.core.management import BaseCommand
from web3 import Web3

from inject_property import InjectProperty


class Command(BaseCommand):
    web3: Web3 = InjectProperty(Web3)

    def handle(self, *args: Any, **options: Any) -> str | None:
        print(self.web3)
