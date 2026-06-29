import random

def asignar_revisiones(alumnos, semilla):
    """
    Asigna a cada alumno otro alumno para revisar.

    La asignación es aleatoria pero reproducible usando una semilla.
    Ningún alumno se revisa a sí mismo.
    """
    if len(alumnos) < 2:
        raise ValueError("Se necesitan al menos dos alumnos.")

    generador = random.Random(semilla)

    revisores = alumnos.copy()
    revisados = alumnos.copy()

    while True:
        generador.shuffle(revisados)

        if all(revisor != revisado for revisor, revisado in zip(revisores, revisados)):
            break

    return list(zip(revisores, revisados))

alumnos = [
    "Leo",
    "Max",
    "Aristeo",
    "Arturo",
    "Ivan",
    "Tiago",
    "Gustavo",
    "Santi",
    "Pato",
    "Daniel",
]

fecha_clase = "2026-06-29"

asignaciones = asignar_revisiones(alumnos, fecha_clase)

for revisor, revisado in asignaciones:
    print(f"{revisor} revisa a {revisado}")