from __future__ import annotations
import math

Peso = int | float
Arista = tuple[int, int, Peso]


class UnionFind:
    """Mantiene una partición de elementos enteros en conjuntos disjuntos."""

    def __init__(self, numero_elementos: int) -> None:
        if type(numero_elementos) is bool or not isinstance(numero_elementos, int):
            raise TypeError("La cantidad de elementos debe ser un entero.")
        if numero_elementos < 0:
            raise ValueError("La cantidad de elementos no puede ser negativa.")
        
        self._padre = list(range(numero_elementos))
        self._tamanos = [1] * numero_elementos
        self._componentes = numero_elementos
        self._num_elementos = numero_elementos

    def find(self, elemento: int) -> int:
        """Devuelve la raíz de la componente de ``elemento``."""
        if type(elemento) is bool or not isinstance(elemento, int):
            raise TypeError("El elemento a buscar debe ser un entero.")
        if not (0 <= elemento < self._num_elementos):
            raise IndexError(f"El elemento {elemento} está fuera de rango.")

        camino = []
        actual = elemento
        while actual != self._padre[actual]:
            camino.append(actual)
            actual = self._padre[actual]
            
        for nodo in camino:
            self._padre[nodo] = actual
            
        return actual

    def union(self, a: int, b: int) -> bool:
        """Une componentes y devuelve si la unión fue efectiva."""
        raiz_a = self.find(a)
        raiz_b = self.find(b)

        if raiz_a == raiz_b:
            return False

        if self._tamanos[raiz_a] < self._tamanos[raiz_b]:
            raiz_a, raiz_b = raiz_b, raiz_a
        elif self._tamanos[raiz_a] == self._tamanos[raiz_b]:
            if raiz_a > raiz_b:
                raiz_a, raiz_b = raiz_b, raiz_a

        self._padre[raiz_b] = raiz_a
        self._tamanos[raiz_a] += self._tamanos[raiz_b]
        self._componentes -= 1
        return True

    def conectados(self, a: int, b: int) -> bool:
        """Indica si dos elementos pertenecen a la misma componente."""
        return self.find(a) == self.find(b)

    def tamano_componente(self, elemento: int) -> int:
        """Devuelve el tamaño de la componente del elemento."""
        return self._tamanos[self.find(elemento)]

    def numero_componentes(self) -> int:
        """Devuelve la cantidad actual de componentes."""
        return self._componentes


def kruskal(
    numero_vertices: int,
    aristas: list[Arista],
) -> tuple[float, list[tuple[int, int, float]]] | None:
    """Calcula un árbol de expansión mínima o devuelve ``None``."""
    
    if type(numero_vertices) is bool or not isinstance(numero_vertices, int):
        raise TypeError("El número de vértices debe ser un entero.")
    if numero_vertices < 0:
        raise ValueError("El número de vértices no puede ser negativo.")
    if numero_vertices <= 1:
        return 0.0, []

    aristas_normalizadas = []
    for arista in aristas:
        if not isinstance(arista, tuple) or len(arista) != 3:
            raise ValueError("Las aristas deben ser tuplas de exactamente 3 elementos.")
        
        u, v, peso = arista
        
        if type(u) is bool or type(v) is bool or not isinstance(u, int) or not isinstance(v, int):
            raise TypeError("Los vértices extremos deben ser enteros.")
        if not (0 <= u < numero_vertices) or not (0 <= v < numero_vertices):
            raise IndexError("Los vértices extremos están fuera del rango válido.")
        if type(peso) is bool or not isinstance(peso, (int, float)):
            raise TypeError("El peso de la arista debe ser numérico.")
        if not math.isfinite(peso):
            raise ValueError("El peso de la arista debe ser un valor finito.")
            
        aristas_normalizadas.append((u, v, float(peso)))

    aristas_ordenadas = sorted(aristas_normalizadas, key=lambda x: x[2])
    
    uf = UnionFind(numero_vertices)
    elegidas = []
    costo_total = 0.0

    for u, v, peso in aristas_ordenadas:
        if uf.union(u, v):
            elegidas.append((u, v, peso))
            costo_total += peso
            if len(elegidas) == numero_vertices - 1:
                break

    if len(elegidas) < numero_vertices - 1:
        return None

    return costo_total, elegidas


def costo_reparacion(
    numero_ciudades: int,
    carreteras: list[tuple[int, int, int]],
) -> int | None:
    """Calcula el costo mínimo de conectar todas las ciudades."""
    if numero_ciudades == 1:
        return 0
        
    carreteras_kruskal = []
    for arista in carreteras:
        if not isinstance(arista, tuple) or len(arista) != 3:
            raise ValueError("Arista mal formada.")
        u, v, costo = arista
        if type(costo) is bool or not isinstance(costo, int):
            raise TypeError("El costo de reparación debe ser un entero.")
            
        carreteras_kruskal.append((u, v, float(costo)))

    resultado = kruskal(numero_ciudades, carreteras_kruskal)
    if resultado is None:
        return None
        
    costo_total, _ = resultado
    return int(costo_total)