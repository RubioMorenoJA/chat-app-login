from hashlib import sha256


def encrypt(string: str) -> str:
    return sha256(string.encode('utf-8')).hexdigest()
