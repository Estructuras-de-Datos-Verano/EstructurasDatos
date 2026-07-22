from __future__ import annotations
from collections import deque
from collections.abc import Iterable

def validar_n(n: int) -> None:
    """Valida el tamaño del problema.

    CSES usa ``1 <= n <= 2 * 10**5``. Esta función separa la validación para
    que las pruebas puedan revisar casos de borde sin mezclar esa lógica con
    el algoritmo principal.
    """

    if not isinstance(n, int):
        raise TypeError("n debe ser un entero")
    if n < 1:
        raise ValueError("n debe ser al menos 1")


def orden_eliminacion(n: int) -> list[int]:
    """Regresa el orden de eliminación del problema Josephus I.

    TODO alumno:
    1. Valida ``n`` usando ``validar_n``.
    2. Modela a los niños vivos con una estructura de datos adecuada.
    3. Simula la regla: se salva uno, se elimina el siguiente.
    4. Regresa una lista con el orden de eliminación.

    Ejemplo:
    ``orden_eliminacion(7)`` debe regresar ``[2, 4, 6, 1, 5, 3, 7]``.
    """

    validar_n(n)
    vivos = deque(range(1, n + 1))
    eliminados = []
    while vivos: 
        if len(vivos) == 1:
            # Si solo queda uno, se saca directamente
            ultimo = vivos.popleft()
            eliminados.append(ultimo)
        else:
            # El primero se salva: rota del frente hacia el final
            nino_salvado = vivos.popleft()
            vivos.append(nino_salvado)
            
            # El segundo se elimina: se saca del frente y se guarda
            nino_eliminado = vivos.popleft()
            eliminados.append(nino_eliminado)
            
    # 4. Regresar la lista con el orden cronológico de eliminación
    return eliminados


def formatear_salida(orden: Iterable[int]) -> str:
    """Convierte una secuencia de enteros al formato de salida de CSES."""

    return " ".join(str(numero) for numero in orden)


def resolver_desde_texto(texto: str) -> str:
    """Resuelve el problema a partir del texto de entrada.

    Esta función permite probar el formato completo de entrada y salida.
    """

    if not isinstance(texto, str):
        raise TypeError("texto debe ser una cadena")

    partes = texto.split()
    if len(partes) != 1:
        raise ValueError("la entrada debe contener únicamente n")

    n = int(partes[0])
    orden = orden_eliminacion(n)
    return formatear_salida(orden) + "\n"

