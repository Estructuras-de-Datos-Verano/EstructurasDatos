
class Pila:

    def __init__(self) -> None:
        """Inicializa la pila vacía."""
        pila = []
        self.pila = pila

    def push(self, elemento: Any) -> None:
        """Agrega un elemento a la pila."""

        self.pila.append(elemento)


    def pop(self, elemento: Any) -> Any:
        """Elimina y regresa el elemento en la cima de la pila.

        Si la pila esta vacia, se lanza una excepcion.
        """
        self.pila = self.pila[:-1]

    def peek(self) -> Any:
        """Regresa el elemento en la cima de la pila sin modificarla.

        Si la pila esta vacia, se lanza una excepcion.
        """
        return self.pila[-1]

    def empty(self) -> Bool:
        """Regresa un valor verdadero o falso según el estado de la pila

        True: Pila vacía
        
        False: Pila no vacía
        """
        if len(self.pila) == 0:
            return True
        else:
            return False