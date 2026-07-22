# Guía para estudiantes

## Encontrar el material de una clase

Los materiales oficiales están en `curso/clase_XX/`. Comienza por el README de
la clase y conserva las rutas internas indicadas para notebooks, código base y
pruebas.

## Ubicar una entrega

Todas las entregas de una persona están agrupadas bajo su identificador:

```text
entregas/<alumno>/clase_XX/
```

No coloques nuevas entregas directamente en `entregas/clase_XX/`. Para revisar
quién entregó una clase sin duplicar contenido, consulta
`docs/entregas_por_clase/clase_XX.md`.

## Ejecutar pruebas desde la raíz

Cuando una clase usa `implementacion.py`, indica explícitamente la entrega y
las pruebas públicas:

```bash
python3 scripts/evaluar.py \
  entregas/<alumno>/clase_XX \
  curso/clase_XX/tests
```

Si agregas pruebas propias, pásalas como tercer argumento. Consulta siempre el
README de la clase porque las clases tempranas pueden usar imports locales
distintos.

## Convención del identificador

Usa minúsculas, sin acentos ni espacios. No renombres carpetas de otra persona
ni combines entregas de clases diferentes.

