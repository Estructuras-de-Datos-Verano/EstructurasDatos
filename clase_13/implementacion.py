from __future__ import annotations

class NodoAVL:
    def __init__(self, valor: int):
        self.valor = valor
        self.izquierdo: NodoAVL | None = None
        self.derecho: NodoAVL | None = None
        self.altura = 1

class ArbolAVL:
    def __init__(self):
        self.raiz: NodoAVL | None = None

    def _h(self, n: NodoAVL | None) -> int:
        return n.altura if n else 0

    def _b(self, n: NodoAVL | None) -> int:
        return self._h(n.izquierdo) - self._h(n.derecho) if n else 0
    # de esta forma vemos las cosas necesarias que ocupamos para poder hacer las rotaciones y balancear el arbol.
    def _rotar_D(self, y: NodoAVL) -> NodoAVL:
        x = y.izquierdo
        y.izquierdo = x.derecho
        x.derecho = y
        y.altura = 1 + max(self._h(y.izquierdo), self._h(y.derecho))
        x.altura = 1 + max(self._h(x.izquierdo), self._h(x.derecho))
        return x

    def _rotar_I(self, x: NodoAVL) -> NodoAVL:
        y = x.derecho
        x.derecho = y.izquierdo
        y.izquierdo = x
        x.altura = 1 + max(self._h(x.izquierdo), self._h(x.derecho))
        y.altura = 1 + max(self._h(y.izquierdo), self._h(y.derecho))
        return y

    def insertar(self, valor: int) -> None:
        self.raiz = self._ins(self.raiz, valor)

    def _ins(self, n: NodoAVL | None, v: int) -> NodoAVL:
        if not n: return NodoAVL(v)
        if v < n.valor:   n.izquierdo = self._ins(n.izquierdo, v)
        elif v > n.valor: n.derecho = self._ins(n.derecho, v)
        else: return n

        n.altura = 1 + max(self._h(n.izquierdo), self._h(n.derecho))
        bal = self._b(n)

        if bal > 1 and v < n.izquierdo.valor:  return self._rotar_D(n)
        if bal < -1 and v > n.derecho.valor:  return self._rotar_I(n)
        if bal > 1 and v > n.izquierdo.valor:
            n.izquierdo = self._rotar_I(n.izquierdo)
            return self._rotar_D(n)
        if bal < -1 and v < n.derecho.valor:
            n.derecho = self._rotar_D(n.derecho)
            return self._rotar_I(n)
        return n

    def contiene(self, valor: int) -> bool:
        act = self.raiz
        while act:
            if valor == act.valor: return True
            act = act.izquierdo if valor < act.valor else act.derecho
        return False

    def altura(self) -> int:
        return self._h(self.raiz)

    def inorden(self) -> list[int]:
        res: list[int] = []
        self._ino(self.raiz, res)
        return res

    def _ino(self, n: NodoAVL | None, res: list[int]):
        if n:
            self._ino(n.izquierdo, res)
            res.append(n.valor)
            self._ino(n.derecho, res)

    def esta_balanceado(self) -> bool:
        return self._ver(self.raiz)

    def _ver(self, n: NodoAVL | None) -> bool:
        if not n: return True
        return abs(self._b(n)) <= 1 and self._ver(n.izquierdo) and self._ver(n.derecho)