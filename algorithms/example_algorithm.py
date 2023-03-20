from .ialgorithm import IAlgorithm


class ExampleAlgorithm(IAlgorithm):
    _name = "Example Algorithm"

    def encrypt(self, text: str):
        return "Encrypted text"

    def decrypt(self, text: str):
        return "Decrypted text"

    def get_name(self):
        return self._name

class ExampleAlgorithm1(IAlgorithm):
    _name = "Całe te"

    def encrypt(self, text: str):
        return "Encrypted text123"

    def decrypt(self, text: str):
        return "Decrypted text123"

    def get_name(self):
        return self._name

class MegaAlgorytm(IAlgorithm):
    _name = "Mega algorytm kryptograficzny"

    def encrypt(self, text: str):
        return "Encrypted text"

    def decrypt(self, text: str):
        return "Decrypted text"

    def get_name(self):
        return self._name

