from algorithms.ialgorithm import IAlgorithm

class Vigenere(IAlgorithm):
    _name = "Vigenere"

    def encrypt(self, tekst, klucz):
        zaszyfrowany_tekst = ""
        klucz = str(klucz)
        klucz_dostosowany = klucz * (len(tekst) // len(klucz)) + klucz[:len(tekst) % len(klucz)]
        for i in range(len(tekst)):
            if tekst[i].isalpha():
                if tekst[i].isupper():
                    zaszyfrowany_tekst += chr((ord(tekst[i]) + ord(klucz_dostosowany[i]) - 2 * 65) % 26 + 65)
                else:
                    zaszyfrowany_tekst += chr((ord(tekst[i]) + ord(klucz_dostosowany[i]) - 2 * 97) % 26 + 97)
            else:
                zaszyfrowany_tekst += tekst[i]
        return zaszyfrowany_tekst


    def decrypt(self, zaszyfrowany_tekst, klucz):
        tekst = ""
        klucz = str(klucz)
        klucz_dostosowany = klucz * (len(zaszyfrowany_tekst) // len(klucz)) + klucz[:len(zaszyfrowany_tekst) % len(klucz)]
        for i in range(len(zaszyfrowany_tekst)):
            if zaszyfrowany_tekst[i].isalpha():
                if zaszyfrowany_tekst[i].isupper():
                    tekst += chr((ord(zaszyfrowany_tekst[i]) - ord(klucz_dostosowany[i]) + 26) % 26 + 65)
                else:
                    tekst += chr((ord(zaszyfrowany_tekst[i]) - ord(klucz_dostosowany[i]) + 26) % 26 + 97)
            else:
                tekst += zaszyfrowany_tekst[i]
        return tekst
    def get_name(self):
        return self._name

