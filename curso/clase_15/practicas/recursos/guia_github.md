# Guía de GitHub — Clase 15

## Rama y commits

Usa `clase-15-nombre`, en minúsculas y sin espacios ni acentos.

```bash
git switch -c clase-15-nombre
git add entregas/nombre/clase_15
git commit -m "[FEAT] Implementa relajación de aristas"
```

Tipos sugeridos: `[FEAT]`, `[FIX]`, `[TEST]`, `[DOC]`, `[REFACTOR]`, `[REVIEW]`.

## Pull Request

Título: `[Clase 15] Nombre - Dijkstra`.

Descripción completa:

```markdown
## Resumen
Implementé Dijkstra, reconstrucción y pruebas propias.

## Cambios
- cola de prioridad con eliminación perezosa;
- validación de pesos;
- reconstrucción de caminos.

## Pruebas
Comando y resultado completo.

## Dificultades
Qué costó y cómo se resolvió.

## Aspectos a revisar
Caso concreto donde quieres retroalimentación.

## Checklist
- [ ] Solo cambié mi carpeta.
- [ ] Todas las pruebas pasan.
```

Antes de abrirlo:

```bash
git branch --show-current
git status
git diff --name-only origin/main
```

> [!CAUTION]
> El diff debe mostrar únicamente `entregas/nombre/clase_15/`.

