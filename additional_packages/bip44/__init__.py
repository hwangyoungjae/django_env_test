from __future__ import annotations

from functools import cached_property
from typing import Literal

from bip32utils import BIP32Key, BIP32_HARDEN
from eth_keys import keys
from eth_typing import ChecksumAddress
from mnemonic import Mnemonic


class Bip44:
    PURPOSE = 44  # BIP44
    COIN_TYPE = 60  # ETH
    CHAIN = 0  # External 고정 // 0:External, 1:Internal
    DEFAULT_ACCOUNT = 0

    def __init__(self, entropy: bytes, account: int = None):
        self.entropy = entropy
        self.account = self.DEFAULT_ACCOUNT if account is None else account

    @classmethod
    def from_words(cls,
                   words: str,
                   salt: str,
                   account: int = None,
                   language: Literal['chinese_simplified', 'chinese_traditional', 'english', 'french', 'italian', 'japanese', 'korean', 'spanish'] = 'english',
                   ) -> Bip44:
        return Bip44(Mnemonic(language=language).to_seed(words, salt), account)

    @cached_property
    def master(self) -> BIP32Key:
        return BIP32Key.fromEntropy(self.entropy)

    @cached_property
    def purpose_layer(self) -> BIP32Key:
        return self.master.ChildKey(self.PURPOSE + BIP32_HARDEN)

    @cached_property
    def coin_type_layer(self) -> BIP32Key:
        return self.purpose_layer.ChildKey(self.COIN_TYPE + BIP32_HARDEN)

    @cached_property
    def account_layer(self) -> BIP32Key:
        return self.coin_type_layer.ChildKey(self.account + BIP32_HARDEN)

    @cached_property
    def change_layer(self) -> BIP32Key:
        return self.account_layer.ChildKey(self.CHAIN)

    def get_bip32_key(self, index: int) -> BIP32Key:
        return self.change_layer.ChildKey(index)

    def get_private_key(self, index: int) -> bytes:
        return self.get_bip32_key(index).PrivateKey()

    def get_public_key(self, index: int) -> bytes:
        return self.get_bip32_key(index).PublicKey()

    def get_checksum_address(self, index: int) -> ChecksumAddress:
        return keys.PublicKey.from_compressed_bytes(self.get_public_key(index)).to_checksum_address()
