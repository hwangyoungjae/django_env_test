from __future__ import annotations

from abc import ABCMeta, abstractmethod

import inject
from eth_typing import ChecksumAddress
from web3 import Web3
from web3.types import Wei, Nonce


class Key(metaclass=ABCMeta):
    @inject.params(web3=Web3)
    def __init__(self, web3: Web3):
        self.web3 = web3

    def get_balance(self) -> Wei:
        return self.web3.eth.get_balance(self.get_checksum_address())

    def get_nonce(self) -> Nonce:
        return self.web3.eth.get_transaction_count(self.get_checksum_address())

    def get_code(self) -> bytes:
        return self.web3.eth.get_code(self.get_checksum_address())

    def is_contract(self) -> bool:
        return bool(self.get_code())

    @abstractmethod
    def get_checksum_address(self) -> ChecksumAddress:
        ...
