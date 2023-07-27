from __future__ import annotations

import binascii
from typing import cast, Optional

import eth_account
import eth_keys
import inject
from eth_account.datastructures import SignedTransaction
from eth_typing import ChecksumAddress
from hexbytes import HexBytes
from web3 import Web3
from web3.types import Wei, Nonce

from .key import Key
from .public_key import PublicKey


class PrivateKey(Key):
    @inject.params(web3=Web3)
    def __init__(self, private_key_bytes: bytes, *, web3: Web3):
        super().__init__(web3)
        self.key = private_key_bytes.hex()
        self.public_key = PublicKey(eth_keys.keys.PrivateKey(private_key_bytes).public_key.to_checksum_address())

    @classmethod
    @inject.params(web3=Web3)
    def from_key(cls, key: str, *, web3: Web3) -> PrivateKey:
        return cls(
            private_key_bytes=binascii.unhexlify(key),
            web3=web3,
        )

    def get_checksum_address(self) -> ChecksumAddress:
        return self.public_key.get_checksum_address()

    def sign_transaction(self, transaction_dict: dict) -> SignedTransaction:
        account = cast(eth_account.Account, self.web3.eth.account)
        return account.sign_transaction(
            transaction_dict=transaction_dict,
            private_key=self.key,
        )

    def transfer(self,
                 public_key: PublicKey,
                 value: Optional[Wei] = None,
                 nonce: Optional[Nonce] = None,
                 gas_price: Optional[Wei] = None,
                 gas: int = 21000,
                 ) -> HexBytes:
        if gas_price is None:
            gas_price = self.web3.eth.get_block('latest')['baseFeePerGas']
        if value is None:
            transaction_fee = gas_price * gas
            value = self.get_balance() - transaction_fee
        if nonce is None:
            nonce = self.get_nonce()
        transaction_dict = {
            'to': public_key.get_checksum_address(),
            'value': value,
            'gasPrice': gas_price,
            'gas': gas,
            'nonce': nonce,
        }
        signed_transaction = self.sign_transaction(transaction_dict)
        return self.web3.eth.send_raw_transaction(signed_transaction.rawTransaction)
