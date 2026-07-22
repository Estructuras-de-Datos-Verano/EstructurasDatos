# Guía de GitHub — Clase 16

Rama: `clase-16-nombre`. PR: `[Clase 16] Nombre - Dijkstra robusto`.

```bash
git switch -c clase-16-nombre
git add entregas/nombre/clase_16
git commit -m "[TEST] Reproduce peso bool inválido"
git commit -m "[FIX] Valida tipos y dominio de pesos"
```

La descripción del PR incluye resumen, contratos protegidos, pruebas, salida de pytest, dificultades, aspectos a revisar y checklist.

Antes de abrirlo:

```bash
git branch --show-current
git status
git diff --name-only origin/main
```

> [!CAUTION]
> El diff debe contener únicamente `entregas/nombre/clase_16/`.

