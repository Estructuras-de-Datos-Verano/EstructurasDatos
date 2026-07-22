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
    eliminados: list[int] = []

    while vivos:
        if len(vivos) == 1:
            eliminados.append(vivos.popleft())
        else:
            sobreviviente = vivos.popleft()
            vivos.append(sobreviviente)

            eliminado = vivos.popleft()
            eliminados.append(eliminado)

    return eliminados



