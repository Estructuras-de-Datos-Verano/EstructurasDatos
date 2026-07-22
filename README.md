# Curso de Estructuras de Datos

Este repositorio reúne el material oficial del curso y conserva las entregas
de los estudiantes en una organización longitudinal. La estructura permite
consultar una clase completa o seguir, sin duplicar archivos, las entregas de
un alumno a lo largo del curso.

## Organización del repositorio

```text
curso-alumnos/
├── curso/       # materiales oficiales por clase
├── entregas/    # trabajo entregado, organizado por alumno
├── docs/        # guías e índices secundarios por clase
├── scripts/     # herramientas generales del curso
└── pyproject.toml
```

No se crean carpetas globales de recursos, rúbricas o archivo mientras no
exista contenido que justifique su presencia. Los recursos exclusivos de una
clase permanecen dentro de esa clase.

## Material por clase

Cada clase vive en `curso/clase_XX/`. Según el tema puede contener notebooks,
código base, pruebas públicas, prácticas, presentación y recursos propios.

Ejemplo:

```text
curso/clase_14/
├── README.md
├── notebooks/
├── src/
├── tests/
├── practicas/
└── presentacion/
```

## Entregas por alumno

Las entregas se guardan en `entregas/<alumno>/clase_XX/`. El identificador del
alumno usa minúsculas, no lleva acentos ni espacios y es estable entre clases.
Los archivos entregados se conservan sin corregir ni combinar.

Consulta [el índice de alumnos](entregas/README.md) o el archivo
[`entregas/alumnos.csv`](entregas/alumnos.csv).

## Índices por clase

La vista secundaria `docs/entregas_por_clase/clase_XX.md` enumera qué alumnos
entregaron cada clase. Sus enlaces apuntan a la única copia física ubicada bajo
`entregas/`.

## Scripts

Las herramientas generales están documentadas en [`scripts/README.md`](scripts/README.md).
Los scripts de asignación no deben ejecutarse solo para consultar el
repositorio. `scripts/generar_indices.py` regenera los índices derivados y
`scripts/validar_entregas.py` revisa la estructura sin cambiarla.

## Pruebas

Las configuraciones de pytest permanecen dentro de cada clase porque distintas
pruebas importan paquetes locales llamados `src` y, desde algunas clases,
esperan el `implementacion.py` de una entrega. Desde la raíz, usa el evaluador
con rutas explícitas:

```bash
python3 scripts/evaluar.py \
  entregas/max/clase_14 \
  curso/clase_14/tests
```

Para probar solo la implementación oficial de una clase temprana, entra en la
carpeta correspondiente y ejecuta su configuración local.

## Convenciones de nombres

- Clases: `clase_XX`, con dos dígitos.
- Alumnos: minúsculas, sin acentos ni espacios; se permiten guiones bajos.
- Entrega: `entregas/<alumno>/clase_XX/`.
- Material oficial: `curso/clase_XX/`.
- Índice secundario: `docs/entregas_por_clase/clase_XX.md`.

## Cómo navegar el repositorio

- Para estudiar un tema, abre `curso/clase_XX/README.md`.
- Para revisar la trayectoria de un alumno, abre `entregas/<alumno>/README.md`.
- Para comparar las entregas de una clase, abre
  `docs/entregas_por_clase/clase_XX.md`.
- Para validar rutas antes de trabajar, ejecuta
  `python3 scripts/validar_entregas.py`.

