from algorithms.ialgorithm import IAlgorithm

class Ceasar(IAlgorithm):
    _name = "Ceasar"

    def encrypt(self, tekst, klucz):
        zaszyfrowany_tekst = ""
        klucz = int(klucz)
        for i in range(len(tekst)):
            if tekst[i].isalpha():
                if tekst[i].isupper():
                    zaszyfrowany_tekst += chr((ord(tekst[i]) + klucz - 65) % 26 + 65)
                else:
                    zaszyfrowany_tekst += chr((ord(tekst[i]) + klucz - 97) % 26 + 97)
            else:
                zaszyfrowany_tekst += tekst[i]
        return zaszyfrowany_tekst

    def decrypt(self, zaszyfrowany_tekst, klucz):
        tekst = ""
        klucz = int(klucz)
        for i in range(len(zaszyfrowany_tekst)):
            if zaszyfrowany_tekst[i].isalpha():
                if zaszyfrowany_tekst[i].isupper():
                    tekst += chr((ord(zaszyfrowany_tekst[i]) - klucz - 65) % 26 + 65)
                else:
                    tekst += chr((ord(zaszyfrowany_tekst[i]) - klucz - 97) % 26 + 97)
            else:
                tekst += zaszyfrowany_tekst[i]
        return tekst

    def get_name(self):
        return self._name

