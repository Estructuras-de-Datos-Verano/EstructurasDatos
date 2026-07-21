def _preorden_recursivo(self, nodo_actual: Nodo | None, resultado: list[int]) -> None:
        if nodo_actual is not None:
            resultado.append(nodo_actual.valor)
            self._preorden_recursivo(nodo_actual.izquierdo, resultado)
            self._preorden_recursivo(nodo_actual.derecho, resultado)

def postorden(self) -> list[int]:
        resultado: list[int] = []
        self._postorden_recursivo(self.raiz, resultado)
        return resultado

def _postorden_recursivo(self, nodo_actual: Nodo | None, resultado: list[int]) -> None:
        if nodo_actual is not None:
            self._postorden_recursivo(nodo_actual.izquierdo, resultado)
            self._postorden_recursivo(nodo_actual.derecho, resultado)
            resultado.append(nodo_actual.valor)