

class vigenere:
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"
    ALPHABET_CASE_SHIFT = 32

    def __init__(self, key) -> None:
        self.key = key

    def encrypt(self, text: str) -> str:
        ciphertext = ""

        keyLen = len(self.key)
        start = ord(self.ALPHABET[0])
        end = ord(self.ALPHABET[-1])

        keyIdx = 0
        for charIdx in range(len(text)):
            val = ord(text[charIdx])
            shift = 0
            if (val >= start - self.ALPHABET_CASE_SHIFT and val <= end - self.ALPHABET_CASE_SHIFT):
                shift = self.ALPHABET_CASE_SHIFT
                val += shift
            
            if (val >= start and val <= end):
                ciphertext = ciphertext + chr(start + (val - start + ord(self.key[keyIdx % keyLen]) - start) % 26 - shift)
                keyIdx += 1
            else:
                ciphertext = ciphertext + text[charIdx]

        return ciphertext

    def decrypt(self, ciphertext: str) -> str:
        text = ""
        
        keyLen = len(self.key)
        start = ord(self.ALPHABET[0])
        end = ord(self.ALPHABET[-1])

        keyIdx = 0
        for charIdx in range(len(ciphertext)):
            val = ord(ciphertext[charIdx])
            shift = 0
            if (val >= start - self.ALPHABET_CASE_SHIFT and val <= end - self.ALPHABET_CASE_SHIFT):
                shift = self.ALPHABET_CASE_SHIFT
                val += shift
            
            if (val >= start and val <= end):
                text = text + chr(start + (val - start - (ord(self.key[keyIdx % keyLen]) - start)) % 26 - shift)
                keyIdx += 1
            else:
                text = text + ciphertext[charIdx]

        return text
