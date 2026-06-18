class Interfaz:
    def __init__(self):
        self.pila = []
    def apilar(self, elemento):
        """Debe agregar un elemento al tope de la pila"""
        self.pila.append(elemento)

    def quitar(self):
        """Debe quitar el ultimo elemento agregado a la pila"""
        if self.empty():
            return None 
        return self.pila.pop()
    def peek(self):
        """Debe regrsar (sin eliminarlo) el ultimo elemento de la pila"""
        if self.empty():
            return None 
        return self.pila[-1]
    def empty(self):
        """Debe corroborar si la pila tiene algun elemento"""
        return len(self.pila) == 0
    