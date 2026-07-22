from __future__ import annotations
from collections.abc import Iterable

class HeapMin:
    """Min-heap de enteros representado con un arreglo indexado desde cero."""

    def __init__(self, valores: Iterable[int] | None = None) -> None:
        """Crea un heap vacío o lo construye a partir de ``valores``."""
        self._elementos: list[int] = []
        if valores is not None:
            self.construir_heap(valores)

    def esta_vacio(self) -> bool:
        """Devuelve ``True`` cuando el heap no almacena elementos."""
        return len(self._elementos) == 0

    def tamano(self) -> int:
        """Devuelve la cantidad de elementos almacenados."""
        return len(self._elementos)

    def minimo(self) -> int:
        """Consulta la raíz sin retirarla."""
        if self.esta_vacio():
            raise IndexError("El heap está vacío.")
        return self._elementos[0]

    def insertar(self, valor: int) -> None:
        """Agrega ``valor`` y restaura la propiedad mediante sift-up."""
        self._elementos.append(valor)
        self._subir(len(self._elementos) - 1)

    def extraer_min(self) -> int:
        """Retira y devuelve el mínimo usando sift-down."""
        if self.esta_vacio():
            raise IndexError("El heap está vacío.")
        
        if len(self._elementos) == 1:
            return self._elementos.pop()
            
        min_val = self._elementos[0]
        self._elementos[0] = self._elementos.pop()
        self._bajar(0)
        return min_val

    def construir_heap(self, valores: Iterable[int]) -> None:
        self._elementos = list(valores)
        n = len(self._elementos)
        if n > 1:
            for i in range(n // 2 - 1, -1, -1):
                self._bajar(i)

    def _subir(self, indice: int) -> None:
        while indice > 0:
            padre = self._indice_padre(indice)
            if self._elementos[padre] > self._elementos[indice]:
                self._elementos[padre], self._elementos[indice] = self._elementos[indice], self._elementos[padre]
                indice = padre
            else:
                break

    def _bajar(self, indice: int) -> None:
        n = len(self._elementos)
        while self._indice_izquierdo(indice) < n:
            izq = self._indice_izquierdo(indice)
            der = self._indice_derecho(indice)
            menor = izq
            
            if der < n and self._elementos[der] < self._elementos[izq]:
                menor = der
                
            if self._elementos[indice] <= self._elementos[menor]:
                break
                
            self._elementos[indice], self._elementos[menor] = self._elementos[menor], self._elementos[indice]
            indice = menor

    def _indice_padre(self, indice: int) -> int:
        if indice == 0:
            raise IndexError("La raíz no tiene padre.")
        return (indice - 1) // 2

    def _indice_izquierdo(self, indice: int) -> int:
        return 2 * indice + 1

    def _indice_derecho(self, indice: int) -> int:
        return 2 * indice + 2

    def cumple_propiedad_heap(self) -> bool:
        n = len(self._elementos)
        for i in range(n // 2):
            izq = self._indice_izquierdo(i)
            der = self._indice_derecho(i)
            if izq < n and self._elementos[i] > self._elementos[izq]:
                return False
            if der < n and self._elementos[i] > self._elementos[der]:
                return False
        return True


def ultima_piedra(piedras: list[int]) -> int:
    """Resuelve Last Stone Weight simulando un Max-Heap mediante un Min-Heap."""
    heap = HeapMin(valores=[-p for p in piedras])
    
    while heap.tamano() > 1:
        piedra1 = -heap.extraer_min()
        piedra2 = -heap.extraer_min()
        
        if piedra1 != piedra2:
            heap.insertar(-(piedra1 - piedra2))
            
    return -heap.minimo() if not heap.esta_vacio() else 0