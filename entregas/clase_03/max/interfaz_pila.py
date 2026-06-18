
class Pila:
    """
    Propuesta de interfaz de pila usando POO.
    """
    def __init__(self, pila):
        self.pila = pila


        if not (isinstance(self.pila, (list, dict,))):
            raise TypeError("Tiene que ser lista o diccionario.")

    def push(self, item):
        """
        Agrega un elemento hasta arriba.
        """
        self.pila.append(item)


    def pop(self):
        """
        Elimina el elemento de hasta arriba.
        """
        if len(self.pila) == 0:
            raise ValueError("Ya está vacío.")
        
        self.pila.remove(self.pila[-1])


    def peek(self):
        """
        Muestra el elemento superior, sin realizar ediciones.
        """
        return self.pila[-1]


    def empty(self):
        """
        Revisa si está vacía.
        """
        if len == 0:
            return True
        
        return False