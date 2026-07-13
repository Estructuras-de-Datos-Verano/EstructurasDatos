from __future__ import annotations
from collections.abc import Iterable


class HeapMin:
    def __init__(self, valores: Iterable[int] | None = None) -> None:
        self.datos = []
        if valores is not None:
            self.construir_heap(valores)

    def esta_vacio(self) -> bool:
        if len(self.datos) == 0:
            return True
        else:
            return False

    def tamano(self) -> int:
       if self.esta_vacio == 0:
           raise ValueError("La lista no debe de estar vacia.")
       else:
           return len(self)

    def minimo(self) -> int:
        if self.esta_vacio == 0:
           raise ValueError("La lista no debe de estar vacia.")   
        min = None
        for _ in self.datos:
            if _ < min:
                min = _
        return min

    def insertar(self, valor: int) -> None:

        self.datos.append(valor)
        self._subir(self.datos, valor)

    def extraer_min(self) -> int:
        self.datos[1:]
        self.datos[0] = self.datos[-1]
        self._bajar(self.datos[0])
        return self.datos
    
    def construir_heap(self, valores: Iterable[int]) -> None:

        raise NotImplementedError

    def _subir(self, indice: int) -> None:
        if indice == self.datos[0]:
            raise ValueError("No se puede subir el primer elemento.")
        while indice > 0:
            for _ in self.valores:
                if self.datos[indice] <= self.datos[_]:
                  _padre = self._indice_padre(indice)
                  self.datos.append(indice)[_padre]
                else:
                    pass

    def _bajar(self, indice: int) -> None:
        if indice == self.datos[-1]:
            raise ValueError("No se puede bajar el ultimo elemento.")
        while indice < len(self.datos) -1:
            
            for _ in self.valores:
                if self.datos[indice] >= self.datos[_]:
                    _padre = self._indice_padre(_)
                    self.datos.append(indice)[_padre]
                else:
                    pass

    def _indice_padre(self, indice: int) -> int:
        padre = (indice - 1)// 2
        return padre

    def _indice_izquierdo(self, indice: int) -> int:
        izquierdo = 2 * indice + 1
        return izquierdo

    def _indice_derecho(self, indice: int) -> int:
        derecho = 2 * indice + 2
        return derecho

    def cumple_propiedad_heap(self) -> bool:

        raise NotImplementedError


def ultima_piedra(piedras: list[int]) -> int:

    raise NotImplementedError("Completa ultima_piedra en tu entrega")