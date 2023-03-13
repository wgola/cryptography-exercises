from abc import ABC, abstractmethod
import os


class Cypher(ABC):
    PATH = os.path.realpath(os.getcwd())

    @abstractmethod
    def encrypt():
        pass

    @abstractmethod
    def decrypt():
        pass

    @abstractmethod
    def cryptoanalysis_plain():
        pass

    @abstractmethod
    def cryptoanalysis_encrypted():
        pass

    @abstractmethod
    def check_key():
        pass

    def get_file(self, filename, option):
        return open(os.path.join(self.PATH, filename), option)

    def if_small_letter(self, ascii_number):
        return 97 <= ascii_number <= 122

    def if_big_letter(self, ascii_number):
        return 65 <= ascii_number <= 90
