from __future__ import annotations
import math

Peso = int | float
Arista = tuple[int, int, Peso]


class UnionFind:
    """Mantiene una partición de elementos enteros en conjuntos disjuntos."""

    def __init__(self, numero_elementos: int) -> None:
        if isinstance(numero_elementos, bool):
            raise TypeError("El número de elementos no puede ser booleano.")
        if not isinstance(numero_elementos, int):
            raise TypeError("El número de elementos debe ser entero.")
        if numero_elementos < 0:
            raise ValueError("El número de elementos no puede ser negativo.")

        self._padre = list(range(numero_elementos))
        self._tamano = [1] * numero_elementos
        self._componentes = numero_elementos

    def _validar_indice(self, elemento: int) -> None:
        if isinstance(elemento, bool):
            raise TypeError("El índice no puede ser booleano.")
        if not isinstance(elemento, int):
            raise TypeError("El índice debe ser entero.")
        if elemento < 0 or elemento >= len(self._padre):
            raise IndexError("Índice fuera de rango.")

    def find(self, elemento: int) -> int:
        """Devuelve la raíz de la componente de ``elemento`` con compresión de caminos."""
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
        """Une componentes usando unión por tamaño y devuelve si fue efectiva."""
        self._validar_indice(a)
        self._validar_indice(b)

        raiz_a = self.find(a)
        raiz_b = self.find(b)

        if raiz_a == raiz_b:
            return False

        # Unión por tamaño: el árbol pequeño se cuelga del grande
        if self._tamano[raiz_a] < self._tamano[raiz_b]:
            raiz_a, raiz_b = raiz_b, raiz_a

        self._padre[raiz_b] = raiz_a
        self._tamano[raiz_a] += self._tamano[raiz_b]
        self._componentes -= 1
        return True

    def conectados(self, a: int, b: int) -> bool:
        """Indica si dos elementos pertenecen a la misma componente."""
        self._validar_indice(a)
        self._validar_indice(b)
        return self.find(a) == self.find(b)

    def tamano_componente(self, elemento: int) -> int:
        """Devuelve el tamaño de la componente del elemento consultando la raíz."""
        self._validar_indice(elemento)
        raiz = self.find(elemento)
        return self._tamano[raiz]

    def numero_componentes(self) -> int:
        """Devuelve la cantidad actual de componentes independientes."""
        return self._componentes


def kruskal(
    numero_vertices: int,
    aristas: list[Arista],
) -> tuple[float, list[tuple[int, int, float]]] | None:
    """Calcula un árbol de expansión mínima mediante el algoritmo de Kruskal."""
    if isinstance(numero_vertices, bool):
        raise TypeError("numero_vertices no puede ser booleano.")
    if not isinstance(numero_vertices, int):
        raise TypeError("numero_vertices debe ser entero.")
    if numero_vertices < 0:
        raise ValueError("numero_vertices no puede ser negativo.")

    if not isinstance(aristas, list):
        raise TypeError("aristas debe ser una lista.")

    # Validar y normalizar aristas en una nueva lista protegida (no muta la original)
    aristas_normalizadas = []
    for arista in aristas:
        if not isinstance(arista, tuple) or len(arista) != 3:
            raise ValueError("Arista mal formada.")

        u, v, w = arista

        if isinstance(u, bool) or isinstance(v, bool):
            raise TypeError("Los extremos de la arista no pueden ser booleanos.")
        if not isinstance(u, int) or not isinstance(v, int):
            raise TypeError("Los extremos de la arista deben ser enteros.")

        if u < 0 or u >= numero_vertices or v < 0 or v >= numero_vertices:
            raise IndexError("Vértice fuera de rango.")

        if isinstance(w, bool):
            raise TypeError("El peso no puede ser booleano.")
        if not isinstance(w, (int, float)):
            raise TypeError("El peso debe ser numérico.")
        if not math.isfinite(w):
            raise ValueError("El peso debe ser un número finito (no inf ni nan).")

        aristas_normalizadas.append((u, v, float(w)))

    # Casos base para 0 o 1 vértice
    if numero_vertices == 0 or numero_vertices == 1:
        return (0.0, [])

    # Ordenar copia por peso ascendentemente
    aristas_normalizadas.sort(key=lambda x: x[2])

    uf = UnionFind(numero_vertices)
    elegidas = []
    costo_total = 0.0

    for u, v, w in aristas_normalizadas:
        if uf.union(u, v):
            elegidas.append((u, v, w))
            costo_total += w
            # Parada temprana matemática al alcanzar V - 1 aristas
            if len(elegidas) == numero_vertices - 1:
                break

    # Si no logramos recolectar V - 1 aristas, el grafo está desconectado
    if len(elegidas) != numero_vertices - 1:
        return None

    return (costo_total, elegidas)


def costo_reparacion(
    numero_ciudades: int,
    carreteras: list[tuple[int, int, int]],
) -> int | None:
    """Calcula el costo mínimo entero de conectar todas las ciudades (0-based)."""
    if isinstance(numero_ciudades, bool):
        raise TypeError("numero_ciudades no puede ser booleano.")
    if not isinstance(numero_ciudades, int):
        raise TypeError("numero_ciudades debe ser entero.")
    if numero_ciudades < 0:
        raise ValueError("numero_ciudades no puede ser negativo.")

    if not isinstance(carreteras, list):
        raise TypeError("carreteras debe ser una lista.")

    aristas_kruskal = []
    for c in carreteras:
        if not isinstance(c, tuple) or len(c) != 3:
            raise ValueError("Carretera mal formada.")
        u, v, w = c
        # Rechazar explícitamente flotantes en el costo para este método
        if isinstance(w, float):
            raise TypeError("El costo en costo_reparacion debe ser estrictamente entero (int).")
        if isinstance(w, bool) or not isinstance(w, int):
            raise TypeError("El costo debe ser entero.")
        aristas_kruskal.append((u, v, w))

    res = kruskal(numero_ciudades, aristas_kruskal)
    if res is None:
        return None

    costo, _ = res
    return int(costo)