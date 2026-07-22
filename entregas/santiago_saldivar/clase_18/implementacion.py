"""Código base de la Clase 18; no contiene las soluciones."""

from __future__ import annotations

import math

Peso = int | float
Arista = tuple[int, int, Peso]


class UnionFind:
    """Mantiene una partición de elementos enteros en conjuntos disjuntos."""

    def __init__(self, numero_elementos: int) -> None:

        if isinstance(numero_elementos, bool) or not isinstance(numero_elementos, int):
            raise TypeError("El número de elementos debe ser un entero")
        if numero_elementos < 0:
            raise ValueError("El número de elementos no puede ser negativo.")

        # Cada elemento comienza siendo raíz
        self._padre = list(range(numero_elementos))
        # Cada componente comienza con tamaño 1
        self._tamano = [1] * numero_elementos
        # Iniciando, cada elemento es su propio conjunto
        self._componentes = numero_elementos

    def find(self, elemento: int) -> int:
        """Devuelve la raíz de la componente de ``elemento``."""

        # Validaciones
        if isinstance(elemento, bool) or not isinstance(elemento, int):
            raise TypeError("El índice del elemento debe ser un entero.")
        if elemento < 0 or elemento >= len(self._padre):
            raise IndexError("Índice de elemento fuera de rango.")

        if self._padre[elemento] != elemento:
            #Si no es su padre...
            # Asocia el nodo hasta la raíz
            self._padre[elemento] = self.find(self._padre[elemento])
            # Recursivo
        return self._padre[elemento]

    def union(self, a: int, b: int) -> bool:
        """Une componentes y devuelve si la unión fue efectiva."""
        raiz_a = self.find(a)
        raiz_b = self.find(b)

        if raiz_a == raiz_b:
            return False
            # No procede si ya están en el mismo conjunto

        # Pegamos el árbol chico bajo el árbol grande
        if self._tamano[raiz_a] < self._tamano[raiz_b]:
            raiz_a, raiz_b = raiz_b, raiz_a
            # raiz_a siempre será el más grande
        self._padre[raiz_b] = raiz_a
        self._tamano[raiz_a] += self._tamano[raiz_b]
        # Sumamos los dos
        self._componentes -= 1
        # Ahora son un mismo subconjunto. Es decir, componente.
        return True

    def conectados(self, a: int, b: int) -> bool:
        """Indica si dos elementos pertenecen a la misma componente."""
        # Checa si comparten raíz
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
    
    # Validaciones

    if isinstance(numero_vertices, bool) or not isinstance(numero_vertices, int):
        raise TypeError("El número de vértices debe ser un entero.")
    
    if numero_vertices < 0:
        raise ValueError("El número de vértices no puede ser negativo.")

    if numero_vertices == 0:
        return 0.0, []
  
    for arista in aristas:
        if not isinstance (arista, tuple) or len(arista) != 3:
            raise ValueError("Cada arista debe ser una tupla de 3 elementos.")
        
        u, v, peso = arista

        if isinstance(u, bool) or not isinstance(u, int) or isinstance(v, bool) or not isinstance(v, int):
            raise TypeError("Los extremos de las aristas deben ser enteros.")
        
        if u < 0 or u >= numero_vertices or v < 0 or v >= numero_vertices:
            raise IndexError("Vértice fuera de rango para el número de vértices.")

        if isinstance(peso, bool) or not isinstance(peso,(int,float)):
            raise TypeError("El peso de la arista debe ser un valor numérico.")
        
        if not math.isfinite(peso):
            raise ValueError("El peso debe ser un número finito.")
    # Ordenar aristas
    # Esta parte domina la complejidad
    aristas_ordenadas = sorted(aristas, key=lambda x: x[2])

    uf = UnionFind(numero_vertices)
    mst_aristas: list[tuple[int, int, float]] = []
    mst_costo = 0.0

    # Une los vértices
    # Pero tiene que checar
    # y así
    for u, v, peso in aristas_ordenadas:
        # Si u y v no están unidos, los unimos
        if uf.union(u, v):
            mst_aristas.append((u, v, float(peso)))
            mst_costo += float(peso)
            # Si ya tenemos v - 1 aristas, el MST está completo
            if len(mst_aristas) == numero_vertices -1:
                break

    if numero_vertices > 1 and uf.numero_componentes() != 1:
        return None
    return mst_costo, mst_aristas

def costo_reparacion(
    numero_ciudades: int,
    carreteras: list[tuple[int, int, int]],
) -> int | None:
    """Calcula el costo mínimo de conectar todas las ciudades."""

    for carretera in carreteras:
        if not isinstance(carretera, tuple) or len(carretera) != 3:
            raise ValueError("Cada carretera debe ser una tupla de 3 elementos.")
        costo = carretera[2]
        if isinstance(costo, bool) or not isinstance(costo, int):
            raise TypeError("El costo de reparación debe ser un entero estrictamente.")

    # Validación básica
    if numero_ciudades <= 1:
        return 0
    
    # Convertimos las carreteras a un formato compatible
    aristas_kruskal: list[Arista] = []
    for u, v, costo in carreteras:
        # Ajustamos índices.
        aristas_kruskal.append((u,v,costo))

    resultado = kruskal(numero_ciudades, aristas_kruskal)

    if resultado is None:
        return None
    
    costo_total, _ = resultado
    return int(costo_total)
