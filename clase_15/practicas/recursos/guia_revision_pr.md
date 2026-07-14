# Guía de revisión técnica — Clase 15

Crea `revision_nombre_revisor.md` dentro de la entrega revisada.

## Flujo

1. Confirma rama y archivos.
2. Resume el enfoque sin reescribir la solución.
3. Revisa inicialización, relajación, heap y entradas obsoletas.
4. Revisa reconstrucción, errores y no mutación.
5. Ejecuta pruebas públicas y propias con `pytest -v`.
6. Pega la salida completa.
7. Escribe fortalezas y mejoras accionables.
8. Solicita respuesta del autor con checklist.

Ejemplo útil:

> En el grafo A→B=10, A→C=1 y C→B=2, `(10,B)` todavía relaja vecinos aunque `distancia[B]` ya vale 3. Compara el valor extraído justo después de `heappop` y agrega una prueba que proteja este caso.

> [!WARNING]
> Evalúa comportamientos observables y evidencia, no a la persona.

