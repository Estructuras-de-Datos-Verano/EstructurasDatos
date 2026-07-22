"""Código base documentado para la Clase 14: min-heaps.

Este archivo define el contrato de la práctica, pero no contiene la solución.
La implementación evaluable debe vivir en
``entregas/clase_14/nombre/implementacion.py``.
"""

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

        self.datos = []
        if valores is not None:
            self.construir_heap(valores)


    def esta_vacio(self) -> bool:
        """Devuelve ``True`` cuando el heap no almacena elementos."""

        if self.datos:
            return False
        else:
            return True

    def tamano(self) -> int:
        """Devuelve la cantidad de elementos almacenados."""

        return len(self.datos)

    def minimo(self) -> int:
        """Consulta la raíz sin retirarla.

        Raises
        ------
        IndexError
            Si el heap está vacío.
        """

        return self.datos[0]

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
        self.datos.append(valor)
        z = len(self.datos) - 1
        self._subir(z)
        

    def extraer_min(self) -> int:
        """Retira y devuelve el mínimo usando sift-down.

        Raises
        ------
        IndexError
            Si el heap está vacío.
        """

        if self.esta_vacio():
            raise IndexError("El heap está vacío")
        a = self.datos[0]
        if self.tamano() == 1:
            self.datos = []
            return a
        else: 
            b = self.datos[-1]
            x = self.datos[1:-1]
            self.datos = [b] + x
            self._bajar(0)
            return a

    def construir_heap(self, valores: Iterable[int]) -> None:
        """Reemplaza el contenido por un heap construido con ``valores``."""
        heap = HeapMin()
        for valor in valores:
            heap.insertar(valor)
            
        self.datos = heap.datos 

    def _subir(self, indice: int) -> None:
        """Desplaza hacia arriba el nodo ubicado en ``indice``."""
        if indice == 0:
            return
        while indice > 0:
            indice_padre = self._indice_padre(indice) # Guardamos el índice del padre
            
            if self.datos[indice] < self.datos[indice_padre]:
                a = self.datos[indice]
                b = self.datos[indice_padre]
                
                # Intercambiamos en self.datos
                self.datos[indice] = b
                self.datos[indice_padre] = a  # <--- Corregido aquí
                
                # ¡Importante! Tienes que actualizar 'indice' para que el while no sea infinito
                indice = indice_padre 
            else:
                break # Si ya no es menor que el padre, terminamos

    def _bajar(self, indice: int) -> None:
        """Desplaza hacia abajo el nodo ubicado en ``indice``."""
        tamano = len(self.datos)
        
        while True:
            indice_menor = indice
            izq = self._indice_izquierdo(indice)
            der = self._indice_derecho(indice)
            
            # Verificamos si el hijo izquierdo existe y es menor que el actual
            if izq < tamano and self.datos[izq] < self.datos[indice_menor]:
                indice_menor = izq
                
            # Verificamos si el hijo derecho existe y es menor que el actual
            if der < tamano and self.datos[der] < self.datos[indice_menor]:
                indice_menor = der
                
            # Si el menor ya no es el nodo actual, intercambiamos y repetimos
            if indice_menor != indice:
                a = self.datos[indice]
                b = self.datos[indice_menor]
                self.datos[indice] = b
                self.datos[indice_menor] = a
                
                indice = indice_menor
            else:
                break # Si el nodo ya es menor que sus hijos, terminamos

    def _indice_padre(self, indice: int) -> int:
        """Calcula el índice del padre; la raíz no tiene padre."""
        if indice == 0:
            raise IndexError("La raíz no tiene padre")
        return (indice - 1) // 2

    def _indice_izquierdo(self, indice: int) -> int:
        """Calcula el índice del hijo izquierdo."""

        return 2 * indice + 1

    def _indice_derecho(self, indice: int) -> int:
        """Calcula el índice del hijo derecho."""

        return 2 * indice + 2

    def cumple_propiedad_heap(self) -> bool: 
        """Comprueba que todo padre sea menor o igual que sus hijos."""

        for i in range(self.tamano()):
            izq = self._indice_izquierdo(i)
            der = self._indice_derecho(i)
            
            # Verificamos que el hijo izquierdo exista y si rompe la propiedad
            if izq < self.tamano() and self.datos[i] > self.datos[izq]:
                return False
                
            # Verificamos que el hijo derecho exista y si rompe la propiedad
            if der < self.tamano() and self.datos[i] > self.datos[der]:
                return False
                
        # Si revisó todos los nodos y no hubo errores, sí es un Min-Heap
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
    if not isinstance(piedras, list):
        raise TypeError("Piedras debe ser una lista de enteros")
    for piedra in piedras:
        if piedra < 0:
            raise ValueError("Los pesos de las piedras deben ser positivos")
    pesos = []
    for piedra in piedras:
        pesos.append(-piedra)
    heap = HeapMin(pesos)
    while heap.tamano() > 1:  # <--- Agregamos paréntesis
        a = heap.extraer_min()
        b = heap.extraer_min()
        if not a == b:
            heap.insertar(a - b)  # <--- a es el más negativo, a-b mantiene el valor negativo correcto
            
    if heap.esta_vacio():
        return 0
    else:
        return -heap.minimo() # <--- Regresamos el peso a positivo