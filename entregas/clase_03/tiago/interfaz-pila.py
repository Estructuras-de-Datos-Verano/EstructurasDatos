class pilaTDA:
    """
    Propuesta de interfaz de pila usando POO.
    """
    def __init__(self):
        self.pila = []
            
    def push(self,objeto):
        """
        Agrega un elemento hasta arriba de la pila.
        """
        self.pila.append(objeto)
        
    def pop(self):
        """
        Remueve el tope.
        """
        if len(self.pila) == 0:
            return None

        else:
            tope = self.pila[-1]
            self.pila.remove(tope)

        return tope

    def peek(self):
        """
        Nos permite ver el tope. No lo remueve ni actualiza la pila.
        """
        if len(self.pila) == 0:
            return None
        
        else:
         tope = self.pila[-1]

         return tope

    def empty(self):
        """
        Revisa si la lista es vacía. Regresa un booleano.
        """
        return len(self.pila) == 0
                