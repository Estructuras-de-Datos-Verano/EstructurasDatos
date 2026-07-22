# Guía de GitHub — Clase 14

## Rama y commits

La rama obligatoria es `clase-14-nombre`: minúsculas, guiones, sin espacios, acentos ni guiones bajos. No reutilices una rama anterior.

Commits: `[TIPO] Descripción breve`, con una intención principal. Tipos: `[FEAT]`, `[FIX]`, `[TEST]`, `[DOC]`, `[STYLE]`, `[REFACTOR]`, `[REVIEW]`.

```bash
git switch -c clase-14-nombre
git add entregas/nombre/clase_14
git commit -m "[FEAT] Implementa inserción en min-heap"
```

## Antes del PR

```bash
git branch --show-current
git status
git diff --name-only origin/main
```

> [!CAUTION]
> El último comando debe mostrar únicamente `entregas/nombre/clase_14/`. Si aparecen otra clase, otro alumno, `.DS_Store`, `__pycache__` o `.pyc`, no abras todavía el PR.

Título: `[Clase 14] Nombre - Heap y cola de prioridad`.

La descripción incluye resumen, cambios, pruebas, dificultades, aspectos a revisar, checklist y ruta exacta.

