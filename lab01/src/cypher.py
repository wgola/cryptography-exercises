from abc import ABC, abstractmethod


class Cypher(ABC):
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
