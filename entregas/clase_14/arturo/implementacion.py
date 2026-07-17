from __future__ import annotations

from collections.abc import Iterable


class HeapMin:
    """Min-heap de enteros representado con un arreglo indexado desde cero.

    Convención
    ----------
    Para un índice ``i``:

    - ``padre(i) = (i - 1) // 2``;
    - ``izquierdo(i) = 2 * i + 1``;
    - ``derecho(i) = 2 * i + 2``.

    Notes
    -----
    Completa esta interfaz en tu carpeta de entrega. No modifiques este archivo
    para entregar la práctica.
    """

    def __init__(self, valores: Iterable[int] | None = None) -> None:
        """Crea un heap vacío o lo construye a partir de ``valores``.

        Parameters
        ----------
        valores : Iterable[int] | None
            Valores iniciales opcionales.
        """
        if valores is None:
            self.valores = []
        else:
            self.valores = list(valores)

            for i in self.valores:
                if not isinstance(i, int):
                    raise ValueError("Los elementos deben ser enteros")
        self.construir_heap(self.valores)
    

    def esta_vacio(self) -> bool:
        """Devuelve ``True`` cuando el heap no almacena elementos."""

        return len(self.valores) == 0


    def tamano(self) -> int:
        """Devuelve la cantidad de elementos almacenados."""

        return len(self.valores)

    def minimo(self) -> int:
        """Consulta la raíz sin retirarla.

        Raises
        ------
        IndexError
            Si el heap está vacío.
        """

        if self.esta_vacio():
            raise IndexError("Valores esta vacio")
        else:
            return self.valores[0]

    def insertar(self, valor: int) -> None:
        """Agrega ``valor`` y restaura la propiedad mediante sift-up.

        Parameters
        ----------
        valor : int
            Valor que se insertará.

        Examples
        --------
        >>> heap = HeapMin()
        >>> heap.insertar(5)
        >>> heap.insertar(2)
        >>> heap.minimo()
        2
        """

        
        if not isinstance(valor, int):
            raise ValueError("Valor debe ser un entero")
        
        self.valores.append(valor)
        ultimo_indice = len(self.valores) - 1
        self._subir(ultimo_indice)


    def extraer_min(self) -> int:
        """Retira y devuelve el mínimo usando sift-down.

        Raises
        ------
        IndexError
            Si el heap está vacío.
        """

        if self.esta_vacio():
            raise IndexError("El heap está vacío")
        
        minimo = self.valores[0]
    
        ultimo = self.valores.pop()
        
        if len(self.valores) > 0:
            self.valores[0] = ultimo
            self._bajar(0)
            
        return minimo

    def construir_heap(self, valores: Iterable[int]) -> None:
        """Reemplaza el contenido por un heap construido con ``valores``."""

        self.valores = list(valores)
        
        for val in self.valores:
            if not isinstance(val, int):
                raise ValueError("Los elementos deben ser enteros")
        
        n = len(self.valores)
        for i in range(n // 2 - 1, -1, -1):
            self._bajar(i)

    def _subir(self, indice: int) -> None:
        """Desplaza hacia arriba el nodo ubicado en ``indice``."""

        while indice > 0:
            padre = self._indice_padre(indice)
            
            if self.valores[indice] < self.valores[padre]:
                self.valores[indice], self.valores[padre] = self.valores[padre], self.valores[indice]
                
                
                indice = padre
            else:
                break

    def _bajar(self, indice: int) -> None:
        """Desplaza hacia abajo el nodo ubicado en ``indice``."""

        n = len(self.valores)
        
        while True:
            izquierdo = self._indice_izquierdo(indice)
            derecho = self._indice_derecho(indice)
            menor = indice

            if izquierdo < n and self.valores[izquierdo] < self.valores[menor]:
                menor = izquierdo
            
            if derecho < n and self.valores[derecho] < self.valores[menor]:
                menor = derecho
            
            if menor != indice:
                self.valores[indice], self.valores[menor] = self.valores[menor], self.valores[indice]
                indice = menor  
            else:
                
                break

    def _indice_padre(self, indice: int) -> int:
        """Calcula el índice del padre; la raíz no tiene padre."""
        return (indice - 1) // 2

    def _indice_izquierdo(self, indice: int) -> int:
        """Calcula el índice del hijo izquierdo."""
        return 2 * indice + 1

    def _indice_derecho(self, indice: int) -> int:
        """Calcula el índice del hijo derecho."""
        return 2 * indice + 2

    def cumple_propiedad_heap(self) -> bool:
        """Comprueba que todo padre sea menor o igual que sus hijos."""

        n = len(self.valores)
        
        for i in range(n // 2):
            izquierdo = self._indice_izquierdo(i)
            derecho = self._indice_derecho(i)
            
            
            if izquierdo < n and self.valores[i] > self.valores[izquierdo]:
                return False
            
            if derecho < n and self.valores[i] > self.valores[derecho]:
                return False
            
        return True


def ultima_piedra(piedras: list[int]) -> int:
    """Resuelve de forma guiada Last Stone Weight con una cola de prioridad.

    Parameters
    ----------
    piedras : list[int]
        Pesos positivos.

    Returns
    -------
    int
        Peso final, o 0 si no queda ninguna piedra.

    Notes
    -----
    Diseña primero el pseudocódigo en ``notebook.md``. Después completa esta
    función dentro de tu ``implementacion.py``.
    """

    heap_piedritas = HeapMin([-p for p in piedras])
    while len(heap_piedritas.valores) >= 2:
        mayor = -1 * heap_piedritas.extraer_min()
        segundo = -1 * heap_piedritas.extraer_min()
        if mayor != segundo:
            heap_piedritas.insertar(-1 * (mayor - segundo))

    if heap_piedritas.esta_vacio():
        return 0 
    return -1 * heap_piedritas.extraer_min()