class Nodo:
    def __init__(self, valor: int):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def esta_vacio(self) -> bool:
        return self.raiz is None

    def insertar(self, valor: int) -> None:
        if self.raiz is None:
            self.raiz = Nodo(valor)
            return
        self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo: Nodo, valor: int):
        if valor == nodo.valor:
            return  # Según las reglas de tu clase, no insertamos duplicados
        elif valor < nodo.valor:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.izquierdo, valor)
        else:
            if nodo.derecho is None:
                nodo.derecho = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.derecho, valor)

    def contiene(self, valor: int) -> bool:
        return self._contiene_recursivo(self.raiz, valor)

    def _contiene_recursivo(self, nodo: Nodo, valor: int) -> bool:
        if nodo is None:
            return False
        if valor == nodo.valor:
            return True
        elif valor < nodo.valor:
            return self._contiene_recursivo(nodo.izquierdo, valor)
        else:
            return self._contiene_recursivo(nodo.derecho, valor)

    def altura(self) -> int:
        return self._altura_recursiva(self.raiz)

    def _altura_recursiva(self, nodo: Nodo) -> int:
        if nodo is None:
            return 0
        return 1 + max(self._altura_recursiva(nodo.izquierdo), self._altura_recursiva(nodo.derecho))

    def inorden(self) -> list[int]:
        resultado = []
        self._inorden_recursivo(self.raiz, resultado)
        return resultado

    def _inorden_recursivo(self, nodo: Nodo, resultado: list):
        if nodo:
            self._inorden_recursivo(nodo.izquierdo, resultado)
            resultado.append(nodo.valor)
            self._inorden_recursivo(nodo.derecho, resultado)

    def preorden(self) -> list[int]:
        resultado = []
        self._preorden_recursivo(self.raiz, resultado)
        return resultado

    def _preorden_recursivo(self, nodo: Nodo, resultado: list):
        if nodo:
            resultado.append(nodo.valor)
            self._preorden_recursivo(nodo.izquierdo, resultado)
            self._preorden_recursivo(nodo.derecho, resultado)

    def postorden(self) -> list[int]:
        resultado = []
        self._postorden_recursivo(self.raiz, resultado)
        return resultado

    def _postorden_recursivo(self, nodo: Nodo, resultado: list):
        if nodo:
            self._postorden_recursivo(nodo.izquierdo, resultado)
            self._postorden_recursivo(nodo.derecho, resultado)
            resultado.append(nodo.valor)