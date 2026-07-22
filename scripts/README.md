# Scripts del curso

## `asignar_revisiones.py`

Asigna revisores de manera aleatoria y reproducible a partir de una semilla.
Es interactivo y puede cambiar las asignaciones mostradas; no debe ejecutarse
solo para inspeccionar el repositorio.

## `evaluar.py`

Ejecuta pruebas públicas y, opcionalmente, pruebas extra sobre una entrega. La
carpeta de entrega se agrega temporalmente a `PYTHONPATH`.

```bash
python3 scripts/evaluar.py \
  entregas/<alumno>/clase_XX \
  curso/clase_XX/tests \
  entregas/<revisor>/clase_XX/test_estudiante.py
```

## `generar_indices.py`

Regenera `entregas/alumnos.csv`, los README de alumnos y los índices Markdown
de `docs/entregas_por_clase/`. Solo escribe archivos de índice conocidos; no
modifica el contenido de las entregas.

## `validar_entregas.py`

Comprueba la organización de clases y entregas, nombres, temporales y enlaces
de los índices. Es de solo lectura y devuelve un código distinto de cero si
encuentra errores estructurales.

