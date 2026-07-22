import math
from typing import Union, Tuple, List

Peso = Union[int, float]
Arista = Tuple[int, int, Peso]

class UnionFind:

    def __init__(self, numero_elementos: int) -> None:
        if type(numero_elementos) is not int:
            raise TypeError("El número de elementos debe ser de tipo int.")
        if numero_elementos < 0:
            raise ValueError("El número de elementos no puede ser negativo.")
        self._padre = list(range(numero_elementos))
        self._tamano = [1] * numero_elementos
        self.componentes = numero_elementos

    def find(self, elemento: int) -> int:
        if type(elemento) is not int:
            raise TypeError("El elemento debe ser de tipo int.")
        if elemento < 0 or elemento >= len(self._padre):
            raise IndexError("El elemento está fuera de rango.")
        if self._padre[elemento] != elemento:
            self._padre[elemento] = self.find(self._padre[elemento])
        return self._padre[elemento]

    def union(self, a: int, b: int) -> bool:
        raiz_a = self.find(a)
        raiz_b = self.find(b)
        if raiz_a == raiz_b:
            return False
        if self._tamano[raiz_a] < self._tamano[raiz_b]:
            raiz_a, raiz_b = raiz_b, raiz_a

        self._padre[raiz_b] = raiz_a
        self._tamano[raiz_a] += self._tamano[raiz_b]
        self.componentes -= 1
        return True

    def conectados(self, a: int, b: int) -> bool:
        return self.find(a) == self.find(b)

    def tamano_componente(self, elemento: int) -> int:
        return self._tamano[self.find(elemento)]

    def numero_componentes(self) -> int:
        return self.componentes


def kruskal(_vertices: int, aristas: list[Arista],) -> tuple[float, list[tuple[int, int, float]]] | None:
    if type(_vertices) is not int:
        raise TypeError("El número de vértices debe ser de tipo int.")
    if _vertices < 0:
        raise ValueError("El número de vértices no puede ser negativo.")
    aristas_validas = []
    for arista in aristas:
        if type(arista) is not tuple or len(arista) != 3:
            raise ValueError("Cada arista debe ser una tupla de 3 elementos.")
        u, v, peso = arista
        if type(u) is not int or type(v) is not int:
            raise TypeError("Los extremos de la arista deben ser enteros.")
        if u < 0 or u >= _vertices or v < 0 or v >= _vertices:
            raise IndexError("Vértice fuera de rango.")
        if type(peso) not in (int, float):
            raise TypeError("El peso debe ser numérico (int o float).")
        if not math.isfinite(peso):
            raise ValueError("El peso no puede ser infinito ni NaN.")
        aristas_validas.append((u, v, float(peso)))
    uf = UnionFind(_vertices)
    aristas_ordenadas = sorted(aristas_validas, key=lambda x: x[2])
    total = 0
    mst_aristas: list[tuple[int, int, float]] = []

    for u, v, peso in aristas_ordenadas:
        if uf.union(u, v):
            total += peso
            mst_aristas.append((u, v, peso))
    if _vertices > 0 and uf.numero_componentes() > 1:
        return None

    return total, mst_aristas


def costo_reparacion(numero_ciudades: int, carreteras: list[tuple[int, int, int]],) -> int | None:
    if type(numero_ciudades) is not int:
        raise TypeError("El número de ciudades debe ser de tipo int.")
    if numero_ciudades < 0:
        raise ValueError("El número de ciudades no puede ser negativo.")
    carreteras_validas = []
    for arista in carreteras:
        if type(arista) is not tuple or len(arista) != 3:
            raise ValueError("Cada arista debe ser una tupla de 3 elementos.")
        u, v, costo = arista
        if type(u) is not int or type(v) is not int:
            raise TypeError("Las ciudades origen y destino deben ser enteras.")
        if u < 0 or u >= numero_ciudades or v < 0 or v >= numero_ciudades:
            raise IndexError("Ciudad fuera del rango permitido.")
        if type(costo) is not int:  
            raise TypeError("El costo debe ser obligatoriamente un número entero.")  
        carreteras_validas.append((u, v, costo))
    uf = UnionFind(numero_ciudades)
    carreteras_ordenadas = sorted(carreteras_validas, key=lambda x: x[2])
    total = 0
    for u, v, costo in carreteras_ordenadas:
        if uf.union(u, v):
            total += costo
    if numero_ciudades > 0 and uf.numero_componentes() > 1:
        return None
    return total