class Pila:

    def __init__(self, elements=None):
        """
        El init toma a elements como None si no se declara, luego en dado de caso de que haya un parámetro lo iguala a self.elements si es lista y si no lo iguala a una vacía
        """
        self.elements = elements if isinstance(elements, list) else []

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        """
        El pop evita intentar quitar algo si es vacío, toma el ultimo elemento de la original y luego convierte a la original a la lista sin ese elemento
        Devuelve el elemento eliminado
        """
        if self.empty():
            return None

        last = self.elements[-1]
        self.elements = self.elements[:-1]
        return last

    def empty(self):
        """
        Comparación Sencilla, devuelve True si está vacía y false si no
        """
        return len(self.elements) == 0

    def peek(self):
        """
        Debuelve el último elemento
        """
        if self.empty():
            return None
        return self.elements[-1]
    def __str__(self):
        return ",".join(str(i) for i in self.elements)
    
stack = Pila()
print(stack.empty())
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.peek() == 3)
print(stack.pop() == 3)
print(stack)
