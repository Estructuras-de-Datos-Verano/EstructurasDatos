from __future__ import annotations
import math

Peso = int | float
Arista = tuple[int, int, Peso]


class UnionFind:

    def __init__(self, numero_elementos: int) -> None:
        if isinstance(numero_elementos, bool):
            raise TypeError("El número de elementos no puede ser bool")
        if not isinstance(numero_elementos, int):
            raise TypeError("El número de elementos debe ser entero")
        if numero_elementos < 0:
            raise ValueError("El número de elementos no puede ser negativo")
        self._n = numero_elementos
        self._padre = list(range(numero_elementos))
        self._tamano = [1] * numero_elementos
        self._componentes = numero_elementos

    def _validar_indice(self, elemento: int) -> None:
        if isinstance(elemento, bool):
            raise TypeError("El índice no puede ser bool")
        if not isinstance(elemento, int):
            raise TypeError("El índice debe ser entero")
        if elemento < 0 or elemento >= self._n:
            raise IndexError("Índice fuera de rango")

    def find(self, elemento: int) -> int:
        self._validar_indice(elemento)
        camino = []
        curr = elemento
        while curr != self._padre[curr]:
            camino.append(curr)
            curr = self._padre[curr]
        for nodo in camino:
            self._padre[nodo] = curr
        return curr

    def union(self, a: int, b: int) -> bool:
        self._validar_indice(a)
        self._validar_indice(b)
        raiz_a = self.find(a)
        raiz_b = self.find(b)
        if raiz_a == raiz_b:
            return False
        if self._tamano[raiz_a] < self._tamano[raiz_b]:
            raiz_a, raiz_b = raiz_b, raiz_a
        self._padre[raiz_b] = raiz_a
        self._tamano[raiz_a] += self._tamano[raiz_b]
        self._componentes -= 1
        return True

    def conectados(self, a: int, b: int) -> bool:
        self._validar_indice(a)
        self._validar_indice(b)
        return self.find(a) == self.find(b)

    def tamano_componente(self, elemento: int) -> int:
        self._validar_indice(elemento)
        return self._tamano[self.find(elemento)]

    def numero_componentes(self) -> int:
        return self._componentes


def kruskal(
    numero_vertices: int,
    aristas: list[Arista],
) -> tuple[float, list[tuple[int, int, float]]] | None:
    if isinstance(numero_vertices, bool):
        raise TypeError("Número de vértices no puede ser bool")
    if not isinstance(numero_vertices, int):
        raise TypeError("Número de vértices debe ser entero")
    if numero_vertices < 0:
        raise ValueError("Número de vértices no puede ser negativo")

    if numero_vertices == 0:
        return (0.0, [])
    if numero_vertices == 1:
        return (0.0, [])

    copia = []
    for arista in aristas:
        
        if not isinstance(arista, tuple):
            raise TypeError("La arista debe ser una tupla")
        if len(arista) != 3:
            raise ValueError("Formato de arista inválido: debe tener 3 elementos")
            
        u, v, w = arista
        if isinstance(u, bool) or isinstance(v, bool) or isinstance(w, bool):
            raise TypeError("Tipos de datos no pueden ser bool")
        if not isinstance(u, int) or not isinstance(v, int):
            raise TypeError("Los vértices deben ser enteros")
        if not isinstance(w, (int, float)):
            raise TypeError("El peso debe ser numérico")
        if not math.isfinite(w):
            raise ValueError("El peso debe ser un número finito")
        if u < 0 or u >= numero_vertices or v < 0 or v >= numero_vertices:
            raise IndexError("Vértice de arista fuera de rango")
        copia.append((u, v, float(w)))

    copia.sort(key=lambda x: x[2])
    uf = UnionFind(numero_vertices)
    mst_aristas = []
    costo_total = 0.0

    for u, v, w in copia:
        if u == v:
            continue
        if uf.union(u, v):
            mst_aristas.append((u, v, w))
            costo_total += w
            if len(mst_aristas) == numero_vertices - 1:
                break

    if len(mst_aristas) < numero_vertices - 1:
        return None

    return (costo_total, mst_aristas)


def costo_reparacion(
    numero_ciudades: int,
    carreteras: list[tuple[int, int, int]],
) -> int | None:
    for carretera in carreteras:
        if not isinstance(carretera, tuple) or len(carretera) != 3:
            raise ValueError("Formato de carretera inválido")
        u, v, w = carretera
        
        if isinstance(w, float) and not isinstance(w, bool):
            raise TypeError("El costo de la carretera debe ser entero, no float")
            
    resultado = kruskal(numero_ciudades, carreteras)
    if resultado is None:
        return None
    return int(round(resultado[0]))