from __future__ import annotations

class Nodo:
    """Nodo de un árbol binario.

    Parámetros
    ----------
    valor : int
        Valor almacenado en el nodo.

    Atributos
    ---------
    valor : int
        Valor del nodo.
    izquierdo : Nodo | None
        Hijo izquierdo.
    derecho : Nodo | None
        Hijo derecho.

    Ejemplo
    -------
    >>> nodo = Nodo(10)
    >>> nodo.valor
    10
    >>> nodo.izquierdo is None
    True
    """

    def __init__(self, valor: int) -> None:
        """Crea un nodo con ``valor`` y sin hijos."""

        self.valor = valor
        self.izquierdo = None
        self.derecho = None


class ArbolBinarioBusqueda:
    """Árbol binario de búsqueda sin valores repetidos.

    Invariante
    ----------
    Para cada nodo:

    - todos los valores del subárbol izquierdo son menores que el valor del nodo;
    - todos los valores del subárbol derecho son mayores que el valor del nodo.

    Convención de altura
    --------------------
    - árbol vacío: altura 0;
    - árbol con solo raíz: altura 1.
    """

    def __init__(self) -> None:
        """Crea un árbol binario de búsqueda vacío."""
        #self._nodos = []
        self._forma = {}
        self._raiz = None
    def esta_vacio(self) -> bool:
        """Regresa True si el árbol no tiene nodos.

        Ejemplo
        -------
        >>> arbol = ArbolBinarioBusqueda()
        >>> arbol.esta_vacio()
        True
        """

        return len(set(self._forma)) == 0

    def insertar(self, valor: int) -> None:
        """Inserta un valor en el árbol.

        Si el árbol está vacío, el nuevo valor se convierte en la raíz.
        Si el valor ya existe, no debe insertarse de nuevo.

        Ejemplo
        -------
        >>> arbol = ArbolBinarioBusqueda()
        >>> arbol.insertar(8)
        >>> arbol.contiene(8)
        True
        """

        if len(self._forma) == 0:
            self._raiz = Nodo(valor)
            self._forma = {
                self._raiz : valor
            }
        elif valor in self._forma.values():
            print(f"Valor ya corresponde a un nodo en el árbol")
        nuevo_nodo = Nodo(valor)
        actual = self._raiz
        while True:
            if valor < actual.valor:
                if actual.izquierdo is None:
                    actual.izquierdo = nuevo_nodo
                    self._forma[nuevo_nodo] = valor
                    break
                else:
                    actual = actual.izquierdo
            elif valor > actual.valor:
                if actual.derecho is None:
                    actual.derecho = nuevo_nodo
                    self._forma[nuevo_nodo] = valor
                    break
                else:
                    actual = actual.derecho
            else:
                print(f"Valor ya corresponde a un nodo en el árbol")
                break


    def contiene(self, valor: int) -> bool:
        """Indica si el valor está en el árbol.

        Ejemplo
        -------
        >>> arbol = ArbolBinarioBusqueda()
        >>> arbol.insertar(8)
        >>> arbol.contiene(8)
        True
        >>> arbol.contiene(5)
        False
        """
        return valor in set(self._forma.values())

        

    def altura(self) -> int:
        """Regresa la altura del árbol.

        Convención de esta clase:

        - árbol vacío: altura 0;
        - árbol con solo raíz: altura 1.

        Ejemplo
        -------
        >>> arbol = ArbolBinarioBusqueda()
        >>> arbol.altura()
        0
        >>> arbol.insertar(8)
        >>> arbol.altura()
        1
        """
        if self._raiz is None:
            return 0
    
        def altura_nodo(nodo):
            if nodo is None:
                return 0
            altura_izquierda = altura_nodo(nodo.izquierdo)
            altura_derecha = altura_nodo(nodo.derecho)
            return 1 + max(altura_izquierda, altura_derecha)

        return altura_nodo(self._raiz)
    def inorden(self):
        """"
        Lo mismo, pero simplificado
        """
        lista = []
        def viajar(nodo):
            if nodo is None:
                return
            viajar(nodo.izquierdo)
            lista.append(nodo.valor)
            viajar(nodo.derecho)
        viajar(self._raiz)
        return lista

    def preorden(self) -> list[int]:
        """Regresa los valores del árbol en recorrido preorden.

        Preorden procesa:

        raíz -> subárbol izquierdo -> subárbol derecho.
        """

        lista = []
        def viajar_preorden(nodo):
            if nodo is None:
                return
            lista.append(nodo)
            viajar_preorden(nodo.izquierdo)
            viajar_preorden(nodo.derecho)
        viajar_preorden(self._raiz)
        return lista


    def postorden(self) -> list[int]:
        """Regresa los valores del árbol en recorrido postorden.

        Postorden procesa:

        subárbol izquierdo -> subárbol derecho -> raíz.
        """

        lista = []
        def viajar_postorden(nodo):
            if nodo is None:
                return None
            viajar_postorden(nodo.izquierdo)
            viajar_postorden(nodo.derecho)
            lista.append(nodo.valor)
        viajar_postorden(self._raiz)
        return lista


    def cantidad_nodos(self) -> int:
        """Regresa la cantidad de nodos almacenados en el árbol.

        Regresa
        -------
        int
            Número de valores distintos insertados.

        Ejemplo
        -------
        >>> arbol = ArbolBinarioBusqueda()
        >>> arbol.cantidad_nodos()
        0
        """

        recorrido = self.inorden()
        return len(set(recorrido)) #set por si acaso se repitieran valores, aunque no deberían porque en clase_11 se verificó con pytest que inorden() no repite valores

    def es_degenerado(self) -> bool:
        """Indica si el árbol está degenerado.

        En esta práctica diremos que un árbol no vacío está degenerado si cada
        nodo tiene a lo más un hijo. Con esta forma, el árbol se parece a una
        lista enlazada y su altura coincide con su cantidad de nodos.

        Regresa
        -------
        bool
            True si el árbol está degenerado; False en otro caso.
        """
        if self._raiz is None:
            return False
        def viajar(nodo):
            if nodo is None:
                return True
            if nodo.izquierdo and nodo.derecho:
                return False
            return viajar(nodo.izquierdo) and viajar(nodo.derecho)
        return viajar(self._raiz)

    def comparaciones_busqueda(self, valor: int) -> int:
        """Cuenta cuántas comparaciones realiza la búsqueda de ``valor``.

        La función debe contar cada nodo visitado durante la búsqueda.

        Parámetros
        ----------
        valor : int
            Valor entero a buscar.

        Regresa
        -------
        int
            Número de comparaciones realizadas. En un árbol vacío regresa 0.

        Ejemplo
        -------
        >>> arbol = ArbolBinarioBusqueda()
        >>> arbol.comparaciones_busqueda(5)
        0
        >>> arbol.insertar(8)
        >>> arbol.comparaciones_busqueda(8)
        1
        """
        count = 0
        actual = self._raiz
        if self._forma == {}:
            return 0
        while actual is not None:
            count += 1
            if valor == actual.valor:
                break
            elif valor > actual.valor:
                actual = actual.derecho
                continue
            elif valor < actual.valor:
                actual = actual.izquierdo
                continue
            elif actual.izquierdo is None and actual.derecho is None: # por si acaso pero el while lo ataca
                # Originalmente usaba while self._forma pero eso da un error cuando el nodo es None, así que lo cambié a while actual is not None
                break
        return count
    def nodos_accedidos(self, valor: int) -> set:
        nodos = []
        actual = self._raiz
        if self._forma == {}:
            return []
        while actual is not None:
            nodos.append(actual)
            if valor == actual.valor:
                break
            if valor >= actual.valor:
                actual = actual.derecho
                continue
            elif valor < actual.valor:
                actual = actual.izquierdo
                continue
            elif actual.izquierdo is None and actual.derecho is None: # por si acaso pero el while lo ataca
                # Originalmente usaba while self._forma pero eso da un error cuando el nodo es None, así que lo cambié a while actual is not None
                break
        return set(nodos)
        
