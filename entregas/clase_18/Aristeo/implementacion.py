
from __future__ import annotations
import math

Peso = int | float
Arista = tuple[int, int, Peso]


class UnionFind:
    """Mantiene una partición de elementos enteros en conjuntos disjuntos."""

    def __init__(self, numero_elementos: int) -> None:
        # 1. Validación de tipo del tamaño (bool hereda de int en Python, hay que rechazarlo explícitamente)
        if isinstance(numero_elementos, bool):
            raise TypeError("El número de elementos no puede ser un valor booleano.")
        if not isinstance(numero_elementos, int):
            raise TypeError("El número de elementos debe ser un entero.")
        if numero_elementos < 0:
            raise ValueError("El número de elementos no puede ser negativo.")

        self._padre = list(range(numero_elementos))
        self._tamano = [1] * numero_elementos
        self._componentes = numero_elementos

    def _validar_indice(self, elemento: int) -> None:
        """Valida que el índice sea de tipo entero, no sea bool y esté dentro del rango."""
        if isinstance(elemento, bool):
            raise TypeError("El índice no puede ser un valor booleano.")
        if not isinstance(elemento, int):
            raise TypeError("El índice debe ser un entero.")
        if elemento < 0 or elemento >= len(self._padre):
            raise IndexError(f"Índice {elemento} fuera de rango [0, {len(self._padre) - 1}].")

    def find(self, elemento: int) -> int:
        """Devuelve la raíz de la componente de ``elemento`` con compresión de caminos."""
        self._validar_indice(elemento)
        
        # Guardar el camino para compresión recursiva o iterativa
        camino = []
        actual = elemento
        while actual != self._padre[actual]:
            camino.append(actual)
            actual = self._padre[actual]
        
        # Compresión de caminos
        for nodo in camino:
            self._padre[nodo] = actual
            
        return actual

    def union(self, a: int, b: int) -> bool:
        """Une componentes por tamaño y devuelve si la unión fue efectiva."""
        self._validar_indice(a)
        self._validar_indice(b)

        raiz_a = self.find(a)
        raiz_b = self.find(b)

        if raiz_a == raiz_b:
            return False

        # Unión por tamaño (el árbol más chico se cuelga del más grande)
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
        """Devuelve el tamaño de la componente del elemento."""
        self._validar_indice(elemento)
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
    if isinstance(numero_vertices, bool):
        raise TypeError("El número de vértices no puede ser un booleano.")
    if not isinstance(numero_vertices, int):
        raise TypeError("El número de vértices debe ser un entero.")
    if numero_vertices < 0:
        raise ValueError("El número de vértices no puede ser negativo.")

    # Casos base rápidos
    if numero_vertices == 0:
        return (0.0, [])
    if numero_vertices == 1:
        return (0.0, [])

    # Copiar y validar rigurosamente la lista de aristas para no mutar la entrada original
    aristas_normalizadas: list[tuple[int, int, float]] = []
    for i, arista in enumerate(aristas):
        if not isinstance(arista, tuple) or len(arista) != 3:
            raise ValueError("Cada arista debe ser una tupla de 3 elementos: (u, v, peso).")
        
        u, v, peso = arista
        
        # Validar extremos (no bools, tipo entero y rango)
        if isinstance(u, bool) or isinstance(v, bool):
            raise TypeError("Los extremos de las aristas no pueden ser booleanos.")
        if not isinstance(u, int) or not isinstance(v, int):
            raise TypeError("Los extremos de las aristas deben ser enteros.")
        if u < 0 or u >= numero_vertices or v < 0 or v >= numero_vertices:
            raise IndexError("Vértice extremo fuera de rango válido.")

        # Validar pesos (no bools, tipo numérico finito, normalizados a float)
        if isinstance(peso, bool):
            raise TypeError("El peso de la arista no puede ser un booleano.")
        if not isinstance(peso, (int, float)):
            raise TypeError("El peso de la arista debe ser un número (int o float).")
        if not math.isfinite(peso):
            raise ValueError("El peso de la arista debe ser un número real finito.")

        aristas_normalizadas.append((u, v, float(peso)))

    # Ordenar aristas por peso de menor a mayor
    aristas_ordenadas = sorted(aristas_normalizadas, key=lambda x: x[2])

    # Algoritmo de Kruskal propiamente dicho usando Union-Find
    uf = UnionFind(numero_vertices)
    aristas_seleccionadas: list[tuple[int, int, float]] = []
    costo_acumulado = 0.0

    for u, v, peso in aristas_ordenadas:
        if uf.union(u, v):
            aristas_seleccionadas.append((u, v, peso))
            costo_acumulado += peso
            # Si ya tenemos V-1 aristas seleccionadas, podemos terminar temprano
            if len(aristas_seleccionadas) == numero_vertices - 1:
                break

    # Si terminamos y no conectamos todos los vértices, el grafo es desconectado
    if len(aristas_seleccionadas) < numero_vertices - 1:
        return None

    return (costo_acumulado, aristas_seleccionadas)


def costo_reparacion(
    numero_ciudades: int,
    carreteras: list[tuple[int, int, int]],
) -> int | None:
    """Calcula el costo mínimo de conectar todas las ciudades."""
    # Convertimos el problema a Kruskal estándar
    # Validamos que todos los costos sean estrictamente enteros según especificación
    aristas_kruskal: list[Arista] = []
    for u, v, costo in carreteras:
        if isinstance(costo, bool) or not isinstance(costo, int):
            raise TypeError("El costo en Road Reparation debe ser un entero estrictamente.")
        aristas_kruskal.append((u, v, costo))

    resultado = kruskal(numero_ciudades, aristas_kruskal)
    if resultado is None:
        return None

    costo_total, _ = resultado
    return int(costo_total)