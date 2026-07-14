from __future__ import annotations
from collections.abc import Iterable

class HeapMin:
    def __init__(self, valores: Iterable[int] | None = None) -> None:
        self.datos: list[int] = []
        if valores is not None:
            self.construir_heap(valores)

    def esta_vacio(self) -> bool:
        return len(self.datos) == 0

    def tamano(self) -> int:
        return len(self.datos)

    def minimo(self) -> int:
        if self.esta_vacio():
            raise IndexError("El heap está vacío.") 
        return self.datos[0]

    def insertar(self, valor: int) -> None:
        self.datos.append(valor)
        self._subir(len(self.datos) - 1)

    def extraer_min(self) -> int:
        if self.esta_vacio():
            raise IndexError("El heap está vacío.")
        
        min_valor = self.datos[0]
        ultimo_valor = self.datos.pop()
        
        if not self.esta_vacio():
            self.datos[0] = ultimo_valor
            self._bajar(0)
            
        return min_valor
    
    def construir_heap(self, valores: Iterable[int]) -> None:
        self.datos = list(valores)
        for i in range((len(self.datos) - 2) // 2, -1, -1):
            self._bajar(i)

    def _subir(self, indice: int) -> None:
        padre = self._indice_padre(indice)
        while indice > 0 and self.datos[indice] < self.datos[padre]:
            self.datos[indice], self.datos[padre] = self.datos[padre], self.datos[indice]
            indice = padre
            padre = self._indice_padre(indice)

    def _bajar(self, indice: int) -> None:
        tamano_total = len(self.datos)
        while self._indice_izquierdo(indice) < tamano_total:
            izq = self._indice_izquierdo(indice)
            der = self._indice_derecho(indice)
            hijo_menor = izq
            
            if der < tamano_total and self.datos[der] < self.datos[izq]:
                hijo_menor = der
                
            if self.datos[indice] <= self.datos[hijo_menor]:
                break
                
            self.datos[indice], self.datos[hijo_menor] = self.datos[hijo_menor], self.datos[indice]
            indice = hijo_menor

    def _indice_padre(self, indice: int) -> int:
        return (indice - 1) // 2

    def _indice_izquierdo(self, indice: int) -> int:
        return 2 * indice + 1

    def _indice_derecho(self, indice: int) -> int:
        return 2 * indice + 2

    def cumple_propiedad_heap(self) -> bool:
        for i in range(len(self.datos)):
            izq = self._indice_izquierdo(i)
            der = self._indice_derecho(i)
            if izq < len(self.datos) and self.datos[i] > self.datos[izq]:
                return False
            if der < len(self.datos) and self.datos[i] > self.datos[der]:
                return False
        return True


def ultima_piedra(piedras: list[int]) -> int:
    if not piedras:
        return 0
        
    heap = HeapMin([-peso for peso in piedras])
    
    while heap.tamano() >= 2:
        mayor = -heap.extraer_min()
        segundo = -heap.extraer_min()
        
        if mayor != segundo:
            diferencia = mayor - segundo
            heap.insertar(-diferencia)
            
    if heap.esta_vacio():
        return 0
    else:
        return -heap.extraer_min()
