# Guía de GitHub para la Clase 13

El flujo del curso es:

```text
Issue -> Branch -> Commit -> Push -> Pull Request -> Review -> Merge
```

> [!IMPORTANT]
> No trabajes directamente sobre `main`.

## Branch

Crear rama:

macOS / Linux y Windows PowerShell:

```bash
git switch -c clase-13-nombre
```

Ver rama actual:

```bash
git branch --show-current
```

## Commit

Formato:

```text
[TIPO] Descripción
```

Ejemplos:

```text
[FEAT] Implementar rotación izquierda
[TEST] Agregar prueba para caso RL
[DOC] Completar discusión técnica
```

## Push

```bash
git push -u origin clase-13-nombre
```

## Pull Request

Un buen PR explica:

- qué cambió;
- cómo se probó;
- qué falta;
- qué parte quieres que revisen con más cuidado.

## Review

Durante la revisión:

1. Descarga la rama.
2. Ejecuta pruebas públicas.
3. Ejecuta tus pruebas propias.
4. Escribe `revision_nombre.md` en la carpeta del compañero.
5. Comenta en GitHub con evidencia.

## Merge

Solo se mezcla cuando:

- las pruebas pasan;
- la entrega está en la carpeta correcta;
- la revisión fue atendida;
- no hay archivos temporales.

> [!CAUTION]
> Antes de abrir PR revisa `git diff --name-only origin/main`. Si aparecen archivos fuera de tu entrega, corrígelo antes de pedir revisión.
