import random

__all__ = ['encrypt', 'decrypt']

def encrypt(text: str) -> str:
    return '|'.join(
        f"{hex(ord(c) * (k := random.randint(2, 10)))[2:]}:{k}"
        for c in text
    )

def decrypt(cipher: str) -> str:
    try:
        return ''.join(
            chr(int(code, 16) // int(k))
            for code, k in (block.split(':') for block in cipher.split('|'))
        )
    except Exception:
        raise ValueError("Невозможно расшифровать")