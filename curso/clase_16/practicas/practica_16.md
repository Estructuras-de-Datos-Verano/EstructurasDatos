# Práctica 16 — Robustecer y revisar Dijkstra

## Idea central

> [!IMPORTANT]
> Antes de corregir una línea, expresa el contrato roto con una entrada y una prueba que falle.

## Entrega

Crea `entregas/nombre/clase_16/` con:

- `implementacion.py`
- `test_estudiante.py`
- `notebook.md`
- `discusion.md`
- `reporte_pytest.md`
- `revision_tecnica.md`

La entrega implementa `_normalizar_grafo`, `dijkstra`, `reconstruir_camino` y `camino_minimo` usando las firmas de `src/contratos_dijkstra.py`.

## Parte 1 — Auditoría antes de editar

Lee `src/dijkstra_para_revisar.py`. Documenta al menos cinco hallazgos:

| Contrato | Entrada mínima | Observado | Esperado | Test propuesto |
| --- | --- | --- | --- | --- |
| peso no negativo | | | | |
| vecino implícito | | | | |
| origen válido | | | | |
| entrada obsoleta | | | | |
| representación | | | | |

No basta escribir “falta validación”. Incluye tipo de excepción o resultado exacto.

## Parte 2 — Normalización robusta

Implementa una copia que:

- acepte `Mapping[str, Sequence[tuple[str, int | float]]]`;
- no comparta listas con la entrada;
- agregue vecinos que solo aparezcan como destino;
- convierta pesos válidos a `float`;
- rechace nodos o vecinos no `str`;
- rechace aristas que no sean pares;
- rechace bool y pesos no numéricos con `TypeError`;
- rechace NaN, infinitos y negativos con `ValueError`.

> [!WARNING]
> `isinstance(True, int)` es verdadero. La comprobación de bool debe ser explícita.

## Parte 3 — Dijkstra y reconstrucción

Conserva estos invariantes:

1. todo nodo normalizado existe en distancias y predecesores;
2. el heap guarda candidaturas históricas `(distancia, nodo)`;
3. solo una candidatura igual a la distancia vigente relaja vecinos;
4. una mejora actualiza distancia, predecesor y heap;
5. el grafo original no cambia.

`reconstruir_camino` distingue clave ausente, inalcanzable, origen=destino y ciclo. `camino_minimo` coordina sin duplicar Dijkstra.

## Parte 4 — Pruebas propias

Agrega al menos cinco pruebas explicadas:

1. bool no se acepta como peso;
2. vecino implícito y no mutación;
3. entrada obsoleta;
4. NaN o infinito;
5. ciclo de predecesores.

Usa parametrización cuando varias entradas protejan la misma regla.

```bash
python3 scripts/evaluar.py entregas/nombre/clase_16 curso/clase_16/tests entregas/nombre/clase_16/test_estudiante.py
```

```powershell
py scripts/evaluar.py entregas/nombre/clase_16 curso/clase_16/tests entregas/nombre/clase_16/test_estudiante.py
```

En `reporte_pytest.md` incluye comando, salida completa, número de pruebas, resultado y un fallo que hayas convertido en regresión automatizada.

## Parte 5 — Discusión

Responde:

1. Diferencia entre algoritmo correcto y función robusta.
2. Razón de separar normalización.
3. Mapping/Sequence frente a dict/list.
4. TypeError frente a ValueError.
5. Bool, NaN e infinito.
6. Copia defensiva.
7. Vecino implícito.
8. Invariante de entradas obsoletas.
9. Responsabilidades de reconstrucción.
10. Matriz contrato–riesgo–prueba.
11. Complejidad de normalización y Dijkstra.
12. Operación dominante en BFS, Dijkstra, Kruskal y topológico.

## Parte 6 — Revisión técnica

Revisa la entrega de un compañero con `practicas/recursos/guia_revision_pr.md`. `revision_tecnica.md` debe contener al menos:

- una fortaleza específica;
- un contrato incumplido o caso no cubierto;
- entrada reproducible;
- test ejecutado;
- recomendación localizada;
- respuesta del autor.

## GitHub

Rama: `clase-16-nombre`.

Commits sugeridos:

```text
[TEST] Reproduce vecino implícito en Dijkstra
[FIX] Normaliza nodos y pesos sin mutar entrada
[TEST] Protege entradas obsoletas y pesos no finitos
[DOC] Documenta contratos y decisiones de revisión
```

PR: `[Clase 16] Nombre - Dijkstra robusto`.

## Checklist

- [ ] Solo modifiqué `entregas/nombre/clase_16/`.
- [ ] Entregué los seis archivos.
- [ ] Respondí el notebook fuera del `.ipynb`.
- [ ] Cada corrección importante tiene una prueba.
- [ ] No muté la entrada.
- [ ] Distinguí errores de tipo, dominio y clave.
- [ ] Probé entrada obsoleta, inalcanzable y ciclo.
- [ ] Guardé la salida completa de pytest.
- [ ] La revisión incluye evidencia reproducible.
- [ ] No agregué cachés ni archivos ajenos.

## Rúbrica

| Criterio | Puntos |
| --- | ---: |
| notebook.md y lectura profesional | 15 |
| normalización y validación | 20 |
| Dijkstra e invariante | 20 |
| reconstrucción y coordinación | 10 |
| pruebas propias | 15 |
| revisión técnica | 10 |
| discusión y reporte | 5 |
| GitHub y organización | 5 |
| **Total** | **100** |

