class Pila:
    def __init__(self):
        self.pila = []

    def push(self, objeto):
        "añadir al tope (final de la lista)"
        self.pila.append(objeto)

    def pop(self):
        "quitar y devolver el tope; devolver None si está vacía"
        if len(self.pila) == 0:
            return None
        else:
            tope = self.pila[-1]
            self.pila.remove(tope)
        return tope

    def peek(self):
        "devolver el tope sin eliminar; None si está vacía"
        if len(self.pila) == 0:
            return None
        else:
            tope = self.pila[-1]
        return tope
    
    def esta_vacia(self):
        "True si no hay elementos"
        return len(self.pila) == 0
    
    def tamano(self):
        "número de elementos actuales"
        return f"La pila tiene {len(self.pila)} elementos"



#ejemplo de uso 
pila = Pila()
pila.push(1)
pila.push(2)
pila.push(3)
print(pila.tamano())  # La pila tiene 3 elementos
print(pila.peek())    # 3   
print(pila.pop())     # 3
print(pila.tamano())  # La pila tiene 2 elementos
print(pila.esta_vacia())  # False
print(pila.pop())     # 2
print(pila.pop())     # 1
print(pila.esta_vacia())  # True
