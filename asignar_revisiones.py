import random


def asignar_revisiones(alumnos, semilla):
    """
    Asigna a cada alumno otro alumno para revisar.

    La asignación es aleatoria pero reproducible usando una semilla.
    Ningún alumno se revisa a sí mismo.
    """
    if len(alumnos) < 2:
        raise ValueError("Se necesitan al menos dos alumnos presentes.")

    generador = random.Random(semilla)

    revisores = alumnos.copy()
    revisados = alumnos.copy()

    while True:
        generador.shuffle(revisados)

        if all(revisor != revisado for revisor, revisado in zip(revisores, revisados)):
            break

    return list(zip(revisores, revisados))


def obtener_alumnos_presentes(alumnos):
    """
    Pregunta si están todos los alumnos.

    Si no están todos, muestra una lista numerada y permite indicar
    los números de los alumnos ausentes separados por espacios.
    """
    respuesta = input("¿Están todos los alumnos? (s/n): ").strip().lower()

    if respuesta in ["s", "si", "sí"]:
        return alumnos.copy()

    print("\nLista de alumnos:")
    for indice, alumno in enumerate(alumnos, start=1):
        print(f"{indice}. {alumno}")

    entrada = input(
        "\nEscribe los números de los alumnos faltantes separados por espacios: "
    ).strip()

    if not entrada:
        return alumnos.copy()

    indices_faltantes = set()

    for dato in entrada.split():
        try:
            indice = int(dato)
            if 1 <= indice <= len(alumnos):
                indices_faltantes.add(indice)
            else:
                print(f"Advertencia: {indice} no está en la lista.")
        except ValueError:
            print(f"Advertencia: {dato} no es un número válido.")

    alumnos_presentes = [
        alumno
        for indice, alumno in enumerate(alumnos, start=1)
        if indice not in indices_faltantes
    ]

    return alumnos_presentes


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

fecha_clase = "2026-07-16"

alumnos_presentes = obtener_alumnos_presentes(alumnos)

print("\nAlumnos presentes:")
for alumno in alumnos_presentes:
    print(f"- {alumno}")

asignaciones = asignar_revisiones(alumnos_presentes, fecha_clase)

print("\nAsignaciones de revisión:")
for revisor, revisado in asignaciones:
    print(f"{revisor} revisa a {revisado}")