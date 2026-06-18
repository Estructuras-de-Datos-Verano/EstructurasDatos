from abc import ABC, abstractmethod
from typing import Any
class Pila(ABC):
    @abstractmethod
    def push(self, elemento: Any) -> None:
        """Agrega un elemento a la pila."""
        pass
    @abstractmethod
    def pop(self) -> Any:
        """Elimina y regresa el elemento en la cima de la pila.

        Si la pila esta vacia, se lanza una excepcion.
        """
        pass

    @abstractmethod
    def peek(self) -> Any:
        """Regresa el elemento en la cima de la pila sin modificarla.

        Si la pila esta vacia, se lanza una excepcion.
        """
        pass
    @abstractmethod
    def empty(self) -> Bool:
        """Regresa un valor verdadero o falso según el estado de la pila

        True: Pila vacía
        
        False: Pila no vacía
        """
        pass