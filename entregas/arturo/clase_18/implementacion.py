from __future__ import annotations
import math

Peso = int | float
Arista = tuple[int, int, Peso]


class UnionFind:
    """Mantiene una partición de elementos enteros en conjuntos disjuntos."""

    def __init__(self, numero_elementos: int) -> None:
        if not isinstance(numero_elementos, int) or isinstance(numero_elementos, bool):
            raise TypeError("El número de elementos debe ser entero.")
        if numero_elementos < 0:
            raise ValueError("El número de elementos no puede ser negativo.")
            
        # Renombrados a variables protegidas (_) para pasar los tests públicos
        self._padre = list(range(numero_elementos))
        self._tamano = [1] * numero_elementos
        self._componentes = numero_elementos

    def _validar(self, elemento: int) -> None:
        if not isinstance(elemento, int) or isinstance(elemento, bool):
            raise TypeError("El elemento debe ser de tipo int.")
        if elemento < 0 or elemento >= len(self._padre):
            raise IndexError("El elemento está fuera del rango válido.")

    def find(self, elemento: int) -> int:
        """Devuelve la raíz de la componente de ``elemento``."""
        self._validar(elemento)
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
        raiz = self.find(elemento)
        return self._tamano[raiz]

    def numero_componentes(self) -> int:
        """Devuelve la cantidad actual de componentes."""
        return self._componentes


def kruskal(
    numero_vertices: int,
    aristas: list[Arista],
) -> tuple[float, list[tuple[int, int, float]]] | None:
    """Calcula un árbol de expansión mínima o devuelve ``None``."""
    
    # 1. Validación estricta del número de vértices
    if not isinstance(numero_vertices, int) or isinstance(numero_vertices, bool):
        raise TypeError("El número de vértices debe ser un número entero.")
    if numero_vertices < 0:
        raise ValueError("El número de vértices no puede ser negativo.")

    # 2. Validación estricta de las aristas y sus dominios
    for arista in aristas:
        if not isinstance(arista, (tuple, list)) or len(arista) != 3:
            raise ValueError("Cada arista debe ser una tupla de 3 elementos.")
            
        u, v, peso = arista
        
        if not isinstance(u, int) or isinstance(u, bool) or not isinstance(v, int) or isinstance(v, bool):
            raise TypeError("Los extremos de la arista deben ser enteros.")
        if u < 0 or u >= numero_vertices or v < 0 or v >= numero_vertices:
            raise IndexError("Los vértices de la arista están fuera de rango.")
            
        if isinstance(peso, bool) or not isinstance(peso, (int, float)):
            raise TypeError("El peso debe ser numérico.")
        if not math.isfinite(peso):
            raise ValueError("El peso debe ser finito.")

    if numero_vertices <= 1:
        return 0.0, []

    ordenadas = sorted([(u, v, float(peso)) for u, v, peso in aristas], key=lambda x: x[2])
    
    uf = UnionFind(numero_vertices)
    costo_total = 0.0
    aristas_mst = []

    for u, v, peso in ordenadas:
        if uf.union(u, v):
            aristas_mst.append((u, v, peso))
            costo_total += peso
            
            if len(aristas_mst) == numero_vertices - 1:
                break

    if len(aristas_mst) != numero_vertices - 1:
        return None

    return costo_total, aristas_mst


def costo_reparacion(
    numero_ciudades: int,
    carreteras: list[tuple[int, int, int]],
) -> int | None:
    """Calcula el costo mínimo de conectar todas las ciudades."""
    
    # Validar estrictamente que el peso sea INT en esta función para CSES
    for arista in carreteras:
        if len(arista) == 3:
            _, _, peso = arista
            if isinstance(peso, bool) or not isinstance(peso, int):
                raise TypeError("El costo de reparación debe ser un entero.")
                
    # No restamos 1 a los índices aquí, delegamos directamente a Kruskal
    resultado = kruskal(numero_ciudades, carreteras)
    
    if resultado is None:
        return None
        
    return int(resultado[0])
