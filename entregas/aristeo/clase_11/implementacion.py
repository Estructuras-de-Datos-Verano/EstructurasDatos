class Nodo:
    def __init__(self, valor: int):
        self.valor = valor
        self.izquierdo: "Nodo | None" = None
        self.derecho: "Nodo | None" = None


class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz: "Nodo | None" = None

    def esta_vacio(self) -> bool:
        return self.raiz is None

    def insertar(self, valor: int) -> None:
        if self.raiz is None:
            self.raiz = Nodo(valor)
            return
        self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo: Nodo, valor: int) -> None:
        if valor < nodo.valor:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            if nodo.derecho is None:
                nodo.derecho = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.derecho, valor)
        # Si valor == nodo.valor, no se inserta (sin duplicados)

    def contiene(self, valor: int) -> bool:
        return self._contiene_recursivo(self.raiz, valor)

    def _contiene_recursivo(self, nodo: "Nodo | None", valor: int) -> bool:
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

    def _altura_recursiva(self, nodo: "Nodo | None") -> int:
        # Convención de la clase: árbol vacío -> altura 0,
        # árbol con solo raíz -> altura 1.
        if nodo is None:
            return 0
        altura_izq = self._altura_recursiva(nodo.izquierdo)
        altura_der = self._altura_recursiva(nodo.derecho)
        return 1 + max(altura_izq, altura_der)

    def inorden(self) -> list[int]:
        resultado: list[int] = []
        self._inorden_recursivo(self.raiz, resultado)
        return resultado

    def _inorden_recursivo(self, nodo: "Nodo | None", resultado: list[int]) -> None:
        if nodo is not None:
            self._inorden_recursivo(nodo.izquierdo, resultado)
            resultado.append(nodo.valor)
            self._inorden_recursivo(nodo.derecho, resultado)

    def preorden(self) -> list[int]:
        resultado: list[int] = []
        self._preorden_recursivo(self.raiz, resultado)
        return resultado

    def _preorden_recursivo(self, nodo: "Nodo | None", resultado: list[int]) -> None:
        if nodo is not None:
            resultado.append(nodo.valor)
            self._preorden_recursivo(nodo.izquierdo, resultado)
            self._preorden_recursivo(nodo.derecho, resultado)

    def postorden(self) -> list[int]:
        resultado: list[int] = []
        self._postorden_recursivo(self.raiz, resultado)
        return resultado

    def _postorden_recursivo(self, nodo: "Nodo | None", resultado: list[int]) -> None:
        if nodo is not None:
            self._postorden_recursivo(nodo.izquierdo, resultado)
            self._postorden_recursivo(nodo.derecho, resultado)
            resultado.append(nodo.valor)
