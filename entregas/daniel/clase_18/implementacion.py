import math

class UnionFind:
    def __init__(self, numero_elementos):
        # El tipo bool en Python hereda de int, por lo que se debe validar explícitamente primero.
        if isinstance(numero_elementos, bool):
            raise TypeError("El número de elementos no puede ser booleano.")
        if not isinstance(numero_elementos, int):
            raise TypeError("El número de elementos debe ser un entero.")
        if numero_elementos < 0:
            raise ValueError("El número de elementos no puede ser negativo.")
        
        self._padre = list(range(numero_elementos))
        self._tamano = [1] * numero_elementos
        self._componentes = numero_elementos

    def _validar_indice(self, x):
        if isinstance(x, bool):
            raise TypeError("El índice no puede ser de tipo bool.")
        if not isinstance(x, int):
            raise TypeError("El índice debe ser un entero.")
        if x < 0 or x >= len(self._padre):
            raise IndexError(f"Índice fuera de rango: {x}.")

    def find(self, x):
        self._validar_indice(x)
        if self._padre[x] != x:
            self._padre[x] = self.find(self._padre[x])
        return self._padre[x]

    def union(self, a, b):
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

    def conectados(self, a, b):
        self._validar_indice(a)
        self._validar_indice(b)
        return self.find(a) == self.find(b)

    def tamano_componente(self, x):
        self._validar_indice(x)
        return self._tamano[self.find(x)]

    def numero_componentes(self):
        return self._componentes


def kruskal(numero_vertices, aristas):
    if isinstance(numero_vertices, bool):
        raise TypeError("El número de vértices no puede ser un booleano.")
    if not isinstance(numero_vertices, int):
        raise TypeError("El número de vértices debe ser un entero.")
    if numero_vertices < 0:
        raise ValueError("El número de vértices no puede ser negativo.")
    
    if numero_vertices <= 1:
        return (0.0, [])
    
    aristas_normalizadas = []
    for i, arista in enumerate(aristas):
        if len(arista) != 3:
            raise ValueError(f"La arista en la posición {i} no cumple el formato (u, v, peso).")
        u, v, peso = arista
        
        if isinstance(u, bool) or isinstance(v, bool):
            raise TypeError("Los extremos de las aristas no pueden ser de tipo booleano.")
        if not isinstance(u, int) or not isinstance(v, int):
            raise TypeError("Los extremos de las aristas deben ser enteros.")
        if u < 0 or u >= numero_vertices or v < 0 or v >= numero_vertices:
            raise IndexError(f"Vértices fuera de rango en la arista ({u}, {v}).")
        
        if isinstance(peso, bool):
            raise TypeError("El peso de la arista no puede ser un booleano.")
        if not isinstance(peso, (int, float)):
            raise TypeError("El peso de la arista debe ser un entero o un flotante.")
        if not math.isfinite(peso):
            raise ValueError("El peso debe ser un número finito.")
        
        aristas_normalizadas.append((u, v, float(peso)))
    
    aristas_ordenadas = sorted(aristas_normalizadas, key=lambda x: x[2])
    
    uf = UnionFind(numero_vertices)
    aristas_seleccionadas = []
    costo_total = 0.0
    
    for u, v, peso in aristas_ordenadas:
        if uf.union(u, v):
            aristas_seleccionadas.append((u, v, peso))
            costo_total += peso
            if len(aristas_seleccionadas) == numero_vertices - 1:
                break
                
    if len(aristas_seleccionadas) != numero_vertices - 1:
        return None
        
    return (costo_total, aristas_seleccionadas)


def costo_reparacion(numero_ciudades, carreteras):
    # El test de Road Reparation exige explícitamente rechazar costos flotantes
    for i, arista in enumerate(carreteras):
        if len(arista) == 3:
            _, _, peso = arista
            if isinstance(peso, float):
                raise TypeError("El costo en las carreteras de Road Reparation debe ser un entero.")
                
    resultado = kruskal(numero_ciudades, carreteras)
    if resultado is None:
        return None
    costo, _ = resultado
    return int(costo)