from __future__ import annotations
from dataclasses import dataclass


@dataclass
class NodoAVL:
    """Nodo de un árbol AVL con almacenamiento explícito de altura."""
    valor: int
    izquierdo: NodoAVL | None = None
    derecho: NodoAVL | None = None
    altura: int = 1


class ArbolAVL:
    """Árbol Binario de Búsqueda auto-balanceado (Árbol AVL)."""

    def __init__(self) -> None:
        """Inicializa un árbol AVL vacío."""
        self.raiz: NodoAVL | None = None

    def altura(self) -> int:
        """Regresa la altura total del árbol."""
        return self._altura(self.raiz)

    def _altura(self, nodo: NodoAVL | None) -> int:
        """Regresa la altura de un nodo o 0 si es None."""
        return nodo.altura if nodo else 0

    def _actualizar_altura(self, nodo: NodoAVL) -> None:
        """Actualiza la altura de un nodo basándose en la altura de sus hijos."""
        nodo.altura = 1 + max(self._altura(nodo.izquierdo), self._altura(nodo.derecho))

    def _factor_balance(self, nodo: NodoAVL | None) -> int:
        """Calcula el factor de balance: altura izquierda - altura derecha."""
        return self._altura(nodo.izquierdo) - self._altura(nodo.derecho) if nodo else 0

    def contiene(self, valor: int) -> bool:
        """Busca un valor en el árbol de forma iterativa y eficiente."""
        actual = self.raiz
        while actual:
            if valor == actual.valor:
                return True
            elif valor < actual.valor:
                actual = actual.izquierdo
            else:
                actual = actual.derecho
        return False

    def inorden(self) -> list[int]:
        """Regresa el recorrido inorden de los elementos (debe resultar ordenado)."""
        resultado: list[int] = []
        self._inorden_aux(self.raiz, resultado)
        return resultado

    def _inorden_aux(self, nodo: NodoAVL | None, resultado: list[int]) -> None:
        if nodo:
            self._inorden_aux(nodo.izquierdo, resultado)
            resultado.append(nodo.valor)
            self._inorden_aux(nodo.derecho, resultado)

    def esta_balanceado(self) -> bool:
        """Verifica de forma recursiva que todo el árbol cumpla el invariante AVL."""
        return self._esta_balanceado_aux(self.raiz)

    def _esta_balanceado_aux(self, nodo: NodoAVL | None) -> bool:
        if nodo is None:
            return True
        balance = self._factor_balance(nodo)
        if abs(balance) > 1:
            return False
        return self._esta_balanceado_aux(nodo.izquierdo) and self._esta_balanceado_aux(nodo.derecho)

    def _rotar_derecha(self, nodo: NodoAVL) -> NodoAVL:
        """Aplica una rotación derecha local (Caso LL) y devuelve la nueva raíz local."""
        nueva_raiz = nodo.izquierdo
        subarbol_intermedio = nueva_raiz.derecho

        # Reestructuración de punteros
        nueva_raiz.derecho = nodo
        nodo.izquierdo = subarbol_intermedio

        # Es crucial actualizar primero el nodo que bajó, y luego el que subió
        self._actualizar_altura(nodo)
        self._actualizar_altura(nueva_raiz)

        return nueva_raiz

    def _rotar_izquierda(self, nodo: NodoAVL) -> NodoAVL:
        """Aplica una rotación izquierda local (Caso RR) y devuelve la nueva raíz local."""
        nueva_raiz = nodo.derecho
        subarbol_intermedio = nueva_raiz.izquierdo

        # Reestructuración de punteros
        nueva_raiz.izquierdo = nodo
        nodo.derecho = subarbol_intermedio

        # Es crucial actualizar primero el nodo que bajó, y luego el que subió
        self._actualizar_altura(nodo)
        self._actualizar_altura(nueva_raiz)

        return nueva_raiz

    def insertar(self, valor: int) -> None:
        """Inserta un valor único en el árbol manteniendo el balanceo."""
        self.raiz = self._insertar_aux(self.raiz, valor)

    def _insertar_aux(self, nodo: NodoAVL | None, valor: int) -> NodoAVL:
        # 1. Inserción estándar de un BST
        if nodo is None:
            return NodoAVL(valor)

        if valor < nodo.valor:
            nodo.izquierdo = self._insertar_aux(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            nodo.derecho = self._insertar_aux(nodo.derecho, valor)
        else:
            return nodo  # Si es duplicado se ignora según el contrato establecido

        # 2. Actualización de alturas antes de tomar decisiones de rotación
        self._actualizar_altura(nodo)

        # 3. Cálculo de balance del nodo actual
        balance = self._factor_balance(nodo)

        # 4. Identificación y resolución de los 4 casos de desbalance

        # Caso LL: Desbalance a la izquierda, inserción a la izquierda
        if balance > 1 and valor < nodo.izquierdo.valor:
            return self._rotar_derecha(nodo)

        # Caso RR: Desbalance a la derecha, inserción a la derecha
        if balance < -1 and valor > nodo.derecho.valor:
            return self._rotar_izquierda(nodo)

        # Caso LR: Desbalance a la izquierda, inserción a la derecha
        if balance > 1 and valor > nodo.izquierdo.valor:
            nodo.izquierdo = self._rotar_izquierda(nodo.izquierdo)
            return self._rotar_derecha(nodo)

        # Caso RL: Desbalance a la derecha, inserción a la izquierda
        if balance < -1 and valor < nodo.derecho.valor:
            nodo.derecho = self._rotar_derecha(nodo.derecho)
            return self._rotar_izquierda(nodo)

        return nodo