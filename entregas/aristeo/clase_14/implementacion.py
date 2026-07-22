import heapq

class HeapMin:
    def __init__(self, datos=None):
        self.heap = []
        if datos:
            self.construir_heap(datos)

    def esta_vacio(self) -> bool:
        return len(self.heap) == 0

    def tamano(self) -> int:
        return len(self.heap)

    def minimo(self) -> int:
        if self.esta_vacio():
            raise IndexError("Consultar desde un heap vacío")
        return self.heap[0]

    def insertar(self, valor: int) -> None:
        self.heap.append(valor)
        self._subir(len(self.heap) - 1)

    def _subir(self, i: int) -> None:
        while i > 0:
            padre = (i - 1) // 2
            if self.heap[padre] <= self.heap[i]:
                break
            self.heap[padre], self.heap[i] = self.heap[i], self.heap[padre]
            i = padre

    def extraer_min(self) -> int:
        if self.esta_vacio():
            raise IndexError("Extraer desde un heap vacío")
        min_val = self.heap[0]
        ultimo = self.heap.pop()
        if not self.esta_vacio():
            self.heap[0] = ultimo
            self._bajar(0)
        return min_val

    def _bajar(self, i: int) -> None:
        n = len(self.heap)
        while True:
            izq = 2 * i + 1
            der = 2 * i + 2
            menor = i
            
            if izq < n and self.heap[izq] < self.heap[menor]:
                menor = izq
            if der < n and self.heap[der] < self.heap[menor]:
                menor = der
                
            if menor == i:
                break
            self.heap[i], self.heap[menor] = self.heap[menor], self.heap[i]
            i = menor

    def construir_heap(self, datos: list[int]) -> None:
        self.heap = list(datos)
        # Floyd's Heap Construction Algorithm: O(n)
        for i in reversed(range(len(self.heap) // 2)):
            self._bajar(i)

    def cumple_propiedad_heap(self) -> bool:
        for i in range(1, len(self.heap)):
            padre = (i - 1) // 2
            if self.heap[padre] > self.heap[i]:
                return False
        return True
    
def ultima_piedra(piedras: list[int]) -> int:
    # No mutar la lista original, creamos una copia transformada
    max_heap = [-p for p in piedras]
    heapq.heapify(max_heap)
    
    while len(max_heap) > 1:
        # Recuperamos los valores positivos usando la negación
        primera = -heapq.heappop(max_heap)
        segunda = -heapq.heappop(max_heap)
        
        if primera != segunda:
            heapq.heappush(max_heap, -(primera - segunda))
            
    return -max_heap[0] if max_heap else 0

