from collections import deque
from pathlib import Path
import subprocess
import sys


def orden_eliminacion_borrador(n):
    if n < 1:
        raise ValueError("n debe ser al menos 1")

    
    vivos = deque(range(1, n + 1))
    eliminados = []

    
    while len(vivos) > 1:
        se_salva = vivos.popleft()
        vivos.append(se_salva)
        
        se_elimina = vivos.popleft()
        eliminados.append(se_elimina)

    if vivos:
        eliminados.append(vivos.popleft())

    return eliminados

n_prueba = 7
resultado = orden_eliminacion_borrador(n_prueba)
print(f"Orden de eliminación para n={n_prueba}: {resultado}")
#a