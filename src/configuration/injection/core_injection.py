import boto3
from django.conf import settings
from inject import Binder
from mypy_boto3_s3 import S3Client
from web3 import Web3

from bip44 import Bip44


def core_injection(binder: Binder):
    binder.bind_to_constructor(Web3, lambda: Web3(Web3.HTTPProvider(settings.WEB3_HTTPS_ENDPOINT)))

    binder.bind_to_constructor(Bip44, lambda: Bip44.from_words(settings.MNEMONIC_WORDS, settings.MNEMONIC_SALT))

    binder.bind_to_constructor(S3Client, lambda: boto3.client(
        service_name='s3',
        aws_access_key_id=settings.S3['ACCESS_KEY_ID'],
        aws_secret_access_key=settings.S3['SECRET_ACCESS_KEY'],
    ))
