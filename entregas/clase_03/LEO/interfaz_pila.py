from abc import ABC, abstractmethod

class Pila(ABC):
    @abstractmethod
    def __innit__(self):
        pass

    @abstractmethod
    def push(self):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def peek(self):
        pass

    @abstractmethod
    def empty(self):
        pass