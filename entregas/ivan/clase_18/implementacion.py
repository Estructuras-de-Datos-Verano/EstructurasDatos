from __future__ import annotations

from math import isfinite

Peso = int | float
Arista = tuple[int, int, Peso]


class UnionFind:
    """Mantiene una partición de elementos enteros en conjuntos disjuntos."""

    def __init__(self, numero_elementos: int) -> None:
        if isinstance(numero_elementos, bool):
            raise TypeError("numero_elementos debe ser un entero")
        if not isinstance(numero_elementos, int):
            raise TypeError("numero_elementos debe ser un entero")
        if numero_elementos < 0:
            raise ValueError("numero_elementos debe ser no ngativo")

        self._padre = list(range(numero_elementos))
        self._tamano = [1] * numero_elementos
        self._componentes = numero_elementos

    def _validar_indice(self, elemento: int) -> None:
        if isinstance(elemento, bool):
            raise TypeError("índice inválido")
        if not isinstance(elemento, int):
            raise TypeError("índice inválido")
        if elemento < 0 or elemento >= len(self._padre):
            raise IndexError("índice fuera de rango")

    def find(self, elemento: int) -> int:
        """Devuelve la raíz de la componente de elemento."""

        self._validar_indice(elemento)
        if self._padre[elemento] != elemento:
            self._padre[elemento] = self.find(self._padre[elemento])
        return self._padre[elemento]

    def union(self, a: int, b: int) -> bool:
        """Une componentes y devuelve si la unión fue efectiva."""

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
        """Indica si dos elementos pertenecen a la misma componente."""
        return self.find(a) == self.find(b)
    

    def tamano_componente(self, elemento: int) -> int:
        """Devuelve el tamaño de la componente del elemento."""
        return self._tamano[self.find(elemento)]
    

    def numero_componentes(self) -> int:
        """Devuelve la cantidad actual de componentes."""
        return self._componentes


def kruskal(
    numero_vertices: int,
    aristas: list[Arista],
) -> tuple[float, list[tuple[int, int, float]]] | None:
    """Calcula un árbol de expansión mínima o devuelve None."""

    if isinstance(numero_vertices, bool):
        raise TypeError("numero_vertices inválido")
    if not isinstance(numero_vertices, int):
        raise TypeError("numero_vertices inválido")
    if numero_vertices < 0:
        raise ValueError("numero_vertices debe ser no negativo")

    aristas_copia: list[tuple[int, int, float]] = []
    for arista in aristas:
        if len(arista) != 3:
            raise ValueError("arista inválida")
        u, v, peso = arista

        if isinstance(u, bool) or not isinstance(u, int):
            raise TypeError("El vértice debe ser un entero")
        if isinstance(v, bool) or not isinstance(v, int):
            raise TypeError("El vértice debe ser un entero")
        if not (0 <= u < numero_vertices):
            raise IndexError("El vértice está fuera de rango")
        if not (0 <= v < numero_vertices):
            raise IndexError("El vértice está fuera de rango")
        if isinstance(peso, bool):
            raise TypeError("El peso debe ser un número")
        if not isinstance(peso, (int, float)):
            raise TypeError("El peso debe ser un número")

        peso = float(peso)
        if not isfinite(peso):
            raise ValueError("El peso no puede ser infinito")
        aristas_copia.append((u, v, peso))

    aristas_ordenadas = sorted(aristas_copia, key=lambda x: x[2])
    uf = UnionFind(numero_vertices)
    mst: list[tuple[int, int, float]] = []
    costo = 0.0

    for u, v, peso in aristas_ordenadas:
        if uf.union(u, v):
            mst.append((u, v, peso))
            costo += peso
            if len(mst) == numero_vertices - 1:
                break

    if numero_vertices == 0:
        return (0.0, [])
    if len(mst) != numero_vertices - 1:
        return None
    return costo, mst


def costo_reparacion(
    numero_ciudades: int,
    carreteras: list[tuple[int, int, int]],
) -> int | None:
    """Calcula el costo mínimo de conectar todas las ciudades."""

    aristas: list[Arista] = []
    for u, v, costo in carreteras:
        if isinstance(costo, bool):
            raise TypeError("El costo debe ser un entero")
        if not isinstance(costo, int):
            raise TypeError("El costo debe ser un entero")
        aristas.append((u, v, costo))

    resultado = kruskal(numero_ciudades, aristas)
    if resultado is None:
        return None
    costo_total, _ = resultado
    return int(costo_total)