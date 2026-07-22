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

        self.valores = list(valores) if valores is not None else []
        #Le permitimos iniciar una lista vacía si no recibe nada.
        #En otro caso, toma lo que reciba.

        if valores is not None:
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
            raise IndexError("El heap está vacío.")
        
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
        # Lo agregamos
        self.valores.append(valor)

        self._subir(len(self.valores) - 1)

        

    def extraer_min(self) -> int:
        """Retira y devuelve el mínimo usando sift-down.

        Raises
        ------
        IndexError
            Si el heap está vacío.
        """
        if self.esta_vacio():
            raise IndexError("No debe estar vacío.")

        # La raíz
        minimo = self.valores[0]
        ultimo_valor = self.valores.pop()

        if not self.esta_vacio():
            self.valores[0] = ultimo_valor
            self._bajar(0)

        return minimo


    def construir_heap(self, valores: Iterable[int]) -> None:
        """Reemplaza el contenido por un heap construido con ``valores``."""

        self.valores = list(valores)

        """
        Mucho ojo con esta parte. Sugerencia de Gemini. Pedir explicaciones.
        """
        for i in range ((len(self.valores) - 2) // 2, -1, -1):
            self._bajar(i)

    def _subir(self, indice: int) -> None:
        """Desplaza hacia arriba el nodo ubicado en ``indice``."""

        while indice > 0:
            padre = (indice -1) // 2
            # Si el elemento es menor que su padre, hay que moverle.
            if self.valores[indice] < self.valores[padre]:
                self.valores[indice], self.valores[padre] = self.valores[padre], self.valores[indice]
                #Los cambia de lugar. 

                #Actualiza para seguir moviéndose hacia arriba.
                indice = padre

            else:
                #Si ya es menor, no le mueve
                break

    def _bajar(self, indice: int) -> None:
        """Desplaza hacia abajo el nodo ubicado en ``indice``."""

        n = len(self.valores)
        #Mientras el nodo actual tenga al menos un hijo izquierdo...
        while 2 * indice + 1 < n:
            izq = 2 * indice + 1
            der = 2 *indice + 2
            menor = izq

            # Si el hijo derecho existe y es menor que el izquierdo, actualizamos el menor.
            if der < n and self.valores[der] < self.valores[izq]:
                menor = der

            #Si el nodo actual es menor, no le mueve.
            if self.valores[indice] <= self.valores[menor]:
                break

            self.valores[indice], self.valores[menor] = self.valores[menor], self.valores[indice]

            indice = menor

        

    def _indice_padre(self, indice: int) -> int:
        """Calcula el índice del padre; la raíz no tiene padre."""

        #La raíz no tiene padre.
        if indice == 0:
            raise IndexError("La raíz no tiene padre.")
        return (indice-1) // 2

    def _indice_izquierdo(self, indice: int) -> int:
        """Calcula el índice del hijo izquierdo."""

        return 2 * indice +1


    def _indice_derecho(self, indice: int) -> int:
        """Calcula el índice del hijo derecho."""

        return 2 * indice + 2

    def cumple_propiedad_heap(self) -> bool:
        """Comprueba que todo padre sea menor o igual que sus hijos."""

        n = self.tamano()

        for i in range ((n-2) // 2 + 1):
            izq = self._indice_izquierdo(i)
            der = self._indice_derecho(i)

            if izq < n and self.valores[i] > self.valores[izq]:
                return False
            
            if der < n and self.valores[i] > self.valores[der]:
                return False
            
        return True
