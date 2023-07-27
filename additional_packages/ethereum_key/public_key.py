from __future__ import annotations

import eth_keys
import inject
from eth_typing import ChecksumAddress
from eth_utils import to_checksum_address
from web3 import Web3

from .key import Key


class PublicKey(Key):
    @inject.params(web3=Web3)
    def __init__(self, address: str | ChecksumAddress, *, web3: Web3):
        super().__init__(web3)
        self._checksum_address = to_checksum_address(address)

    @classmethod
    @inject.params(web3=Web3)
    def from_public_key_bytes(cls, public_key_bytes: bytes, *, web3: Web3) -> PublicKey:
        return cls(
            address=eth_keys.keys.PublicKey(public_key_bytes).to_checksum_address(),
            web3=web3,
        )

    @classmethod
    @inject.params(web3=Web3)
    def from_compressed_bytes(cls, compressed_bytes: bytes, *, web3: Web3) -> PublicKey:
        return cls(
            address=eth_keys.keys.PublicKey.from_compressed_bytes(compressed_bytes).to_checksum_address(),
            web3=web3,
        )

    def get_checksum_address(self) -> ChecksumAddress:
        return self._checksum_address
