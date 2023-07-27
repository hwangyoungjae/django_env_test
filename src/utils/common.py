def s2b(s: str) -> bytes:
    if isinstance(s, bytes):
        return s
    else:
        return str(s).encode()


def b2s(b: bytes) -> str:
    if isinstance(b, str):
        return b
    elif isinstance(b, bytes):
        return b.decode()
    else:
        return str(b)
