class Pila:

    def __init__(self):
        self.pila = []  

    def apilar(self, item):
        self.pila.append(item)

    def desapilar(self):
        return self.pila.pop()
    
    def esta_vacia(self):
        return len(self.pila) == 0
    
    def peek(self):
        if self.esta_vacia():
            return None
        else: 
            return self.pila[-1]

    def tamano(self):
        return len(self.pila)
    

    