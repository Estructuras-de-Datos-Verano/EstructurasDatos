
# Importar librerias necesarias

from collections import deque
from pathlib import Path
import subprocess
import sys

raiz = Path.cwd()
if not (raiz / "src").exists() and (raiz.parent / "src").exists():
    raiz = raiz.parent

if str(raiz) not in sys.path:
    sys.path.insert(0, str(raiz))

print(f"Carpeta de trabajo detectada: {raiz}")


# Función axuliar validar_n (piede explicitamente utilizarla en el notebook)

def validar_n(n: int) -> None:
    if not isinstance(n, int):
        raise TypeError("n debe ser un entero")
    if n < 1:
        raise ValueError("n debe ser al menos 1")
    
# Función principal orden_eliminacion (la que se pide resolver en el notebook)

def orden_eliminacion(n: int) -> list[int]:
    validar_n(n)

    vivos = deque(range(1, n + 1))
    eliminados = []
    
    while vivos:
        vivos.append(vivos.popleft())
        eliminados.append(vivos.popleft())

    return eliminados

# Ejemplo de uso que viene ne el josephus.py de 7 niños explicitamente

print("Ejemplo del orden de eliminación de los niños: ", orden_eliminacion(7))
