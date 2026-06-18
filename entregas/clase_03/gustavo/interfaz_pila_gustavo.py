
class Pila:
    def __init__(self):
        self.items = []

    def push(self, elemento):
        """Agrega un elemento al tope de la pila."""
        self.items.append(elemento)

    def pop(self):
        """Elimina y regresa el elemento del tope. Lanza error si está vacía."""
        if self.esta_vacia():
            raise IndexError("Error: La pila está vacía. No se puede hacer pop().")
        return self.items.pop()

    def peek(self):
        """Regresa el elemento del tope sin eliminarlo. Lanza error si está vacía."""
        if self.esta_vacia():
            raise IndexError("Error: La pila está vacía. No se puede hacer peek().")
        # El tope es el último elemento de la lista (-1)
        return self.items[-1]

    def esta_vacia(self):
        """Regresa True si no hay elementos, False en caso contrario."""
        return len(self.items) == 0

    def tamano(self):
        """Regresa la cantidad de elementos en la pila."""
        return len(self.items)


# === Ejemplo de uso ===

mi_pila = Pila()

# Agregamos elementos
mi_pila.push(5)
mi_pila.push(10)
mi_pila.push(15)

print(f"Tamaño de la pila: {mi_pila.tamano()}")  # Debería ser 3
print(f"Elemento en el tope (peek): {mi_pila.peek()}")  # Debería ser 15

# Sacamos elementos
print(f"Elemento eliminado (pop): {mi_pila.pop()}")  # Saca el 15
print(f"Nuevo elemento en el tope: {mi_pila.peek()}")  # Ahora es 10

print(f"¿Está vacía la pila?: {mi_pila.esta_vacia()}")  # False
