import unittest
import vigenere as v
import rsa as r

class vigenereTest(unittest.TestCase):

    def test_1(self):
        cipher = v.vigenere("cryptii")
        text = "The quick brown fox jumps over 13 lazy dogs."
        print("Text: ", text)

        ciphertext = cipher.encrypt(text)
        print("Encrypted text: ", ciphertext)
        self.assertEqual(ciphertext, "Vyc fnqkm spdpv nqo hjfxa qmcg 13 eiha umvl.")

        decryptedText = cipher.decrypt(ciphertext)
        print("Decrypted text: ", decryptedText)
        self.assertEqual(decryptedText, text)

        print("")

class rsaTest(unittest.TestCase):

    def test_1(self):
        # n, e, d = r.rsa.make_key_pair(8)
        n=2534665157
        e=7
        d=1810402843

        # cipher = r.rsa()
        text = 123
        print("Text: ", text)

        ciphertext = r.rsa.encrypt(text, e, n)
        print("Encrypted text: ", ciphertext)
        self.assertEqual(ciphertext, 2463995467)

        decryptedText = r.rsa.decrypt(ciphertext, d, n)
        print("Decrypted text: ", decryptedText)
        self.assertEqual(decryptedText, text)

        print("")

if __name__ == '__main__':
    unittest.main()
