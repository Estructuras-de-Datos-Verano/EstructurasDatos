from collections import deque
from math import inf


class NodoSimple:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None


class NodoDoble(NodoSimple):
    def __init__(self, valor):
        super().__init__(valor)
        self.anterior = None


class ColaLigada:
    def __init__(self):
        self._frente = None
        self._final = None
        self._tamano = 0

    def encolar(self, valor):
        nodo = NodoSimple(valor)
        if self._final is None:
            self._frente = nodo
        else:
            self._final.siguiente = nodo
        self._final = nodo
        self._tamano += 1

    def desencolar(self):
        if self._frente is None:
            raise IndexError("cola vacía")
        nodo = self._frente
        valor = nodo.valor
        self._frente = nodo.siguiente
        if self._frente is None:
            self._final = None
        nodo.siguiente = None
        self._tamano -= 1
        return valor

    def esta_vacia(self):
        return self._tamano == 0

    def primero(self):
        if self._frente is None:
            raise IndexError("cola vacía")
        return self._frente.valor

    def __len__(self):
        return self._tamano


class DequeLigada:
    def __init__(self):
        self._inicio = None
        self._final = None
        self._tamano = 0

    def agregar_inicio(self, valor):
        nodo = NodoDoble(valor)
        if self._inicio is None:
            self._inicio = self._final = nodo
        else:
            nodo.siguiente = self._inicio
            self._inicio.anterior = nodo
            self._inicio = nodo
        self._tamano += 1

    def agregar_final(self, valor):
        nodo = NodoDoble(valor)
        if self._final is None:
            self._inicio = self._final = nodo
        else:
            nodo.anterior = self._final
            self._final.siguiente = nodo
            self._final = nodo
        self._tamano += 1

    def quitar_inicio(self):
        if self._inicio is None:
            raise IndexError("deque vacío")
        nodo = self._inicio
        valor = nodo.valor
        self._inicio = nodo.siguiente
        if self._inicio is None:
            self._final = None
        else:
            self._inicio.anterior = None
        nodo.anterior = None
        nodo.siguiente = None
        self._tamano -= 1
        return valor

    def quitar_final(self):
        if self._final is None:
            raise IndexError("deque vacío")
        nodo = self._final
        valor = nodo.valor
        self._final = nodo.anterior
        if self._final is None:
            self._inicio = None
        else:
            self._final.siguiente = None
        nodo.anterior = None
        nodo.siguiente = None
        self._tamano -= 1
        return valor

    def esta_vacia(self):
        return self._tamano == 0

    def primero(self):
        if self._inicio is None:
            raise IndexError("deque vacío")
        return self._inicio.valor

    def ultimo(self):
        if self._final is None:
            raise IndexError("deque vacío")
        return self._final.valor

    def __len__(self):
        return self._tamano


def bfs_predecesores(grafo, origen):
    if origen not in grafo:
        raise KeyError(f"origen {origen} no encontrado")

    predecesores = {nodo: None for nodo in grafo}
    cola = ColaLigada()
    cola.encolar(origen)
    predecesores[origen] = None

    while not cola.esta_vacia():
        nodo = cola.desencolar()
        for vecino in grafo.get(nodo, []):
            if vecino not in predecesores:
                predecesores[vecino] = nodo
                cola.encolar(vecino)

    return predecesores


def bfs_camino(grafo, origen, destino):
    if origen not in grafo:
        raise KeyError(f"origen {origen} no encontrado")
    if destino in grafo:
        if destino == origen:
            return [destino]
    predecesores = bfs_predecesores(grafo, origen)
    if destino not in predecesores:
        raise KeyError(f"destino {destino} no encontrado")
    return reconstruir_camino(predecesores, origen, destino)


def reconstruir_camino(predecesores, inicio, fin=None):
    if fin is None:
        nodo = inicio
        camino = []
        visitados = set()
        while nodo is not None:
            if nodo in visitados:
                raise ValueError("ciclo detectado")
            visitados.add(nodo)
            camino.append(nodo)
            if nodo not in predecesores:
                break
            padre = predecesores[nodo]
            if padre is None:
                break
            nodo = padre
        if len(camino) == 1:
            if any(valor == camino[0] for valor in predecesores.values()):
                return [camino[0]]
            return []
        return list(reversed(camino))

    if inicio == fin:
        return [inicio]

    camino = []
    actual = fin
    visitados = set()
    while actual is not None:
        if actual in visitados:
            raise ValueError("ciclo detectado")
        visitados.add(actual)
        camino.append(actual)
        if actual == inicio:
            return list(reversed(camino))
        padre = predecesores.get(actual)
        if padre is None:
            return []
        actual = padre

    return []


def _validar_peso(peso):
    if isinstance(peso, bool) or not isinstance(peso, int):
        raise TypeError("peso debe ser un entero 0 o 1")
    if peso not in (0, 1):
        raise ValueError("peso debe ser 0 o 1")


def cero_uno_bfs(grafo, origen):
    if origen not in grafo:
        raise KeyError(f"origen {origen} no encontrado")

    distancias = {nodo: inf for nodo in grafo}
    predecesores = {nodo: None for nodo in grafo}
    distancias[origen] = 0

    cola = deque()
    cola.append(origen)

    while cola:
        nodo = cola.popleft()
        for vecino_dato in grafo.get(nodo, []):
            if not isinstance(vecino_dato, (tuple, list)):
                raise TypeError("cada arista debe ser una tupla (vecino, peso)")
            if len(vecino_dato) != 2:
                raise ValueError("cada arista debe tener dos elementos")
            vecino, peso = vecino_dato
            if not isinstance(vecino, str):
                raise TypeError("vecino debe ser un nodo válido")
            _validar_peso(peso)

            if vecino not in distancias:
                distancias[vecino] = inf
                predecesores[vecino] = None

            nueva_distancia = distancias[nodo] + peso
            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                predecesores[vecino] = nodo
                if peso == 0:
                    cola.appendleft(vecino)
                else:
                    cola.append(vecino)

    return distancias, predecesores


def camino_cero_uno(grafo, origen, destino):
    if origen not in grafo:
        raise KeyError(f"origen {origen} no encontrado")
    if destino not in grafo and destino != origen:
        # si no existe en el grafo, se permite solo si es descubierto como vecino implícito
        distancias, predecesores = cero_uno_bfs(grafo, origen)
        if destino not in distancias:
            raise KeyError(f"destino {destino} no encontrado")
        if distancias[destino] == inf:
            raise KeyError(f"destino {destino} no encontrado")
        return distancias[destino], reconstruir_camino(predecesores, origen, destino)

    if destino == origen:
        return 0, [origen]

    distancias, predecesores = cero_uno_bfs(grafo, origen)
    if distancias.get(destino, inf) == inf:
        return inf, []
    return distancias[destino], reconstruir_camino(predecesores, origen, destino)