from ulid import ULID


def gen_ulid() -> str:
    return str(ULID())
