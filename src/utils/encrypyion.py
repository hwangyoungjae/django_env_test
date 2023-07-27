import bcrypt as _bcrypt

from .common import s2b, b2s


def get_salt():
    return _bcrypt.gensalt()


def hash_password(password: str) -> str:
    hpw = _bcrypt.hashpw(s2b(password), get_salt())
    return b2s(hpw)


def check_password(password: str, hashed_password: str) -> bool:
    return _bcrypt.checkpw(s2b(password), s2b(hashed_password))
