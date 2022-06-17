
import random


class rsa:

    def __init__(self) -> None:
        pass

    def encrypt(message: int, e: int, n: int) -> int:
        # check if input is valid
        
        return pow(message, e, n)

    def decrypt(ciphertext: int, d: int, n: int) -> int:

        return pow(ciphertext, d, n)
