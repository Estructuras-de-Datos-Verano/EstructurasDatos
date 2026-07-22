# Guía de Git para esta organización

Antes de preparar cambios, confirma la ruta y revisa el estado local:

```bash
pwd
git status --short
```

Una entrega nueva o corregida debe limitarse a:

```text
entregas/<alumno>/clase_XX/
```

El material oficial de la clase correspondiente vive en
`curso/clase_XX/`. No copies pruebas públicas ni implementaciones oficiales a
otra clase para resolver problemas de rutas.

Antes de registrar cambios, revisa los nombres afectados con:

```bash
git diff --name-only
```

Las reglas de ramas, títulos y revisiones específicas de una actividad se
encuentran en el README o la práctica de esa clase. Esta guía no sustituye esas
instrucciones.

