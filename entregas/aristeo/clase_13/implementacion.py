class NodoAVL:
    def __init__(self, valor: int):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None
        self.altura = 1  # Convención: hoja tiene altura 1

class ArbolAVL:
    def __init__(self):
        self.raiz = None

    def _get_altura(self, nodo: NodoAVL) -> int:
        return nodo.altura if nodo else 0

    def _get_balance(self, nodo: NodoAVL) -> int:
        if not nodo:
            return 0
        return self._get_altura(nodo.izquierdo) - self._get_altura(nodo.derecho)

    def _rotar_izquierda(self, x: NodoAVL) -> NodoAVL:
        y = x.derecho
        T2 = y.izquierdo

        # Rotación
        y.izquierdo = x
        x.derecho = T2

        # Actualizar alturas (el orden importa: primero el de abajo, luego el de arriba)
        x.altura = 1 + max(self._get_altura(x.izquierdo), self._get_altura(x.derecho))
        y.altura = 1 + max(self._get_altura(y.izquierdo), self._get_altura(y.derecho))

        return y

    def _rotar_derecha(self, y: NodoAVL) -> NodoAVL:
        x = y.izquierdo
        T2 = x.derecho

        # Rotación
        x.derecho = y
        y.izquierdo = T2

        # Actualizar alturas
        y.altura = 1 + max(self._get_altura(y.izquierdo), self._get_altura(y.derecho))
        x.altura = 1 + max(self._get_altura(x.izquierdo), self._get_altura(x.derecho))

        return x

    def insertar(self, valor: int) -> None:
        self.raiz = self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo: NodoAVL, valor: int) -> NodoAVL:
        # 1. Inserción BST estándar
        if not nodo:
            return NodoAVL(valor)
        
        if valor < nodo.valor:
            nodo.izquierdo = self._insertar_recursivo(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            nodo.derecho = self._insertar_recursivo(nodo.derecho, valor)
        else:
            return nodo # No se permiten duplicados o se ignoran

        # 2. Actualizar altura del nodo ancestro
        nodo.altura = 1 + max(self._get_altura(nodo.izquierdo), self._get_altura(nodo.derecho))

        # 3. Obtener factor de balance
        balance = self._get_balance(nodo)

        # 4. Casos de Desbalance
        # Caso LL (Izquierda Izquierda)
        if balance > 1 and valor < nodo.izquierdo.valor:
            return self._rotar_derecha(nodo)

        # Caso RR (Derecha Derecha)
        if balance < -1 and valor > nodo.derecho.valor:
            return self._rotar_izquierda(nodo)

        # Caso LR (Izquierda Derecha)
        if balance > 1 and valor > nodo.izquierdo.valor:
            nodo.izquierdo = self._rotar_izquierda(nodo.izquierdo)
            return self._rotar_derecha(nodo)

        # Caso RL (Derecha Izquierda)
        if balance < -1 and valor < nodo.derecho.valor:
            nodo.derecho = self._rotar_derecha(nodo.derecho)
            return self._rotar_izquierda(nodo)

        return nodo

    def contiene(self, valor: int) -> bool:
        actual = self.raiz
        while actual:
            if valor == actual.valor:
                return True
            elif valor < actual.valor:
                actual = actual.izquierdo
            else:
                actual = actual.derecho
        return False

    def altura(self) -> int:
        return self._get_altura(self.raiz)

    def inorden(self) -> list[int]:
        resultado = []
        self._inorden_recursivo(self.raiz, resultado)
        return resultado

    def _inorden_recursivo(self, nodo: NodoAVL, lista: list[int]):
        if nodo:
            self._inorden_recursivo(nodo.izquierdo, lista)
            lista.append(nodo.valor)
            self._inorden_recursivo(nodo.derecho, lista)

    def esta_balanceado(self) -> bool:
        return self._verificar_balance(self.raiz)

    def _verificar_balance(self, nodo: NodoAVL) -> bool:
        if not nodo:
            return True
        balance = self._get_balance(nodo)
        if abs(balance) > 1:
            return False
        return self._verificar_balance(nodo.izquierdo) and self._verificar_balance(nodo.derecho)