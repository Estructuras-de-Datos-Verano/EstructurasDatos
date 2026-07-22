# Guía de revisión de Pull Request

Revisar código no significa buscar culpables. Significa ayudar a que una solución sea más correcta, clara y verificable.

> [!NOTE]
> En Clase 13 la revisión también se entrega como archivo Markdown dentro de la carpeta del compañero.

## Qué revisar

- Correctitud: ¿cumple el contrato?
- Invariante: ¿preserva BST y balance AVL?
- Rotaciones: ¿actualiza enlaces y alturas?
- Pruebas: ¿cubren casos simples y dobles?
- Documentación: ¿los nombres y docstrings explican intención?
- Git: ¿la entrega está en la carpeta correcta?

## Comentarios bloqueantes

Un comentario bloqueante señala algo que debe corregirse antes de mezclar.

Malo:

> No sirve.

Bueno:

> Bloqueante: el caso RL falla porque se aplica rotación izquierda directamente sobre el nodo desbalanceado. Para RL primero debe rotarse a la derecha el hijo derecho y luego a la izquierda el nodo desbalanceado.

## Comentarios sugeridos

Un comentario sugerido mejora claridad sin impedir necesariamente el avance.

Malo:

> Cambia esto.

Bueno:

> Sugerencia: renombrar `fb` a `factor_balance` haría más legible la condición de rotación.

## Cómo responder revisiones

- Agradece la observación.
- Explica si aceptas o no el cambio.
- Si cambiaste código, menciona dónde.
- Si no cambiaste, justifica técnicamente.

Ejemplo:

> Gracias. Actualicé `_rotar_derecha` para recalcular primero la altura del nodo que baja y después la nueva raíz local. También agregué una prueba para LL.

## Cómo justificar una observación

Una buena observación tiene tres partes:

1. evidencia;
2. impacto;
3. sugerencia.

Ejemplo:

> Evidencia: con `[30, 10, 20]` la raíz queda en 30. Impacto: el árbol sigue desbalanceado. Sugerencia: revisar el caso LR como rotación izquierda sobre el hijo izquierdo seguida de rotación derecha.

## Plantilla de revisión

```markdown
# Revisión de PR

## Resumen

## Código

## Pruebas

## Fortalezas

## Mejoras

## Salida completa de pytest

## Conclusión
```

## Checklist del revisor

- [ ] Descargué la rama.
- [ ] Ejecuté pruebas públicas.
- [ ] Ejecuté mis pruebas.
- [ ] Agregué `revision_nombre.md`.
- [ ] Pegué salida completa de pytest.
- [ ] Hice comentarios útiles.

> [!WARNING]
> No basta con decir "pasa mis pruebas". Debes pegar la salida completa para que la revisión sea reproducible.
