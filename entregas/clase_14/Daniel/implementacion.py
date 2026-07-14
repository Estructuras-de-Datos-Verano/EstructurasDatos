import heapq
from typing import List, Any

class HeapMin:
    

    def __init__(self, elementos: List[Any] = None) -> None:
        # Si no nos dan elementos, empezamos con una lista vacía
        if elementos is None:
            self._arreglo: List[Any] = []
        else:
            # Hacemos una copia para no alterar la lista original del usuario
            self._arreglo = list(elementos)  
            # construimos el heap a partir de la lista dada
            self._construir_heap()

    def vacio(self) -> bool:
        # Nos dice si la estructura no tiene nada
        return len(self._arreglo) == 0

    def tamano(self) -> int:
        # Nos dice cuántas cosas hay guardadas
        return len(self._arreglo)

    def minimo(self) -> Any:
        # Solo echa un vistazo al elemento más chico (que está al inicio) sin sacarlo
        if self.vacio():
            raise IndexError("No puedes ver el mínimo de un heap vacío.")
        return self._arreglo[0]

    def insertar(self, valor: Any) -> None:
        # Ponemos el nuevo elemento al final de la lista
        self._arreglo.append(valor)
        # Lo ayudamos a "flotar" hacia arriba hasta que encuentre su lugar correcto
        self._subir(len(self._arreglo) - 1)

    def extraer_minimo(self) -> Any:
        if self.vacio():
            raise IndexError("No puedes sacar nada de un heap vacío.")
        
        # Guardamos el más chico para devolverlo al final
        min_valor = self._arreglo[0]
        # Agarramos el último elemento de la lista para rellenar el hueco de la raíz
        ultimo_valor = self._arreglo.pop()
        
        if not self.vacio():
            self._arreglo[0] = ultimo_valor
            # Como este último valor suele ser grande, lo "hundimos" a su lugar ideal
            self._bajar(0)
            
        return min_valor

    def cumple_propiedad_heap(self) -> bool:
        # Revisa que ningún papá sea más grande que sus hijos
        n = len(self._arreglo)
        for i in range(n):
            izq = 2 * i + 1
            der = 2 * i + 2
            if izq < n and self._arreglo[i] > self._arreglo[izq]:
                return False
            if der < n and self._arreglo[i] > self._arreglo[der]:
                return False
        return True

    def _subir(self, i: int) -> None:
        # Compara el elemento con su papá y, si es más chico, lo intercambia para que suba
        actual = i
        while actual > 0:
            padre = (actual - 1) // 2
            if self._arreglo[padre] <= self._arreglo[actual]:
                break  # Si el papá ya es menor o igual, todo está en orden
            # Intercambio de posiciones
            self._arreglo[actual], self._arreglo[padre] = self._arreglo[padre], self._arreglo[actual]
            actual = padre

    def _bajar(self, i: int) -> None:
        # Compara el elemento con sus dos hijos, busca al hijo más chico y baja si es necesario
        actual = i
        n = len(self._arreglo)
        
        while True:
            menor = actual
            izq = 2 * i + 1
            der = 2 * i + 2
            
            # ¿El hijo izquierdo es menor?
            if izq < n and self._arreglo[izq] < self._arreglo[menor]:
                menor = izq
            # ¿El hijo derecho es todavía más chico?
            if der < n and self._arreglo[der] < self._arreglo[menor]:
                menor = der
                
            # Si el menor sigue siendo él mismo, ya llegó a su lugar
            if menor == actual:
                break
                
            # Intercambio de posiciones con el hijo más chico
            self._arreglo[actual], self._arreglo[menor] = self._arreglo[menor], self._arreglo[actual]
            actual = menor
            i = menor

    def _construir_heap(self) -> None:
        # Acomoda una lista desordenada desde la mitad hacia atrás de forma eficiente
        n = len(self._arreglo)
        for i in range((n // 2) - 1, -1, -1):
            self._bajar(i)


def ultima_piedra(piedras: List[int]) -> int:
   
    # Pasamos todo a negativo para simular un "Max-Heap"
    max_heap = [-p for p in piedras]
    heapq.heapify(max_heap)
    
    # Mientras queden al menos dos piedras para chocar
    while len(max_heap) > 1:
        # Sacamos las dos más pesadas (recordando quitarles el negativo)
        piedra1 = -heapq.heappop(max_heap)
        piedra2 = -heapq.heappop(max_heap)
        
        # Si no son iguales, se destruyen parcialmente y queda una diferencia
        if piedra1 != piedra2:
            diferencia = piedra1 - piedra2
            heapq.heappush(max_heap, -diferencia)
            
    # Si quedó una piedra la regresamos en positivo; si no quedó ninguna, devolvemos 0
    return -max_heap[0] if max_heap else 0