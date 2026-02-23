"""Simple cipher exercises (miscellaneous).

Implement small, educational cryptographic functions:
- caesar_encrypt(text, shift)
- caesar_decrypt(text, shift)
- vigenere_encrypt(text, key)
- vigenere_decrypt(text, key)

Note: These are for learning purposes only and are NOT secure for real use.
For advanced algorithms (AES/RSA) students should use established libraries.
"""

from typing import List


def caesar_encrypt(text: str, shift: int) -> str:
    """Return Caesar-cipher encrypted text using given integer shift."""
    raise NotImplementedError()


def caesar_decrypt(text: str, shift: int) -> str:
    """Return decrypted text for a given Caesar cipher shift."""
    raise NotImplementedError()


def vigenere_encrypt(text: str, key: str) -> str:
    """Return Vigenère-cipher encrypted text using `key`."""
    raise NotImplementedError()


def vigenere_decrypt(text: str, key: str) -> str:
    """Return decrypted text for a Vigenère cipher using `key`."""
    raise NotImplementedError()


if __name__ == "__main__":
    print("Implement simple ciphers and add tests. Avoid using these for real encryption.")