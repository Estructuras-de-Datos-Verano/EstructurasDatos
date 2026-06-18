class Pila:
    def __init__(self):
        self.pila_l = []
    def apilar(self, elemento):
        self.pila.append(elemento)
    def desapilar(self):
        self.pila = self.pila[:-1]
    def esta_vacia(self):
        if len(self.pila) == 0:
            return True
        else:
            return False
    def peek(self):
        return self.pila[-1]
 # Debe funcionar como en el .md