"""Punto de partida de la Clase 17.

Completa las operaciones sin cambiar sus nombres ni sus firmas públicas. No
uses ``collections.deque`` ni un heap: la finalidad es construir las
estructuras auxiliares que necesitan BFS y 0-1 BFS.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from typing import Generic, TypeVar
from math import inf, isinf

T = TypeVar("T")


@dataclass(slots=True)
class NodoSimple(Generic[T]):
    """Nodo de una lista simplemente ligada."""

    valor: T
    siguiente: NodoSimple[T] | None = None


@dataclass(slots=True)
class NodoDoble(Generic[T]):
    """Nodo de una lista doblemente ligada."""

    valor: T
    anterior: NodoDoble[T] | None = None
    siguiente: NodoDoble[T] | None = None


class ColaLigada(Generic[T]):
    """Cola FIFO implementada con nodos simples."""

    def __init__(self) -> None:
        self._frente: NodoSimple[T] | None = None
        self._final: NodoSimple[T] | None = None
        self._tamano = 0

    def encolar(self, valor: T) -> None:
        """Agrega un valor al final en O(1)."""
        nuevo = NodoSimple(valor)
        if self._final is None:
            self._frente = self._final = nuevo
        else:
            self._final.siguiente = nuevo
            self._final = nuevo
        self._tamano += 1

    def desencolar(self) -> T:
        """Retira y devuelve el frente; lanza IndexError si está vacía."""
        if self._frente is None:
            raise IndexError("Desencolar desde una cola vacía")
        
        valor = self._frente.valor
        self._frente = self._frente.siguiente
        
        if self._frente is None:
            self._final = None
            
        self._tamano -= 1
        return valor

    def primero(self) -> T:
        """Consulta el frente sin retirarlo; lanza IndexError si está vacía."""
        if self._frente is None:
            raise IndexError("Consulta desde una cola vacía")
        return self._frente.valor

    def esta_vacia(self) -> bool:
        """Indica si no hay elementos."""
        return self._tamano == 0

    def __len__(self) -> int:
        return self._tamano


class DequeLigada(Generic[T]):
    """Deque implementada con nodos dobles."""

    def __init__(self) -> None:
        self._inicio: NodoDoble[T] | None = None
        self._final: NodoDoble[T] | None = None
        self._tamano = 0

    def agregar_inicio(self, valor: T) -> None:
        """Agrega un valor al inicio en O(1)."""
        nuevo = NodoDoble(valor)
        if self._inicio is None:
            self._inicio = self._final = nuevo
        else:
            nuevo.siguiente = self._inicio
            self._inicio.anterior = nuevo
            self._inicio = nuevo
        self._tamano += 1

    def agregar_final(self, valor: T) -> None:
        """Agrega un valor al final en O(1)."""
        nuevo = NodoDoble(valor)
        if self._final is None:
            self._inicio = self._final = nuevo
        else:
            nuevo.anterior = self._final
            self._final.siguiente = nuevo
            self._final = nuevo
        self._tamano += 1

    def quitar_inicio(self) -> T:
        """Retira y devuelve el inicio; lanza IndexError si está vacía."""
        if self._inicio is None:
            raise IndexError("Quitar inicio desde una deque vacía")
            
        viejo_inicio = self._inicio
        valor = viejo_inicio.valor
        self._inicio = viejo_inicio.siguiente
        
        if self._inicio is None:
            self._final = None
        else:
            self._inicio.anterior = None
            
        # ¡Esta es la línea clave que faltaba! Desconectar el nodo retirado.
        viejo_inicio.siguiente = None 
            
        self._tamano -= 1
        return valor

    def quitar_final(self) -> T:
        """Retira y devuelve el final; lanza IndexError si está vacía."""
        if self._final is None:
            raise IndexError("Quitar final desde una deque vacía")
            
        viejo_final = self._final
        valor = viejo_final.valor
        self._final = viejo_final.anterior
        
        if self._final is None:
            self._inicio = None
        else:
            self._final.siguiente = None
            
        # ¡Esta es la línea clave que faltaba! Desconectar el nodo retirado.
        viejo_final.anterior = None
            
        self._tamano -= 1
        return valor

    def primero(self) -> T:
        """Consulta el inicio sin retirarlo."""
        if self._inicio is None:
            raise IndexError("Consulta desde una deque vacía")
        return self._inicio.valor

    def ultimo(self) -> T:
        """Consulta el final sin retirarlo."""
        if self._final is None:
            raise IndexError("Consulta desde una deque vacía")
        return self._final.valor

    def esta_vacia(self) -> bool:
        """Indica si no hay elementos."""
        return self._tamano == 0

    def __len__(self) -> int:
        return self._tamano


def bfs_predecesores(
    grafo: Mapping[str, Sequence[str]], origen: str
) -> dict[str, str | None]:
    """Devuelve la tabla de predecesores de un BFS desde ``origen``."""
    if origen not in grafo:
        raise KeyError(f"El origen {origen} no se encuentra.")

    predecesores: dict[str, str | None] = {nodo: None for nodo in grafo}
    
    # Manejar vecino implícito: si origen es el único nodo y no está en keys, ya falló.
    # Si hay vecinos que no son llaves, se agregan a predecesores al descubrirlos.
    visitados = {origen}
    
    cola: ColaLigada[str] = ColaLigada()
    cola.encolar(origen)

    while not cola.esta_vacia():
        actual = cola.desencolar()
        
        for vecino in grafo.get(actual, []):
            if vecino not in predecesores:
                predecesores[vecino] = None
            
            if vecino not in visitados:
                visitados.add(vecino)
                predecesores[vecino] = actual
                cola.encolar(vecino)

    return predecesores


def reconstruir_camino(
    predecesores: Mapping[str, str | None], origen: str, destino: str
) -> list[str]:
    """Reconstruye un camino desde una tabla de predecesores."""
    if origen not in predecesores or destino not in predecesores:
        return []

    if origen == destino:
        return [origen]

    camino = []
    actual: str | None = destino
    visitados: set[str] = set()

    while actual is not None:
        if actual in visitados:
            raise ValueError("Se detectó un ciclo en la reconstrucción.")
            
        visitados.add(actual)
        camino.append(actual)

        if actual == origen:
            camino.reverse()
            return camino

        actual = predecesores.get(actual)

    return []


def bfs_camino(
    grafo: Mapping[str, Sequence[str]], origen: str, destino: str
) -> list[str]:
    """Devuelve un camino mínimo por número de aristas, o una lista vacía."""
    if origen not in grafo:
        raise KeyError(f"El origen {origen} no se encuentra.")
    if destino not in grafo and destino != origen:
        # Permite destino implicito si es alcanzable, pero falla si de plano no está
        # Revisa si está como valor en alguna lista
        implicito = any(destino in vecinos for vecinos in grafo.values())
        if not implicito:
            raise KeyError(f"El destino {destino} no se encuentra.")
        
    predecesores = bfs_predecesores(grafo, origen)
    return reconstruir_camino(predecesores, origen, destino)


def cero_uno_bfs(
    grafo: Mapping[str, Sequence[tuple[str, int]]], origen: str
) -> tuple[dict[str, float], dict[str, str | None]]:
    """Calcula distancias para pesos enteros 0/1 usando ``DequeLigada``."""
    if origen not in grafo:
        raise KeyError("Falta el origen en el grafo.")

    distancias: dict[str, float] = {nodo: inf for nodo in grafo}
    predecesores: dict[str, str | None] = {nodo: None for nodo in grafo}
    
    distancias[origen] = 0.0
    deque: DequeLigada[str] = DequeLigada()
    deque.agregar_inicio(origen)

    while not deque.esta_vacia():
        actual = deque.quitar_inicio()

        for arista in grafo.get(actual, []):
            if not isinstance(arista, (tuple, list)) or len(arista) != 2:
                raise ValueError("La arista debe tener exactamente dos elementos.")
                
            vecino, peso = arista
            
            if not isinstance(vecino, str):
                raise TypeError("El vecino debe ser texto.")
            
            # Validación estricta requerida por la prueba parametrizada
            if type(peso) is not int:
                raise TypeError("El peso debe ser un entero 0 o 1.")
            if peso not in (0, 1):
                raise ValueError("El peso debe ser 0 o 1.")

            # Vecinos implícitos
            if vecino not in distancias:
                distancias[vecino] = inf
                predecesores[vecino] = None

            candidato = distancias[actual] + float(peso)

            if candidato < distancias[vecino]:
                distancias[vecino] = candidato
                predecesores[vecino] = actual
                
                if peso == 0:
                    deque.agregar_inicio(vecino)
                else:
                    deque.agregar_final(vecino)

    return distancias, predecesores


def camino_cero_uno(
    grafo: Mapping[str, Sequence[tuple[str, int]]], origen: str, destino: str
) -> tuple[float, list[str]]:
    """Devuelve el costo y un camino mínimo 0-1; ``(inf, [])`` si no existe."""
    if origen not in grafo:
        raise KeyError("Falta el origen.")
        
    # Verificar si el destino existe de forma explícita o implícita
    destino_existe = destino in grafo or any(
        destino == v for aristas in grafo.values() for v, _ in aristas if len(aristas) > 0 and isinstance(aristas[0], tuple)
    )
    
    if not destino_existe and origen != destino:
         raise KeyError("Falta el destino.")

    distancias, predecesores = cero_uno_bfs(grafo, origen)
    
    costo_final = distancias.get(destino, inf)
    if isinf(costo_final):
        return inf, []

    camino = reconstruir_camino(predecesores, origen, destino)
    return costo_final, camino


__all__ = [
    "NodoSimple",
    "NodoDoble",
    "ColaLigada",
    "DequeLigada",
    "bfs_predecesores",
    "reconstruir_camino",
    "bfs_camino",
    "cero_uno_bfs",
    "camino_cero_uno",
]